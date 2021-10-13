
from .bi_classes import *


LEN_TIME = 7


class X01Send:
    """
    Class containing data for a 0x01 send package.

    This class is used when sending a package containing a sound chunk. It encodes both time and sound data.

    Attributes
    ----------
    time: Time
        An object containing time data.
    payload: list of ints
        Ints of 16 bits, containing sound data.

    Methods
    -------
    encode()
        Encodes the send package
    decode(buffer: list of ints)
        Decodes a hex string containing data for a send package.
    """
    def __init__(self):
        """
        Initiates class variables
        """
        self.time = TimeEncoding()
        self.payload = []

    def encode(self) -> str:
        """
        Encodes the send package
        :return: Encoded hex string
        """
        encoded_send = ""
        encoded_send += self.time.encode()
        encoded_send += "".join(["{:02X}".format(x) for x in self.payload])
        return encoded_send

    def decode(self, buffer) -> None:
        """
        Decodes a hex string containing data for a send package.
        :param buffer: List of ints
        :return: None
        """
        time_buffer = buffer[:LEN_TIME]
        self.time = TimeEncoding()
        self.time.decode(time_buffer)

        self.payload = [x for x in buffer[LEN_TIME:]]
