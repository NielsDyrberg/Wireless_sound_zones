
from soundzone_protocol import SZPApl
from data_transport import DataTransport
from modules.read_music_file import MusicReader

NUMBER_OF_CLIENTS = 8  # Max number of clients.


class SoundZoneServer:
    """
    A class used to control a SoundZone Server

    Attributes
    ----------
    clients : list of DataTransport
        Used to store objects to communicate with clients.
    n_enrolled_clients: int
        Keeps track of the number of enrolled clients
    _chunk_size: int
        Defines to number of bytes read each time.

    Methods
    -------
    enroll_client():
        Adds a client who requests to be enrolled to list of clients.
    manual_add_client(client_id: int, client_name: str)
        Adds a client from #client_id and #client_name
    """
    def __init__(self):
        """
        Constructs list of clients.

        Initially the elements are all None.
        """
        self.clients = [None] * NUMBER_OF_CLIENTS
        self.n_enrolled_clients = 0
        self._chunk_size = 1023

    def _set_file_format(self, file_format):
        """
        Sets the file format, and sends the parameters to the clients
        :param file_format: Format of file
        :return: None
        """
        resolution = file_format[0]
        sample_size = file_format[1]

    def _filter_block(self, block: list) -> list:
        """
        Filters a chunk of song into n [number of clients] chunks of song
        :param block: The sound block to filter
        :return: client_n X block_size List of the filtered block
        """
        # TODO filter block, instead of just returning a list of the same block
        list_to_return = [None] * NUMBER_OF_CLIENTS
        for client, i in zip(self.clients, range(0, self.clients.__len__())):
            if client is not None:
                list_to_return[i] = block
        return list_to_return

    def _make_send_packet(self, payload):
        """
        Used to create a send packet with payload
        :param payload: The chunk of sound that should be sent
        :return: An object of SZPApl that is filled with payload
        """
        szp = SZPApl()
        szp.add_command(command="send")
        szp.command.payload = payload
        # Todo Remove .time if sync is not needed under one song
        szp.command.time.hour = 0x0
        szp.command.time.minute = 0x0
        szp.command.time.second = 0x0
        szp.command.time.mili_second = 0x0
        szp.command.time.micro_second = 0x0
        return szp

    def enroll_client(self) -> None:
        """
        Adds a client who requests to be enrolled to list of clients.
        :return: None
        """
        # TODO Finish the enroll client method
        receive_client = DataTransport("")
        rcv_payload, client_ip = receive_client.receive(return_sender_addr=True)

        szp = SZPApl()
        decoded_payload = szp.decode(rcv_payload)
        # self.clients[decoded_payload.payload["enroll"].id] = DataTransport(client_ip)

    def manual_add_client(self, client_id: int, client_name: str) -> None:
        """
        Used to add a client manually. This is if the server already knows the client id and name.
        :param client_id: The id of the client.
        :param client_name: hostname of client
        :return: None
        """
        if self.clients[client_id] is None:
            self.clients[client_id] = DataTransport(client_name)
        else:
            raise Exception("Client Id is not empty!")

    def play_song(self, song_name: str, file_format: str):
        """
        Used to play a song
        :param song_name: Name of the song
        :param file_format: The format of the song
        :return: None
        """
        mr = MusicReader(file_name=song_name, file_format=file_format, size=self._chunk_size)

        if mr is None:
            raise Exception("Music reader did not read file!")

        self._set_file_format(mr.get_format())
        # Todo eventually sound should be mono, so _left should not be necessary
        raw_block = mr.read_block_left()
        while raw_block is not None:
            filtered_blocks = self._filter_block(raw_block)

            for client, i in zip(self.clients, range(0, self.clients.__len__())):
                # Send 1 filtered block too each client
                if client is not None:
                    packet_obj = self._make_send_packet(filtered_blocks[i])
                    client.send(packet_obj.encode())
            raw_block = mr.read_block_left()


if __name__ == "__main__":
    pass

