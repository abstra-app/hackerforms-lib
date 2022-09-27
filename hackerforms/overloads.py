import os
import sys
import builtins

from .socket import send
from .generated.inputs import read
from .generated.outputs import display_plotly
from .generated.page import Page


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
    def print_overload(*values):
        page = Page()
        for value in values:
            page.display(value)
        return page.run()

    builtins.print = print_overload


def _overload_plotly_show():
    try:
        from plotly.io import renderers
        from plotly.graph_objects import Figure
        from plotly.io._base_renderers import ExternalRenderer

        class FormsRenderer(ExternalRenderer):
            def render(self, fig_dict):
                fig = Figure(data=fig_dict)
                display_plotly(fig)
                return {}

        renderers["hackerforms"] = FormsRenderer()
        renderers.default = "hackerforms"
    except Exception as e:
        pass


def initialize():
    _overload_stdio()
    _overload_input()
    _overload_plotly_show()
    if os.getenv("ENABLE_PRINT_AS_DISPLAY") == "true":
        _overload_print()
