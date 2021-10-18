
from soundzone_protocol import SZPApl
from data_transport import DataTransport


class SoundZoneClient:
    """
    Class used to control a SoundZone Client

    Atributes
    ---------
    _server: DataTransport

    Methods
    -------
    manual_add_server(hostname)
        Used to add a server manually.
    receive()
    """
    def __init__(self):
        # obj of szp
        self._server = None

    def manual_add_server(self, hostname="master.local"):
        """
        Used to add a server manually.

        Here the servers hostname is needed.
        :param hostname: hostname of server
        :return: None
        """
        if self._server is None:
            self._server = DataTransport(hostname)
        else:
            raise Exception("Client Id is not empty!")

    def receive(self):
        """
        Used to receive a Bytearray from the server
        :return: Bytearray
        """
        if isinstance(self._server, DataTransport):
            return self._server.receive()
        else:
            raise Exception(f"Server is not of type DataTransport, got {type(self._server)}")


if __name__ == "__main__":
    pass
