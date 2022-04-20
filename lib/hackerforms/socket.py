import os
import atexit
from socket import socket, AF_INET, SOCK_STREAM

from .utils import serialize, deserialize


SOCK_RECV_SIZE = 32 * 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((os.environ.get("BROKER_IP", ""), int(os.environ.get('PORT'))))


def send(data):
    sock.sendall(serialize(data))


def receive(path: str = ''):
    data = deserialize(sock.recv(SOCK_RECV_SIZE))
    if not path:
        return data
    return data.get(path, None)


@atexit.register
def close():
    sock.close()
