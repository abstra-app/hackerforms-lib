from hackerforms.common import Output


class TextOutput(Output):
    type = "text-output"

    def __init__(self, text: str, **kwargs):
        """Display a text to the user

        Positional Args:
            text (str): The text to display to the user

        Keyword Args:
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        self.text = str(text)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "text": self.text,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
