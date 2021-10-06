

class XF1CheckConn:
    def __init__(self):
        self.ack = None
        self._ack = 0x01

    def encode(self):
        """
        Encodes an acknowledgment
        :return: "01"
        """
        return "{:02X}".format(self._ack)  # Nothing to encode

    def decode(self, buffer):
        """
        There should only be one byte to decode
        :param buffer:
        :return: None
        """
        self.ack = buffer[0]
