import os
import atexit
from websocket import create_connection
from .utils import serialize, deserialize
import webbrowser


session_id = os.environ.get('SESSION_ID')
# ws_host = os.environ.get('WS_HOST', 'ws://localhost:8080')
ws_host = os.environ.get('WS_HOST', 'wss://hackerforms-broker.abstra.cloud')

ws = create_connection(
    f'{ws_host}/lib?sessionId={session_id}')

if session_id == None:
    session_id = ws.recv()
    webbrowser.open(f'localhost:8001/play?sessionId={session_id}')


start = ws.recv()
while start != 'start':
    start = ws.recv()

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
