"""
:author: Thomas Delaet <thomas@delaet.org>

Port for Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>

"""
import socket
import time
import threading
import logging
from queue import Queue
import ssl
import serial
import serial.threaded
import websocket
import domipy

class Protocol(serial.threaded.Protocol):
    """Serial protocol."""

    def data_received(self, data):
        # pylint: disable-msg=E1101
        self.parser(data)


class DomintellException(Exception):
    """Domintell Exception."""
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

class DomintellConnection(object):
    """
    Generic Domintell connection
    """

    controller = None

    def set_controller(self, controller):
        """
        :return: None
        """
        assert isinstance(controller, domipy.Controller)
        self.controller = controller

    def send(self, message, callback=None):
        """
        :return: None
        """
        raise NotImplementedError

class WSSConnection(DomintellConnection):
    """
        Wrapper for Secure Web Socket connection configuration
    """
    def __init__(self, device, controller=None, ping_interval=0):
        DomintellConnection.__init__(self)
        self.logger = logging.getLogger('domintell')
        self._device = device
        self.controller = controller
        self.ping_interval = ping_interval 

        try:
            websocket.enableTrace(True)
            self._socket =websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
            self._socket.connect(device)

        except Exception as ex:
            self.logger.error("Could not open socket, \
                              no messages are read or written to the bus")
            raise DomintellException("Could not open socket port") from ex
        # build a read thread
        self._listen_process = threading.Thread(None, self.read_daemon,
                                         "domintell-process-reader", (), {})
        self._listen_process.daemon = True
        self._listen_process.start()

        # build a writer thread
        self._write_queue = Queue()
        self._write_process = threading.Thread(None, self.write_daemon,
                                               "domintell-connection-writer", (), {})
        self._write_process.daemon = True
        self._write_process.start()

        # build a ping thread
        self._ping_process = threading.Thread(None, self.ping_daemon,
                                            "domintell-ping-writer", (), {})
        self._ping_process.daemon = True

    def stop(self):
        """Close socket."""
        self.logger.warning("Stop executed")
        try:
            self._socket.close()
        except Exception as ex:
            self.logger.error("Error while closing socket")
            raise DomintellException("Error while closing socket") from ex
        time.sleep(1)

    def feed_parser(self, data):
        """Parse received message."""
        self.controller.feed_parser(data)

    def send(self, message, callback=None):
        """Add message to write queue."""
        assert isinstance(message, domipy.Message)
        self._write_queue.put_nowait((message, callback))

    def read_daemon(self):
        """Reads incoming data."""
        while True:
            data = self._socket.recv()
            self.feed_parser(data)

    def write_daemon(self):
        """Write thread."""
        while True:
            (message, callback) = self._write_queue.get(block=True)
            self.logger.info("Sending message to socket: %s", str(message))
            self.logger.debug("Sending controll message:  %s", message.to_string())
            if message.is_binary():
                self._socket.send(message.to_string())
            else:
                self._socket.send(bytes(message.to_string(),'ascii'))
            time.sleep(1)
            if callback:
                callback()

    def ping_daemon(self):
        """Put ping message into write thread every ping_interval sec"""
        while True:
            ping_message = domipy.messages.Hello()
            self.send(ping_message)
            time.sleep(self.ping_interval)

    def start_ping(self, interval=-1):
        """
        Start sending PING message to DETH02 every minute.
        DETH02 will end Login 'session' if no messages received
        in predefined interval (10mins default)
        """
        if interval > -1:
            self.ping_interval = interval

        if self.ping_interval > 0:
            if not self._ping_process.is_alive():
                self._ping_process.start()
