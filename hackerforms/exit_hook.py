from inspect import FrameInfo
import sys
from types import TracebackType
import inspect
import os
import typing


def representations(locals):
    result = {}
    for key, value in list(locals.items()):
        try:
            result[key] = repr(value)
        except:
            pass
    return result


def traceback_to_infos(traceback: TracebackType) -> typing.List[FrameInfo]:
    return inspect.getouterframes(traceback.tb_frame)


def make_debug_data(frames: typing.List[FrameInfo]):
    return {
        "debug": {
            "stack": [
                {
                    "filename": info.filename,
                    "lineno": info.lineno,
                    "name": info.function,
                    "locals": representations(info.frame.f_locals),
                }
                for info in (frames)
            ]
        }
    }


class ExitHooks(object):
    def __init__(self):
        self.exit_code = None
        self.exception = None
        self.debug_data = None
        self.hook()

    def hook(self):
        self._orig_exit = sys.exit
        self._orig_excepthook = sys.excepthook
        sys.exit = self.exit
        sys.excepthook = self.excepthook

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def excepthook(self, exc_type, exc, traceback):
        self.exception = str(exc)
        if os.environ.get("ABSTRA_DEBUG"):
            self.debug_data = make_debug_data(traceback_to_infos(traceback))
        self._orig_excepthook(exc_type, exc, traceback)


hooks = ExitHooks()
