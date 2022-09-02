import builtins
from .generated.inputs import read
from .generated.outputs import display


def overload_input():
    read_overload = lambda msg="": read(msg)
    builtins.input = read_overload
    builtins.raw_input = read_overload


def overload_print():
    builtins.print = display
