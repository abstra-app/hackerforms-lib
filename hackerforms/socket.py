import atexit
import os
from websocket import create_connection
from .exit_hook import hooks
from .utils import serialize, deserialize, persist_session_id, open_browser
from .parameters import set_params
import os
import inspect

initialized = False


# TODO: create_connection should have retry logic
def initialize():
    global ws, initialized
    initialized = True
    session_id = os.environ.get("SESSION_ID")
    # ws_host = os.environ.get('WS_HOST', 'ws://localhost:8080')
    ws_host = os.environ.get("WS_HOST", "wss://hackerforms-broker.abstra.cloud")

    # frontend_host = os.environ.get('FRONTEND_HOST', 'http://localhost:8001')
    frontend_host = os.environ.get("FRONTEND_HOST", "https://console.abstracloud.com")

    if session_id:
        ws = create_connection(f"{ws_host}/lib?sessionId={session_id}")
    else:
        ws = create_connection(f"{ws_host}/lib")
        session_id = receive("sessionId")
        open_browser(frontend_host, session_id)
        persist_session_id(session_id)

    start = {"type": None}
    while start["type"] != "start":
        start = receive()

    set_params(start["params"])
    return session_id


def representations(locals):
    result = {}
    for key, value in locals.items():
        rep = repr(value)
        if len(rep) > 100:
            result[key] = rep[:40] + " ... " + rep[-40:]
        else:
            result[key] = repr(value)
    return result


def send(data):
    if not initialized:
        return

    if os.environ.get("ABSTRA_DEBUG"):
        debug = {
            "debug": {
                "stack": [
                    {
                        "filename": info.filename,
                        "lineno": info.lineno,
                        "name": info.function,
                        "locals": representations(info.frame.f_locals),
                    }
                    for info in inspect.getouterframes(inspect.currentframe())
                ]
            }
        }
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


@atexit.register
def close():
    if not initialized or ws is None or not ws.connected:
        return
    send(
        {
            "type": "program:end",
            "exitCode": hooks.exit_code,
            "exception": hooks.exception,
        }
    )
    ws.close()
