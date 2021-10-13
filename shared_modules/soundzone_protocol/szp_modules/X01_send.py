
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
        Decodes a Bytearray containing data for a send package.
    """
    def __init__(self):
        """
        Initiates class variables
        """
        self.time = TimeEncoding()
        self.payload = []

    def encode(self) -> bytearray:
        """
        Encodes the send package
        :return: Encoded Bytearray
        """
        encoded_send = self.time.encode()
        list_of_payload = [x.to_bytes(1, 'big') for x in self.payload]
        for byte in list_of_payload:
            encoded_send += byte
        return encoded_send

    def decode(self, buffer) -> None:
        """
        Decodes a Bytearray containing data for a send package.
        :param buffer: List of ints
        :return: None
        """
        time_buffer = buffer[:LEN_TIME]
        self.time = TimeEncoding()
        self.time.decode(time_buffer)

        self.payload = [x for x in buffer[LEN_TIME:]]
