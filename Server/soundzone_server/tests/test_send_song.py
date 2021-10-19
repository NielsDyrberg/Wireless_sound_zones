from soundzone_server import SoundZoneServer
import time


def test_send_song():
    client_id = 0  # Client id used for testing
    hostname = "localhost"  # testing locally

    szs = SoundZoneServer()
    szs.manual_add_client(client_id, hostname)

    szs.play_song(song_name="epic_sax_guy", file_format="wav")


if __name__ == "__main__":
    test_send_song()







