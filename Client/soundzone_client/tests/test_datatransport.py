

from data_transport import DataTransport


def test_data_transport():
    hostname = ''

    dt = DataTransport(hostname)

    rsv_msg = dt.receive()
    print(rsv_msg)


if __name__ == "__main__":
    test_data_transport()
