
from soundzone_protocol import SZPApl
from data_transport import DataTransport, get_ip_from_name


NUMBER_OF_CLIENTS = 8  # Max number of clients.


class SoundZoneServer:
    """
    A class used to control a SoundZone Server

    Attributes
    ----------
    clients : list of DataTransport
        Used to store objects to communicate with clients.

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

    def enroll_client(self) -> None:
        """
        Adds a client who requests to be enrolled to list of clients.
        :return: None
        """
        receive_client = DataTransport(get_ip_from_name("all"))
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
            self.clients[client_id] = DataTransport(get_ip_from_name(client_name))
        else:
            raise Exception("Client Id is not empty!")

    def run(self):
        pass


if __name__ == "__main__":
    pass

