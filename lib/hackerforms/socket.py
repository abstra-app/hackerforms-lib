import os
import atexit
from websocket import create_connection

from .utils import serialize, deserialize


session_id = os.environ.get('SESSION_ID')
host = 'ws://localhost:8080'
# host = 'wss://hackerforms-broker.abstra.cloud'

ws = create_connection(
    f'{host}/lib?sessionId={session_id}')


def send(data):
    ws.send(serialize(data))


def receive(path: str = ''):
    data = deserialize(ws.recv())
    if not path:
        return data
    return data.get(path, None)


@atexit.register
def close():
    ws.close()
