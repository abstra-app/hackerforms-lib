import builtins
from .generated.inputs import read


def overload_input():
    builtins.input = read
    builtins.raw_input = read
