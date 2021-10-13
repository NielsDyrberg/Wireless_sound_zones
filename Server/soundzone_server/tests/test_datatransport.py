

from soundzone_server import DataTransport


def test_data_transport():
    """
    Used to test sending a packet to a client
    :return: None
    """
    hostname = "client1.local"  # depends on your client hostname

    # hostname = "" == '0.0.0.0'
    # hostname = 'localhost' == 127.0.0.1

    dt = DataTransport(hostname)

    encoded_hex = "A1B4"
    dt.send(encoded_hex)


if __name__ == "__main__":
    test_data_transport()
