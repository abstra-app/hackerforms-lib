from hackerforms.common import Output
from typing import Any
import json


class PlotlyOutput(Output):
    type = "plotly-output"

    def __init__(self, fig: Any, **kwargs):
        """Display a plotly figure to the user

        Positional Args:
            fig (plotly.Figure): The figure to display to the user

        Keyword Args:
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        self.fig = fig
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "figure": json.loads(self.fig.to_json()),
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
