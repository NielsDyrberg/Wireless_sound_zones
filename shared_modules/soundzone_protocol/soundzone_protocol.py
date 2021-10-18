
"""
This file should gather all shared aspects of the SZP

using SZP version 0.0.2
"""

from .szp_modules import *


_supported_cids = {  # Commands supported that has been implemented.
    0x01: "send",
    0xA1: "enroll",
    0xB3: "set_sound_format",
    0xF1: "checkConn"
}


def _get_key(val, dict_):
    """
    Used to get the key of a corresponding value, in a dictionary.
    :param val: Value that should match the key.
    :param dict_: The dictionary to search trough.
    :return: The key.
    """
    for key, value in dict_.items():
        if val == value:
            return key


class SZPApl:
    """
    Attributes
    ----------
    cid : int
        The command ID
    cid_name : str
        The command name
    command : obj
        The command object. The type depends on what command is underlying.

    Methods
    -------
    _add_command_to_command()
        Used to assign an command object corresponding the command name.
    add_command()
        Used to add a command to to #command.
    encode()
        Encodes the class into a bytearray.
    decode()
        Decodes a buffer Bytearray following SoundZone Protocol
    """
    def __init__(self):
        """
        Initiates cid, cid_name and payload
        """
        self.cid = None
        self.cid_name = None
        self.command = None

    def _add_command_to_command(self):
        """
        Used to assign a command object corresponding the command name to #command.
        :return: None
        """
        if self.cid_name == "checkConn":
            command = XF1CheckConn()
        elif self.cid_name == "send":
            command = X01Send()
        elif self.cid_name == "enroll":
            command = XA1Enroll()
        elif self.cid_name == "set_sound_format":
            command = XB3SetSoundFormat()
        else:
            raise Exception(f"Command name not known, got: {self.cid_name}")
        self.command = command

    def add_command(self, command: [int, str]):
        """
        Used to add a command to to #command.
        :param command: The cid or cid_name used to find the correct command obj.
        :return: None
        """
        if type(command) is int:
            if command not in _supported_cids.keys():
                raise Exception(f"CID not supported, got: {hex(command)}")
            self.cid = command
            self.cid_name = _supported_cids[command]
        elif type(command) is str:
            if command not in _supported_cids.values():
                raise Exception(f"Command name not supported, got: {hex(command)}")
            self.cid = _get_key(command, _supported_cids)
            self.cid_name = command
        else:
            raise Exception(f"Command has to be of type str or int, got {type(command)}")
        self._add_command_to_command()

    def encode(self):
        """
        Encodes the class into a Bytearray.
        :return: Bytearray, encoded as described in SoundZone Protocol
        """
        encoded_apl = self.cid.to_bytes(1, 'big')
        encoded_apl += self.command.encode()
        return encoded_apl

    def decode(self, buffer):
        """
        Decodes a buffer Bytearray following SoundZone Protocol
        :param buffer: Bytearray to decode
        :return: None
        """
        self.cid = buffer[0]
        payload = buffer[1:]

        if self.cid not in _supported_cids.keys():
            raise Exception(f"CID not supported, got: {hex(self.cid)}")

        self.cid_name = _supported_cids[self.cid]
        self._add_command_to_command()
        self.command.decode(payload)
















