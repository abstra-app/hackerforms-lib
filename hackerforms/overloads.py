import builtins
from .generated.inputs import read, display


def overload_input():
    builtins.input = read
    builtins.raw_input = read


def overload_print():
    builtins.print = display
