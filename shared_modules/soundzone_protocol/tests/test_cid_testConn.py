
from soundzone_protocol import SZPApl


def test_cid_check_conn_decode():
    # obj of szp
    szp = SZPApl()
    szp.decode("F101")
    print(szp)


def test_cid_test_conn_encode():
    szp = SZPApl()
    szp.add_command(command_name="checkConn")
    resulst = szp.encode()
    print(resulst)


if __name__ == "__main__":
    test_cid_check_conn_decode()
