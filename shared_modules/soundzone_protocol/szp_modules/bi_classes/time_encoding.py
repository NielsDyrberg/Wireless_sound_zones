

class TimeEncoding:
    """
    A class containing time data, used for timing playback.

    Attributes
    ----------
    hour: The hour the chunk should be played
    minute: The minute the chunk should be played
    second: The second the chunk should be played
    mili_second: The mili_second the chunk should be played
    micro_second: The micro_second the chunk should be played

    Methods
    -------
    __init__(minute=None, second=None, mil_second=None, mic_second=None, n_second=None)
    encode()
        Encodes time data into a Bytearray.
    decode(buffer)
        Decodes a Bytearray, and fills it into the class variables
    """
    def __init__(self, hour=None, minute=None, second=None, mil_second=None, mic_second=None, n_second=None):
        """
        Initiates class variables
        :param hour: The hour the chunk should be played
        :param minute: The minute the chunk should be played
        :param second: The second the chunk should be played
        :param mil_second: The mili_second the chunk should be played
        :param mic_second: The micro_second the chunk should be played
        """
        self.hour = hour
        self.minute = minute
        self.second = second
        self.mili_second = mil_second
        self.micro_second = mic_second

    def encode(self) -> bytearray:
        """
        Encodes time data into a Bytearray.
        :return: Encoded Bytearray
        """
        encoded_time = self.hour.to_bytes(1, 'big')
        encoded_time += self.minute.to_bytes(1, 'big')
        encoded_time += self.second.to_bytes(1, 'big')
        encoded_time += self.mili_second.to_bytes(2, 'big')
        encoded_time += self.micro_second.to_bytes(2, 'big')
        return encoded_time

    def decode(self, buffer):
        """
        Decodes a Bytearray, and fills it into the class variables
        :param buffer: List of ints
        :return: None
        """
        self.hour = buffer[0]
        self.minute = buffer[1]
        self.second = buffer[2]
        self.mili_second = (buffer[3] << 8) + buffer[4]
        self.micro_second = (buffer[5] << 8) + buffer[6]