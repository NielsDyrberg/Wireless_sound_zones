

class XB3SetSoundFormat:
    """
    Class containing data for a 0xB3 set_sound_format package.

    Attributes
    ----------
    format_id: int
        The used format id.
    raw_setup: RawSetup
        Data for a raw file format. It is only used when format_id is 0x01

    Methods
    -------
    encode()
        Encodes the sound format into a hex string
    decode(buffer)
        Decodes a hex string containing data for a set_sound_format package.
    """
    def __init__(self):
        """
        Initiates class variables
        """
        self.format_id = None
        self.raw_setup = None

    def encode(self):
        """
        Encodes the sound format into a hex string
        :return: Encoded hex string
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
        Decodes a hex string containing data for a set_sound_format package.
        :param buffer: List of ints that should be decoded.
        :return: None
        """
        self.format_id = buffer[0]
        if self.format_id == 0x01:
            raw_setup_buffer = buffer[1:]
            self.raw_setup = RawSetup()
            self.raw_setup.decode(raw_setup_buffer)


class RawSetup:
    """
    Class containing data for a RawSetup package.

    Attributes
    ----------
    sample_rate: int
    sample_resolution: RawSetup

    Methods
    -------
    encode()
        Encodes the RawSetup into a hex string
    decode(buffer)
        Decodes a hex string containing data for a RawSetup package.
    """
    def __init__(self):
        """
        Initiates class variables
        """
        self.sample_rate = None
        self.sample_resolution = None

    def encode(self):
        """
        Encodes the RawSetup package
        :return: Encoded hex string
        """
        return "{:04X}{:02X}".format(self.sample_rate, self.sample_resolution)

    def decode(self, buffer):
        """
        Decodes a hex string containing data for a RawSetup package.
        :param buffer: List of ints that should be decoded.
        :return: None
        """
        self.sample_rate = (buffer[0] << 8) + buffer[1]
        self.sample_resolution = buffer[2]

