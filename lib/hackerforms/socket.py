import os
import atexit
from websocket import create_connection
from .utils import serialize, deserialize


session_id = os.environ.get('SESSION_ID')
# host = 'ws://localhost:8080'
host = 'wss://hackerforms-broker.abstra.cloud'

ws = create_connection(
    f'{host}/lib?sessionId={session_id}')

start = ws.recv()
if start != 'start':
    raise Exception('Broker not started')

def send(data):
    ws.send(serialize(data))


def receive(path: str = ''):
    raw_data = ws.recv()

    if raw_data == 'keep-alive':
        return receive(path)

    data = deserialize(raw_data)
    if not path:
        return data
    return data.get(path, None)


@atexit.register
def close():
    ws.close()
