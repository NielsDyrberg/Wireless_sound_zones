
import time
import socket
from soundzone_protocol import SoundZoneProtocol


class SoundZoneServer:
    def __init__(self):
        # obj of szp
        self.szp = SoundZoneProtocol()

    def send(self, msg):
        """
        Makes the server connect to the client and then sends the msg.
        :param msg: Message to send
        :return: None (Maybe eventually a ack)
        """
        self.szp.connect(self.szp.ip['client1'])
        for i in range(1, 5):
            self.szp.send(msg)
            time.sleep(1)

    def send_to(self, msg, address):
        """
        (Future development)
        Sends message to specific address
        :param msg: Message to send
        :param address: Ip address of where to send
        :return: None (Maybe eventually a ack)
        """
        pass


if __name__ == "__main__":
    test_obj = SoundZoneServer()
    test_obj.send("Hello World")
