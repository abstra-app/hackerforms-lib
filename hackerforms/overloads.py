import os
import sys
import builtins

from .socket import send
from .generated.inputs import read
from .generated.outputs import display


def writeWraper(type, write, text):
    write(text)
    send({"type": type, "log": text})
    return len(text)


def _overload_stdio():
    stdout_write = sys.stdout.write
    stderr_write = sys.stderr.write

    sys.stdout.write = lambda text: writeWraper("stdout", stdout_write, text)
    sys.stderr.write = lambda text: writeWraper("stderr", stderr_write, text)


def _overload_input():
    read_overload = lambda msg="": read(msg)
    builtins.input = read_overload
    builtins.raw_input = read_overload


def _overload_print():
    builtins.print = display


def initialize():
    _overload_stdio()
    _overload_input()
    if os.getenv("ENABLE_PRINT_AS_DISPLAY") == "true":
        _overload_print()
