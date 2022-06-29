from abc import abstractmethod, ABC
from validators import url
from urllib.parse import quote
from typing import Any
import json


from .apis import upload_file


class Output(ABC):
    type: str

    @abstractmethod
    def json(self):
        pass


class TextOutput(Output):
    type = 'text-output'

    def __init__(self, message: str, **kwargs):
        '''Display a message to the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will continue the form
        '''
        self.message = message
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
            'columns': self.column
        }


class MarkdownOutput(Output):
    type = 'markdown-output'

    def __init__(self, text: str, **kwargs):
        '''Display a formatted text to the user

        Positional Arg(s):
            text (str): The formatted text to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will continue the form
        '''
        self.text = text
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'text': self.text,
            'columns': self.column
        }


class ImageOutput(Output):
    type = 'image-output'

    def __init__(self, image_str: str, **kwargs):
        '''Display an image to the user

        Positional Arg(s):
            image_str (str): The url or base64 encoding of the image to display to the user

        Keyword Arg(s):
            subtitle (str): The subtitle of the image
            button_text (str): The text to display on the button that will continue the form
        '''
        self.image_str = image_str
        self.subtitle = kwargs.get('subtitle', '')
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'image_str': self.image_str,
            'subtitle': self.subtitle,
            'columns': self.column
        }


class LinkOutput(Output):
    type = 'link-output'

    def __init__(self, link_url: str, **kwargs):
        '''Display a link to the user

        Positional Arg(s):
            link_url (str): The url of the link to display to the user

        Keyword Arg(s):
            link_text (str): The text to display on the link
            button_text (str): The text to display on the button that will continue the form
            same_tab (bool): Whether to open the link in the same tab or not
        '''
        self.link_url = link_url
        self.link_text = kwargs.get('link_text', 'Click here')
        self.column = kwargs.get('columns', 1)
        self.same_tab = kwargs.get('same_tab', False)

    def json(self):
        return {
            'type': self.type,
            'linkUrl': self.link_url,
            'linkText': self.link_text,
            'columns': self.column,
            'sameTab': self.same_tab,
        }


class FileOutput(Output):
    type = 'file-output'

    def __init__(self, file: Any, **kwargs):
        '''Display a button for the user to download a file

        Positional Arg(s):
            file (File): The file to download

        Keyword Arg(s):
            download_text (str): The text to display on the button that will download the file
            button_text (str): The text to display on the button that will continue the form
        '''
        self.file = file
        self.download_text = kwargs.get('download_text', 'Download here')
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'message': self.file if isinstance(self.file, str) else upload_file(self.file),
            'downloadText': self.download_text,
            'columns': self.column,
            'file': self.file
        }


class HTMLOutput(Output):
    type = 'html-output'

    def __init__(self, html: str, **kwargs):
        '''Display a html snippet to the user

        Positional Arg(s):
            html (str): The html snippet to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will continue the form
        '''
        self.html = html
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'html': self.html,
            'columns': self.column
        }


class PandasOutput(Output):
    type = 'pandas-output'

    def __init__(self, df: Any, **kwargs):
        '''Display a pandas dataframe to the user

        Positional Arg(s):
            df (pandas.DataFrame): The dataframe to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will continue the form
        '''
        self.df = df
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'table': json.loads(self.df.to_json(orient="table")),
            'columns': self.column
        }


class PlotlyOutput(Output):
    type = 'plotly-output'

    def __init__(self, fig: Any, **kwargs):
        '''Display a plotly figure to the user

        Positional Arg(s):
            fig (plotly.Figure): The figure to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will continue the form
        '''
        self.fig = fig
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'figure': json.loads(self.fig.to_json()),
            'columns': self.column
        }


class IFrameOutput(Output):
    type = 'iframe-output'

    def __init__(self, url_or_html: str, **kwargs):
        '''Display an inline iframe to the user

        Positional Arg(s):
            url_or_html (str): The link to the document or the own document to display to the user

        Keyword Arg(s):
            width (int): The width of the iframe
            height (int): The height of the iframe
            button_text (str): The text to display on the button that will continue the form
        '''
        if url(url_or_html):
            self.url = url_or_html
        else:
            self.url = f"data:text/html,{quote(url_or_html)}"

        self.width = kwargs.get('width', 800)
        self.height = kwargs.get('height', 600)
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'url': self.url,
            'width': self.width,
            'height': self.height,
            'columns': self.column
        }
