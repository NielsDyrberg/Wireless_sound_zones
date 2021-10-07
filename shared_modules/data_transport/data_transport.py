
import socket


def get_ip_from_name(name):
    try:
        return _IP[name]
    except KeyError:
        print("KeyError")
        return None


_IP = {
    "local": '127.0.0.1',
    "all": '0.0.0.0',
    "master": '192.168.1.35',
    "client1": '192.168.1.36'
}

PORT = 1695  # port # for tcp
HEADER_SIZE = 16  # two bytes for header size
ADDRESS_FAMILY = socket.AF_INET
SOCK_TYPE = socket.SOCK_STREAM
ENCODING = "utf-8"
BUFFER_LEN = 8


class DataTransport:
    def __init__(self, address, port=PORT, header_size=HEADER_SIZE, encoding=ENCODING, addr_family=ADDRESS_FAMILY,
                 socket_type=SOCK_TYPE, buffer_len=BUFFER_LEN):
        self.buffer_len = buffer_len
        self._ADDR = address
        self._PORT = port
        self._HEADER_SIZE = header_size
        self._ENCODING = encoding
        self._ADDRESS_FAMILY = addr_family
        self._SOCK_TYPE = socket_type

        self._s = None
        self._sender_socket = None
        self._port_open = False
        self._connected = False

    def _open_port(self):
        """
        Opens port to allow incoming connections
        :return: None
        """
        try:
            self._s = socket.socket(self._ADDRESS_FAMILY, self._SOCK_TYPE)
        except OSError as msg:
            self._s = None

        if self._s is not None:
            try:
                self._s.bind((self._ADDR, self._PORT))
                self._s.listen(1)
            except OSError as msg:
                self._s.close()
                self._s = None

        if self._s is None:
            raise Exception("Could not open socket")
        else:
            self.port_open = True

    def _close(self):
        self._s.close()

    def _connect(self):
        """
        Connects a socket to another.
        :return: None
        """
        # if self._s is None:
        self._s = socket.socket(self._ADDRESS_FAMILY, self._SOCK_TYPE)
        self._s.connect((self._ADDR, self._PORT))
        self._connected = True

    def receive(self, return_sender_addr=False):
        """
        Prints all received data chunks
        :return: payload
        """
        if not self._port_open:
            self._open_port()

        self._sender_socket, address = self._s.accept()

        payload = bytes()
        new_payload = True
        payload_len = None

        while True:
            tmp_payload = self._sender_socket.recv(self.buffer_len)
            if new_payload:
                try:
                    payload_len = int(tmp_payload[:self._HEADER_SIZE])
                except ValueError:
                    continue
                new_payload = False
                # print(f"Receiving new payload with len: {payload_len}")  # Debug msg

            payload += tmp_payload

            if len(payload) - self._HEADER_SIZE == payload_len:
                # print("Full msg received")  # Debug msg
                payload = payload[self._HEADER_SIZE:]
                payload = payload.decode()
                if return_sender_addr:
                    return payload, address
                else:
                    return payload

    def send(self, msg):
        """
        Sends a msg to pre-connected address
        :param msg: Message to send
        :return: None
        """
        self._connect()

        header = bytes(f"{len(msg):<{self._HEADER_SIZE}}", encoding=self._ENCODING)
        msg = bytes(msg, self._ENCODING)
        msg = header+msg
        # print(msg)  # Debug msg
        self._s.send(msg)

    def send_and_receive(self, msg):
        pass


if __name__ == "__main__":
    pass



