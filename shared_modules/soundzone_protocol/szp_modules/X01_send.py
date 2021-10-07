

LEN_TIME = 8


class X01Send:
    """
    Class containing data for a 0x01 send package.

    This class is used when sending a package containing a sound chunk. It encodes both time and sound data.

    Atributes
    ---------
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
        self.time = Time()
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
        self.time = Time()
        self.time.decode(time_buffer)

        self.payload = [((x << 8) + y) for x, y in zip(buffer[LEN_TIME::2], buffer[LEN_TIME+1::2])]


class Time:
    """
    A class containing time data, used for timing playback.

    Atributes
    ---------
    minute: The minute the chunk should be played
    second: The second the chunk should be played
    mili_second: The mili_second the chunk should be played
    micro_second: The micro_second the chunk should be played
    nano_second: The nano_second the chunk should be played

    Methods
    -------
    __init__(minute=None, second=None, mil_second=None, mic_second=None, n_second=None)
    encode()
        Encodes time data into a hex string.
    decode(buffer)
        Decodes a hex string, and fills it into the class variables
    """
    def __init__(self, minute=None, second=None, mil_second=None, mic_second=None, n_second=None):
        """
        Initiates class variables
        :param minute: The minute the chunk should be played
        :param second: The second the chunk should be played
        :param mil_second: The mili_second the chunk should be played
        :param mic_second: The micro_second the chunk should be played
        :param n_second: The nano_second the chunk should be played
        """
        self.minute = minute
        self.second = second
        self.mili_second = mil_second
        self.micro_second = mic_second
        self.nano_second = n_second

    def encode(self) -> str:
        """
        Encodes time data into a hex string.
        :return: Encoded hex string
        """
        return "{:02X}{:02X}{:04X}{:04X}{:04X}".format(self.minute, self.second, self.mili_second, self.micro_second,
                                                       self.nano_second)

    def decode(self, buffer):
        """
        Decodes a hex string, and fills it into the class variables
        :param buffer: List of ints
        :return: None
        """
        self.minute = buffer[0]
        self.second = buffer[1]
        self.mili_second = (buffer[2] << 8) + buffer[3]
        self.micro_second = (buffer[4] << 8) + buffer[5]
        self.nano_second = (buffer[6] << 8) + buffer[7]
