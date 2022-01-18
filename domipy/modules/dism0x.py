"""
Dimmer control module DDIM01
Controlls:
  DISM04
  DISM08
  DMOV01
  VAR - Binary version only

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domipy
import domipy.messages

class GenericDISM0xModule(domipy.Module):
    """
    Abstract DISM  control module     
    """
    COMMAND_CODE = 'UNK'

    def __init__(self, serial_number, controller):
        domipy.Module.__init__(self, serial_number, controller)

    def is_on(self, channel):
        if channel < self.number_of_channels():
            if self._values[channel] > 0:
                return True
        return False
    
    def get_value(self, channel):
        if channel < self.number_of_channels():
            return self._values[channel]
    
    def sim_long_push(self, channel):
        """
        Simulate long push
        """
        # TODO
        pass

    def sim_long_push_end(self, channel):
        """ 
        Simulate end of long push
        """
        # TODO
        pass

    def sim_short_push(self, channel):
        """
        Simulate short push
        """
        # TODO
        pass

    def sim_short_push_end(self, channel):
        """ 
        Simulate end of short push
        """
        # TODO
        pass

    def number_of_channels(self):
        raise NotImplementedError

    def _on_message(self, message):
        raise NotImplementedError

class DISM04Module(GenericDISM0xModule):

    COMMAND_CODE = 'IS4'

    def number_of_channels(self):
        return 4

    def _on_message(self, message):
        if isinstance(message, domipy.DISM4StatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))

class DISM08Module(GenericDISM0xModule):

    COMMAND_CODE = 'IS8'

    def number_of_channels(self):
        return 8

    def _on_message(self, message):
        if isinstance(message, domipy.DISM8StatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))
                    

class DMOV01Module(GenericDISM0xModule):

    COMMAND_CODE = 'DET'

    def number_of_channels(self):
        return 1

    def _on_message(self, message):
        if isinstance(message, domipy.DMOVStatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))
        

class DVARModule(GenericDISM0xModule):
    """
    4 LED's driver
    """
    COMMAND_CODE = 'VAR'

    def number_of_channels(self):
        return 1

    def _on_message(self, message):
        if isinstance(message, domipy.VARStatusMessage):
            self._values = message.get_values()
            
            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))

domipy.register_module_class(DISM04Module)
domipy.register_module_class(DISM08Module)
domipy.register_module_class(DMOV01Module)
domipy.register_module_class(DVARModule)