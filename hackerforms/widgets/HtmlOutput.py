from hackerforms.common import Output


class HtmlOutput(Output):
    type = "html-output"

    def __init__(self, html: str, **kwargs):
        """Display a html snippet to the user

        Positional Args:
            html (str): The html snippet to display to the user

        Keyword Args:
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        self.html = html
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "html": self.html,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
