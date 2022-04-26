import os
import atexit
from websocket import create_connection
from .utils import serialize, deserialize
import webbrowser


session_id = os.environ.get('SESSION_ID')
ws_host = os.environ.get('WS_HOST', 'ws://localhost:8080')
# ws_host = os.environ.get('WS_HOST', 'wss://hackerforms-broker.abstra.cloud')


def send(data):
    ws.send(serialize(data))


def receive(path: str = ''):
    data = deserialize(ws.recv())

    if data['type'] == 'keep-alive':
        return receive(path)

    if not path:
        return data
    return data.get(path, None)


if session_id == None:
    ws = create_connection(f'{ws_host}/lib')
    session_id = receive('sessionId')
    webbrowser.open(f'http://localhost:8001/local/{session_id}')
else:
    ws = create_connection(f'{ws_host}/lib?sessionId={session_id}')

start = None
while start != 'start':
    start = receive('type')


@atexit.register
def close():
    send({'type': 'program:end'})
    ws.close()
