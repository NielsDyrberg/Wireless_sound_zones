
from soundzone_protocol import SZPApl
from data_transport import DataTransport, get_ip_from_name


NUMBER_OF_CLIENTS = 8


class SoundZoneServer:
    def __init__(self):
        self.clients = [None] * NUMBER_OF_CLIENTS

    def enroll_client(self):
        receive_client = DataTransport(get_ip_from_name("all"))
        rcv_payload, client_ip = receive_client.receive(return_sender_addr=True)

        szp = SZPApl()
        decoded_payload = szp.decode(rcv_payload)
        # self.clients[decoded_payload.payload["enroll"].id] = DataTransport(client_ip)

    def manual_add_client(self, client_id: int, client_name: str):
        if self.clients[client_id] is None:
            self.clients[client_id] = DataTransport(get_ip_from_name(client_name))
        else:
            raise Exception("Client Id is not empty!")

    def run(self):
        pass


if __name__ == "__main__":
    main_obj = SoundZoneServer()
    main_obj.run()

