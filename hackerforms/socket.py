import os
import atexit
import inspect

from .parameters import set_params
from .exit_hook import hooks, make_debug_data
from .utils import serialize, deserialize, persist_session_id, open_browser


WS_HOST = os.environ.get("WS_HOST", "wss://hackerforms-broker.abstra.cloud")
FRONTEND_HOST = os.environ.get("FRONTEND_HOST", "https://console.abstracloud.com")


ws = None
initialized = False


def initialize():
    from websocket import create_connection

    global ws, initialized
    initialized = True
    session_id = os.environ.get("SESSION_ID")

    if session_id:
        ws = create_connection(f"{WS_HOST}/lib?sessionId={session_id}")
    else:
        ws = create_connection(f"{WS_HOST}/lib")
        session_id = receive("sessionId")
        open_browser(FRONTEND_HOST, session_id)
        persist_session_id(session_id)

    atexit.register(close)

    start = {"type": None}
    while start["type"] != "start":
        start = receive()
    set_params(start["params"])
    return session_id


def send(data, debug_data=None):
    if not initialized:
        return
    if os.environ.get("ABSTRA_DEBUG"):
        debug = debug_data or make_debug_data(inspect.stack())
        ws.send(serialize({**data, **debug}))
    else:
        ws.send(serialize(data))


def receive(path: str = ""):
    if not initialized:
        return
    recvd = ws.recv()
    if not recvd:
        raise Exception("Websocket not connected")
    data = deserialize(recvd)
    if not path:
        return data
    return data.get(path, None)


def close():
    if not initialized or ws is None or not ws.connected:
        return
    send(
        {
            "type": "program:end",
            "exitCode": hooks.exit_code,
            "exception": hooks.exception,
        },
        debug_data=hooks.debug_data,
    )
    ws.close()
