import socket

from soundzone_protocol import SoundZoneProtocol


class SoundZoneClient:
    def __init__(self):
        # obj of szp
        self.szp = SoundZoneProtocol()

    def receive(self):
        """
        Configures the client to accept incoming connections, and the recieved the msg.
        :return: None (Maybe msg eventually)
        """
        self.szp.open_port(None)
        self.szp.receive()


if __name__ == "__main__":
    test_obj = SoundZoneClient()
    test_obj.receive()

