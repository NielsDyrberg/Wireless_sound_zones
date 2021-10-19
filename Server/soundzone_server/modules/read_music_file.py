
from .utils import get_project_root
from scipy.io import wavfile


class MusicReader:
    """
    A class used to read a music file

    Attributes
    ----------
    _file_format: str
        The file format.
    _max_block_size: int
        The maximum size of song block read.
    _sample_rate: int
        sample_rate to play back song.
    _resolution: int
        The sample resolution, in bytes.
    _head: int
        The position of the reader head.
    _data: ndarray
        The opened wave file.

    Methods
    -------
    get_format():

    read_block():

    read_block_left():

    """
    def __init__(self, file_name: str, file_format: str, size: int):
        """
        Initializes class variables, and loads the song file.
        :param file_name: The name of the file, without file extension.
        :param file_format: The format of the file.
        :param size: The max block size.
        """
        root_path = get_project_root()
        self._file_format = file_format
        self._max_block_size = size
        self._sample_rate = None
        self._data = None
        self._resolution = None
        self._head = None
        if self._file_format == "wav":
            self._sample_rate, self._data = wavfile.read(f"{root_path}/songs/{file_name}.{file_format}")

        if self._data is not None:
            # Get the resolution
            res = self._data.dtype.name
            if res == "int16":
                self._resolution = 2  # resolution is 2 bytes

    def get_format(self) -> tuple:
        """
        Ruturns file format data.
        :return: tuple (sample_rate, resolution)
        """
        return self._sample_rate, self._resolution

    def read_block(self, channel=None) -> list:
        """
        Reads a block of sound.
        :param channel: What channel to read, if None the first channel is read.
        :return: List of sound data in bytes, big endian.
        """
        if self._file_format == "wav":
            if self._head is None:
                self._head = 0
            old_head = self._head
            self._head += self._max_block_size

            if channel is None:
                ret = self._data[old_head:self._head]
            elif channel.lower() == "left":
                ret = self._data[old_head:self._head, 0]
            else:
                raise Exception(f"Channel not supported, got: {channel}")

            ret = [x.to_bytes(2, 'big', signed=True) for x in ret.tolist()]

            if not ret or None:
                ret = None

            return ret

    def read_block_left(self) -> list:
        """
        Reads a block of the left channel, i a stereo song
        :return: List of sound data in bytes, big endian.
        """
        return self.read_block('left')
