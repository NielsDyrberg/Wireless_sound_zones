
import socket


def get_ip_from_name(name):
    """
    Function used to retrieve ip's from _IP dict
    :param name: hostname of the wanted device
    :return: str, whit ip
    """
    try:
        return _IP[name]
    except KeyError:
        print("KeyError")
        return None


_IP = {  # Dictionary containing hostnames and IP's
    "local": '127.0.0.1',
    "all": '0.0.0.0',
    "master": '192.168.1.35',
    "client1": '192.168.1.36'
}

PORT = 1695  # port # for tcp
HEADER_SIZE = 16  # two bytes for header size
ADDRESS_FAMILY = socket.AF_INET
SOCK_TYPE = socket.SOCK_STREAM  # Sock stream is TCP, should be UDP to follow SZP standard.
ENCODING = "utf-8"  # What encoding to use when encoding text
BUFFER_LEN = 8  # Length of rx buffer


class DataTransport:
    """
    Class used to bind the 7th later SZP and the lower transport layer (UDP)

    Attributes
    ----------
    buffer_len: int
        The length of the rx buffer
    _ADDR: str
        IP address where to communicate
    _PORT: int
        On what port to communicate
    _HEADER_SIZE: int
        The length of the header
    _ENCODING: str
        The encoding to use for strings
    _ADDRESS_FAMILY: socket.AddressFamily
        The address family used
    _SOCK_TYPE: socket.SocketKind
        The socket type used
    _s: socket object
        Contains the socket used for transmission
    _sender_socket:
        Socket of the sender
    _port_open: bool
        Keeps track of the status of the port
    _connected: bool
        Keeps track on if the socket is connected

    Methods
    -------
    __init__()
        Initiates the class parameters
    _open_port()
        Opens port to allow incoming connections
    _close()
        Closes #_s socket
    _connect()
        Connects a #_s socket to the specified socket (specified by #_ADDR).
    receive(return_sender_addr)
        Used to receive data sent from another socket.
    send(msg)
        Sends a msg to #_s socket specified by #_ADDR
    """
    def __init__(self, address, port=PORT, header_size=HEADER_SIZE, encoding=ENCODING, addr_family=ADDRESS_FAMILY,
                 socket_type=SOCK_TYPE, buffer_len=BUFFER_LEN):
        """
        Initiates the class parameters
        :param address: IP where to communicate
        :param port: On what port to communicate
        :param header_size: The length of the header
        :param encoding: The encoding to use for strings
        :param addr_family: The address family used
        :param socket_type: The socket type used
        :param buffer_len: The length of the rx buffer
        """
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

    def _open_port(self) -> None:
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
        """
        Closes #_s socket
        :return: None
        """
        self._s.close()

    def _connect(self):
        """
        Connects a #_s socket to the specified socket (specified by #_ADDR).
        :return: None
        """
        # if self._s is None:
        self._s = socket.socket(self._ADDRESS_FAMILY, self._SOCK_TYPE)
        self._s.connect((self._ADDR, self._PORT))
        self._connected = True

    def receive(self, return_sender_addr=False):
        """
        Used to receive data sent from another socket.

        It allows connections specified by #_ADDR
        :param return_sender_addr: determine if address of the sender socket should be returned
        :return: payload (, address)
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
        Sends a msg to #_s socket specified by #_ADDR

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



