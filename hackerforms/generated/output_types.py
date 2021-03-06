###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################
from abc import abstractmethod, ABC
from urllib.parse import quote
import io
import typing
import json
from validators import url

from .file_utils import convert_file


class Output(ABC):
    type: str

    @abstractmethod
    def json(self):
        pass


class TextOutput(Output):
    type = "text-output"

    def __init__(self, message: str, **kwargs):
        """Display a message to the user

        Positional Args:
            message (str): The message to display to the user

        Keyword Args:
            button_text (str): The text to display on the button that will continue the form
        """
        self.message = message
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "message": self.message,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }


class MarkdownOutput(Output):
    type = "markdown-output"

    def __init__(self, text: str, **kwargs):
        """Display a formatted text to the user

        Positional Args:
            text (str): The formatted text to display to the user

        Keyword Args:
            button_text (str): The text to display on the button that will continue the form
        """
        self.text = text
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "text": self.text,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }


class ImageOutput(Output):
    type = "image-output"

    def __init__(self, image: typing.Union[str, io.IOBase], **kwargs):
        """Display an image to the user

        Positional Args:
            image (file-like or str (path, url, base64)): The image to display to the user

        Keyword Args:
            subtitle (str): The subtitle of the image
            button_text (str): The text to display on the button that will continue the form
        """
        self.image = image
        self.subtitle = kwargs.get("subtitle", "")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "image_str": convert_file(self.image),
            "subtitle": self.subtitle,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }


class LinkOutput(Output):
    type = "link-output"

    def __init__(self, link_url: str, **kwargs):
        """Display a link to the user

        Positional Args:
            link_url (str): The url of the link to display to the user

        Keyword Args:
            link_text (str): The text to display on the link
            button_text (str): The text to display on the button that will continue the form
            same_tab (bool): Whether to open the link in the same tab or not
        """
        self.link_url = link_url
        self.link_text = kwargs.get("link_text", "Click here")
        self.same_tab = kwargs.get("same_tab", False)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "message": self.link_text,
            "linkUrl": self.link_url,
            "columns": self.columns,
            "sameTab": self.same_tab,
            "fullWidth": self.full_width,
        }


class FileOutput(Output):
    type = "file-output"

    def __init__(self, file: typing.Union[str, io.IOBase], **kwargs):
        """Display a button for the user to download a file

        Positional Args:
            file (file-like or str (path, url, base64)): The file to download

        Keyword Args:
            download_text (str): The text to display on the button that will download the file
            button_text (str): The text to display on the button that will continue the form
        """
        self.file = file
        self.download_text = kwargs.get("download_text", "Download here")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "message": convert_file(self.file),
            "downloadText": self.download_text,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }


class HTMLOutput(Output):
    type = "html-output"

    def __init__(self, html: str, **kwargs):
        """Display a html snippet to the user

        Positional Args:
            html (str): The html snippet to display to the user

        Keyword Args:
            button_text (str): The text to display on the button that will continue the form
        """
        self.html = html
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "html": self.html,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }


class PandasOutput(Output):
    type = "pandas-output"

    def __init__(self, df: typing.Any, **kwargs):
        """Display a pandas dataframe to the user

        Positional Args:
            df (pandas.DataFrame): The dataframe to display to the user

        Keyword Args:
            button_text (str): The text to display on the button that will continue the form
        """
        self.df = df
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.display_index = kwargs.get("display_index", False)

    def json(self):
        return {
            "type": self.type,
            "table": json.loads(self.df.to_json(orient="table")),
            "columns": self.columns,
            "fullWidth": self.full_width,
            "displayIndex": self.display_index,
        }


class PlotlyOutput(Output):
    type = "plotly-output"

    def __init__(self, fig: typing.Any, **kwargs):
        """Display a plotly figure to the user

        Positional Args:
            fig (plotly.Figure): The figure to display to the user

        Keyword Args:
            button_text (str): The text to display on the button that will continue the form
        """
        self.fig = fig
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "figure": json.loads(self.fig.to_json()),
            "columns": self.columns,
            "fullWidth": self.full_width,
        }


class IFrameOutput(Output):
    type = "iframe-output"

    def __init__(self, url_or_html: str, **kwargs):
        """Display an inline iframe to the user

        Positional Args:
            url_or_html (str): The link to the document or the own document to display to the user

        Keyword Args:
            width (int): The width of the iframe
            height (int): The height of the iframe
            button_text (str): The text to display on the button that will continue the form
        """
        if url(url_or_html):
            self.url = url_or_html
        else:
            self.url = f"data:text/html,{quote(url_or_html)}"

        self.width = kwargs.get("width", 800)
        self.height = kwargs.get("height", 600)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self):
        return {
            "type": self.type,
            "url": self.url,
            "width": self.width,
            "height": self.height,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
