import sys
from .socket import send

stdout_write = sys.stdout.write
stderr_write = sys.stderr.write


def writeWraper(type, write, text):
    write(text)
    send({"type": type, "log": text})
    return len(text)


def initialize():
    sys.stdout.write = lambda text: writeWraper("stdout", stdout_write, text)
    sys.stderr.write = lambda text: writeWraper("stderr", stderr_write, text)
