
from .utils import get_project_root
from scipy.io import wavfile


class MusicReader:
    def __init__(self, file_name, file_format, size):
        self.file_format = file_format
        self.max_block_size = size
        root_path = get_project_root()
        self.f = None
        self.sample_rate = None
        self.data = None
        self.resolution = None
        self.head = None
        if self.file_format == "wav":
            self.sample_rate, self.data = wavfile.read(f"{root_path}/songs/{file_name}")

        if self.data is not None:
            # Get the resolution
            res = self.data.dtype.name
            if res == "int16":
                self.resolution = 2  # resolution is 2 bytes

    def get_format(self) -> tuple:
        return self.sample_rate, self.resolution

    def read_block(self, channel):
        if self.file_format == "wav":
            if self.head is None:
                self.head = 0
            old_head = self.head
            self.head += self.max_block_size

            if channel is None:
                ret = self.data[old_head:self.head]
            elif channel.lower() == "left":
                ret = self.data[old_head:self.head, 0]
            else:
                raise Exception(f"Channel not supported, got: {channel}")

            ret = [x.to_bytes(2, 'big', signed=True) for x in ret.tolist()]

            if not ret or None:
                ret = None

            return ret

    def read_block_left(self):
        return self.read_block('left')
    """
    def read_block_right(self):
        return self.read_block('right')
    """
