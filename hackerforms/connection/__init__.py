import os, atexit, inspect, typing

from ..exit_hook import hooks, make_debug_data
from ..utils import serialize, deserialize, persist_session_id, open_browser


WS_HOST = os.environ.get("WS_HOST", "wss://hackerforms-broker.abstra.cloud")
FRONTEND_HOST = os.environ.get("FRONTEND_HOST", "https://console.abstracloud.com")


class Connection:
    session_id = None
    debug_enabled = False
    ws = None
    url_params: dict = {}

    def __init__(
        self,
        session_id: typing.Union[str, None] = None,
        debug_enabled: bool = False,
    ) -> None:
        from websocket import create_connection

        self.session_id = session_id
        self.debug_enabled = debug_enabled

        if session_id:
            self.ws = create_connection(f"{WS_HOST}/lib?sessionId={session_id}")
        else:
            self.ws = create_connection(f"{WS_HOST}/lib")
            self.session_id = self.receive("sessionId")
            open_browser(FRONTEND_HOST, self.session_id)
            persist_session_id(self.session_id)

        atexit.register(self.close)

        start = {"type": None}
        while start["type"] != "start":
            start = self.receive()
        self.url_params = start["params"]

    def close(self):
        if self.ws is None or not self.ws.connected:
            return
        self.send(
            {
                "type": "program:end",
                "exitCode": hooks.exit_code,
                "exception": hooks.exception,
            },
            debug_data=hooks.debug_data,
        )
        self.ws.close()

    def send(self, data, debug_data=None):
        if self.debug_enabled:
            debug = debug_data or make_debug_data(inspect.stack())
            self.ws.send(serialize({**data, **debug}))
        else:
            self.ws.send(serialize(data))

    def receive(self, path: str = ""):
        recvd = self.ws.recv()
        if not recvd:
            raise Exception("Websocket not connected")
        data = deserialize(recvd)
        if not path:
            return data
        return data.get(path, None)