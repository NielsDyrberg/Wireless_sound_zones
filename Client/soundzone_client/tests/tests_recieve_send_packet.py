
from soundzone_protocol import SZPApl
from soundzone_client import SoundZoneClient


def test_receive_data_pack():
    szc = SoundZoneClient()
    szc.manual_add_server("all")
    msg_rcv = szc.receive()

    szp = SZPApl()
    szp.decode(msg_rcv)

    print(szp.payload.payload)


if __name__ == "__main__":
    test_receive_data_pack()