

from soundzone_server import DataTransport


def test_data_transport():
    """
    Used to test sending a packet to a client
    :return: None
    """
    hostname = "rpi4-niels"  # depends on your client hostname

    # hostname = "" == '0.0.0.0'
    # hostname = 'localhost' == 127.0.0.1

    dt = DataTransport(hostname, addr="192.168.1.15")

    encoded_hex = b'\xA1\xB4'
    dt.send(encoded_hex)


if __name__ == "__main__":
    test_data_transport()
