
from soundzone_protocol import SZPApl
from soundzone_server import SoundZoneServer


def test_send_packet():
    client_id = 0  # Client id used for testing
    hostname = "local"  # testing locally

    szs = SoundZoneServer()
    szs.manual_add_client(client_id, hostname)

    szp = SZPApl()
    szp.add_command(command_name="send")
    szp.payload.payload = [0x4255, 0x5136, 0x1234, 0x5678, 0x1111]
    szp.payload.time.minute = 0x01
    szp.payload.time.second = 0x42
    szp.payload.time.mili_second = 0x24
    szp.payload.time.micro_second = 0x0324
    szp.payload.time.nano_second = 0x0244

    szs.clients[client_id].send(szp.encode())


if __name__ == "__main__":
    test_send_packet()