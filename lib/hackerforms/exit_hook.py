import atexit
import sys

from simple_websocket_server import WebSocket


class ExitHooks(object):
    def __init__(self):
        self.exit_code = None
        self.exception = None
        self.hook()

    def hook(self):
        self._orig_exit = sys.exit
        sys.exit = self.exit
        sys.excepthook = self.exc_handler

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def exc_handler(self, exc_type, exc, *args):
        self.exception = exc


hooks = ExitHooks()


def close(send: function, ws: WebSocket):
    send({
        'type': 'program:end',
        'exitCode': hooks.exit_code,
        'exception': hooks.exception
    })
    ws.close()


def register(send: function, ws: WebSocket):
    atexit.register(close, send=send, ws=ws)
