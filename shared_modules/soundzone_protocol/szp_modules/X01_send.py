

LEN_TIME = 8


class X01Send:
    def __init__(self):
        self.time = Time()
        self.payload = []

    def encode(self):
        """
        Encodes nothing
        :return:
        """
        encoded_send = ""
        encoded_send += self.time.encode()
        encoded_send += "".join(["{:02X}".format(x) for x in self.payload])
        return encoded_send

    def decode(self, buffer):
        """
        :param buffer:
        :return: None
        """
        time_buffer = buffer[:LEN_TIME]
        self.time = Time()
        self.time.decode(time_buffer)

        self.payload = [((x << 8) + y) for x, y in zip(buffer[LEN_TIME::2], buffer[LEN_TIME+1::2])]


class Time:
    def __init__(self, minute=None, second=None, mil_second=None, mic_second=None, n_second=None):
        self.minute = minute
        self.second = second
        self.mili_second = mil_second
        self.micro_second = mic_second
        self.nano_second = n_second

    def encode(self):
        return "{:02X}{:02X}{:04X}{:04X}{:04X}".format(self.minute, self.second, self.mili_second, self.micro_second,
                                                       self.nano_second)

    def decode(self, buffer):
        self.minute = buffer[0]
        self.second = buffer[1]
        self.mili_second = (buffer[2] << 8) + buffer[3]
        self.micro_second = (buffer[4] << 8) + buffer[5]
        self.nano_second = (buffer[6] << 8) + buffer[7]
