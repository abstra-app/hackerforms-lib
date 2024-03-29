import sys, builtins, os

from .socket import send
from .page import Page

try:
    from .generated.inputs import read
    from .generated.outputs import display_plotly
except ImportError:
    pass

print_as_display = os.getenv("ENABLE_PRINT_AS_DISPLAY") == "true"


def writeWraper(type, write, text):
    try:
        write(text)
        send({"type": type, "log": text})
    finally:
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


def _overload_to_widgets():
    _overload_input()
    _overload_plotly_show()
    print_as_display and _overload_print()
