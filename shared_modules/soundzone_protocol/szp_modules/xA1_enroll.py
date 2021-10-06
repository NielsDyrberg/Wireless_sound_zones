

class XA1Enroll:
    def __init__(self):
        self.client_id = None
        self.res = None

    def encode(self):
        """
        Encodes nothing
        :return:
        """
        encoded_send = ""
        encoded_send += "{:02X}".format(self.res)
        return encoded_send

    def decode(self, buffer):
        """
        :param buffer:
        :return: None
        """
        self.client_id = buffer[0]
