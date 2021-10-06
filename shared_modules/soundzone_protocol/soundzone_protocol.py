
"""
This file should gather all shared aspects of the SZP

using SZP version 0.0.2
"""

from .szp_modules import *


_supported_cids = {
    0x01: "send",
    0xA1: "enroll",
    0xB3: "set_sound_format",
    0xF1: "checkConn"
}


def _get_key(val, dict_):
    for key, value in dict_.items():
        if val == value:
            return key


class SZPApl:
    def __init__(self):
        self.cid = None
        self.cid_name = None
        self.payload = None

    def _call_command_encode(self):
        if self.cid_name == "checkConn":
            payload = XF1CheckConn()
        elif self.cid_name == "send":
            payload = X01Send()
        elif self.cid_name == "enroll":
            payload = XA1Enroll()
        elif self.cid_name == "set_sound_format":
            payload = XB3SetSoundFormat()
        else:
            raise Exception(f"Command name not known, got: {self.cid_name}")
        self.payload = payload

    def _call_command_decode(self, buffer):
        if self.cid_name == "checkConn":
            self.payload = XF1CheckConn()
        elif self.cid_name == "send":
            self.payload = X01Send()
        elif self.cid_name == "enroll":
            self.payload = XA1Enroll()
        elif self.cid_name == "set_sound_format":
            self.payload = XB3SetSoundFormat()
        else:
            raise Exception(f"Command name not known, got: {self.cid_name}")
        self.payload.decode(buffer)

    def add_command(self, command_id=None, command_name=None):
        if command_id is not None:
            if command_id not in _supported_cids.keys():
                raise Exception(f"CID not supported, got: {hex(command_id)}")
            self.cid = command_id
            self.cid_name = _supported_cids[command_id]
        elif command_name is not None:
            if command_name not in _supported_cids.values():
                raise Exception(f"Command name not supported, got: {hex(command_name)}")
            self.cid = _get_key(command_name, _supported_cids)
            self.cid_name = command_name

        self._call_command_encode()

    def encode(self):
        encoded_apl = "{:02X}".format(self.cid)
        encoded_apl += self.payload.encode()
        return encoded_apl

    def decode(self, buffer):
        """
        Decodes a buffer Hex string.
        :param buffer: Hex string to decode
        :return: None
        """
        buffer = [int(x+y, 16) for x, y in zip(buffer[0::2], buffer[1::2])]

        self.cid = buffer[0]
        payload = buffer[1:]

        if self.cid not in _supported_cids.keys():
            raise Exception(f"CID not supported, got: {hex(self.cid)}")

        self.cid_name = _supported_cids[self.cid]
        self._call_command_decode(payload)

















