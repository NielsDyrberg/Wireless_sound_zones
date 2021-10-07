

_ACK = 0x01


class XF1CheckConn:
    """
    A class used for debugging.

    It works like a ping function.

    Attributes
    ----------
    ack: int
        The ack sent/recieved

    Methods
    -------
    encode()
    decode(buffer)
    """
    def __init__(self):
        self.ack = None

    def encode(self):
        """
        Encodes an acknowledgment
        :return: "01"
        """
        return "{:02X}".format(_ACK)  # Nothing to encode

    def decode(self, buffer):
        """
        There should only be ack byte to decode
        :param buffer: list of int: should only contain one byte
        :return: None
        """
        self.ack = buffer[0]
