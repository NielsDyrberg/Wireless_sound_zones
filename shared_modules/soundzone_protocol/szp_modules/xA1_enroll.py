

class XA1Enroll:
    """
    Class containing data for a 0xA1 enroll package.

    Attributes
    ----------
    client_id: int
        CLient_id
    res: int
        response, is either 0 (Dennie), or 1 (Accepts)

    Methods
    -------
    encode()
    decode(buffer)
    """
    def __init__(self):
        """
        Initiates class variables
        """
        self.client_id = None
        self.res = None

    def encode(self):
        """
        Encodes the enroll package
        :return: Encoded hex string
        """
        encoded_send = ""
        encoded_send += "{:02X}".format(self.res)
        return encoded_send

    def decode(self, buffer):
        """
        Decodes a hex string containing data for a enroll package.
        :param buffer: List of ints that should be decoded.
        :return: None
        """
        self.client_id = buffer[0]
