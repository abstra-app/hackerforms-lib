from hackerforms.common import Output


class ProgressOutput(Output):
    type = "progress-output"

    def __init__(self, current: float = 50, total: float = 100, **kwargs):
        """Display a progress bar. This widget is shown on screen until the script shows a new widget

        Positional Args:
            current (float): The progress being made. Defaults to 50.
            total (float): Total progress. Defaults to 100.

        Keyword Args:
            text (str): The text displayed with this progress step. Defaults to "".
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        self.current = current
        self.total = total
        self.text = kwargs.get("text", "")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "current": self.current,
            "total": self.total,
            "text": self.text,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
