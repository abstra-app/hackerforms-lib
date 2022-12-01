from hackerforms.common import Output


class LinkOutput(Output):
    type = "link-output"

    def __init__(self, link_url: str, **kwargs):
        """Display a link to the user

        Positional Args:
            link_url (str): The url of the link to display to the user

        Keyword Args:
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            link_text (str): The text to display on the link. Defaults to "Click here".
            same_tab (bool): Whether to open the link in the same tab or not. Defaults to False.

        """
        self.link_url = link_url
        self.link_text = kwargs.get("link_text", "Click here")
        self.same_tab = kwargs.get("same_tab", False)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "linkText": self.link_text,
            "linkUrl": self.link_url,
            "columns": self.columns,
            "sameTab": self.same_tab,
            "fullWidth": self.full_width,
        }
