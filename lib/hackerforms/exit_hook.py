import sys


class ExitHooks(object):
    def __init__(self):
        self.exit_code = None
        self.exception = None
        self.hook()

    def hook(self):
        self._orig_exit = sys.exit
        self._orig_excepthook = sys.excepthook
        sys.exit = self.exit
        sys.excepthook = self.excepthook

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def excepthook(self, exc_type, exc, *args):
        self.exception = str(exc)
        self._orig_excepthook(exc_type, exc, *args)


hooks = ExitHooks()
