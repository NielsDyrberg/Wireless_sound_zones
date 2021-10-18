
from modules import MusicReader


def test_read_sound_file():
    mr = MusicReader(file_name="epic_sax_guy.wav", file_format="wav", size=10)

    print(f"sample_rate: {mr.sample_rate}")
    for x in range(0, 10):
        res = mr.read_block_left()
        print(res)


if __name__ == "__main__":
    test_read_sound_file()
