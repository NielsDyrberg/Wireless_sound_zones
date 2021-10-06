

from soundzone_protocol import SZPApl


def test_cid_send_decode(buffer):
    # obj of szp
    szp = SZPApl()
    szp.decode(buffer)
    print(szp)
    return szp


def test_cid_send_encode(szp_in=None):
    if szp_in is None:
        szp = SZPApl()
        szp.add_command(command_name="send")
        szp.payload.payload = [0x4255, 0x5136, 0x1234, 0x5678, 0x1111]
        szp.payload.time.minute = 0x01
        szp.payload.time.second = 0x42
        szp.payload.time.mili_second = 0x24
        szp.payload.time.micro_second = 0x0324
        szp.payload.time.nano_second = 0x0244
    else:
        szp = szp_in
    res = szp.encode()
    print(res)
    return res


if __name__ == "__main__":
    string_to_decode = test_cid_send_encode()
    szp_obj = test_cid_send_decode(string_to_decode)
    string_to_decode_v2 = test_cid_send_encode(szp_obj)
