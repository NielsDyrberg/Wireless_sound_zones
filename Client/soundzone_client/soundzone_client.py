
from soundzone_protocol import SZPApl
from data_transport import DataTransport, get_ip_from_name


class SoundZoneClient:
    def __init__(self):
        # obj of szp
        self._server = None

    def manual_add_server(self, name="master"):
        if self._server is None:
            self._server = DataTransport(get_ip_from_name(name))
        else:
            raise Exception("Client Id is not empty!")

    def receive(self):
        if isinstance(self._server, DataTransport):
            return self._server.receive()
        else:
            raise Exception(f"Server is not of type DataTransport, got {type(self._server)}")


if __name__ == "__main__":
    pass
