import sys, os
from .debug_utils import CloseDTO, traceback_to_infos


class ExitHooks(object):
    def __init__(self):
        self.exit_code = None
        self.exception = None
        self.frames = None

        self._orig_exit = sys.exit
        self._orig_excepthook = sys.excepthook
        sys.exit = self.exit
        sys.excepthook = self.excepthook

    @property
    def close_dto(self):
        return CloseDTO(
            exit_code=self.exit_code, exception=self.exception, frames=self.frames
        )

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def excepthook(self, exc_type, exc, traceback):
        self.exception = str(exc)
        if os.environ.get("ABSTRA_DEBUG"):
            self.frames = traceback_to_infos(traceback)
        self._orig_excepthook(exc_type, exc, traceback)
