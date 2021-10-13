
from soundzone_protocol import SZPApl
from soundzone_server import SoundZoneServer


def test_send_packet():
    """
    Used to test sending a sound packet to a client
    :return: None
    """
    client_id = 0  # Client id used for testing
    hostname = "client1.local"  # testing locally

    szs = SoundZoneServer()
    szs.manual_add_client(client_id, hostname)

    szp = SZPApl()
    szp.add_command(command="send")
    szp.command.payload = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77]
    szp.command.time.hour = 0x4
    szp.command.time.minute = 0x01
    szp.command.time.second = 0x42
    szp.command.time.mili_second = 0x24
    szp.command.time.micro_second = 0x0324

    encoded_hex = szp.encode()
    szs.clients[client_id].send(szp.encode())


if __name__ == "__main__":
    test_send_packet()
