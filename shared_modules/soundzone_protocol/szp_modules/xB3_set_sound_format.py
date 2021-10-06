

class XB3SetSoundFormat:
    def __init__(self):
        self.format_id = None
        self.raw_setup = None

    def encode(self):
        """
        Encodes the sound format into a hex string
        :return:
        """
        encoded_send = ""
        encoded_send += "{:02X}".format(self.format_id)
        if self.format_id == 0x01:
            if self.raw_setup is None:
                raise Exception("raw_setup obj should be set, it is None")
            encoded_send += self.raw_setup.encode()
        return encoded_send

    def decode(self, buffer):
        """
        :param buffer:
        :return: None
        """
        self.format_id = buffer[0]
        if self.format_id == 0x01:
            raw_setup_buffer = buffer[1:]
            self.raw_setup = RawSetup()
            self.raw_setup.decode(raw_setup_buffer)


class RawSetup:
    def __init__(self):
        self.sample_rate = None
        self.sample_resolution = None

    def encode(self):
        return "{:04X}{:02X}".format(self.sample_rate, self.sample_resolution)

    def decode(self, buffer):
        self.sample_rate = (buffer[0] << 8) + buffer[1]
        self.sample_resolution = buffer[2]

