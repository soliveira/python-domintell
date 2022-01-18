"""
:author: Thomas Delaet <thomas@delaet.org>

Port for Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import base64
import domipy


class Message(object):
    # pylint: disable-msg=R0904
    """
    Base Domintell message
    """

    def __init__(self, moduleType=None, serialNumber=None):
        self.moduleType = moduleType
        self.serialNumber = serialNumber
        self.dataType = None
        self.data = None

    def set_attributes(self, module_type, serial_number, data_type, data):
        """
        :return: None
        """
        assert isinstance(module_type, str)
        assert isinstance(serial_number, str)
        assert isinstance(data_type, str)
        assert isinstance(data, str)
        self.moduleType = module_type
        self.serialNumber = serial_number
        self.dataType = data_type
        self.data = data

    def populate(self, serial_number, data_type, data_string):
        """
        :return: None
        """
        raise NotImplementedError

    def get_values(self):
        raise NotImplementedError

    def to_json_basic(self):
        """
        Create JSON structure with generic attributes

        :return: dict
        """
        return {'name': self.__class__.__name__, 'module_type': self.moduleType,
                'serial_number': self.serialNumber, 'data_type': self.dataType}

    def to_string(self):
        """
        Convert to domintell controll string

        This method may be overridden in subclasses to include more than just generic attributes

        :return: str
        """
        return "{}{}".format(self.moduleType, self.serialNumber)

    def to_json(self):
        """
        Dump object structure to JSON

        This method should be overridden in subclasses to include more than just generic attributes

        :return: str
        """
        return json.dumps(self.to_json_basic())

    def __str__(self):
        return self.to_json()

    def parser_error(self, message):
        """
        :return: None
        """
        raise domipy.ParserError(self.__class__.__name__ + " " + message)
    
    def is_binary(self):
        return False

