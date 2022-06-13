from abc import abstractmethod, ABC
from .apis import upload_file
from validators import url
from urllib.parse import quote
import json


class Output(ABC):
    type: str

    @abstractmethod
    def json():
        pass


class TextOutput(Output):
    type = 'text-output'

    def __init__(self, message: str, **kwargs):
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
        self.link_url = link_url
        self.link_text = kwargs.get('link_text', 'Click here')
        self.column = kwargs.get('columns', 1)
        self.same_tab = kwargs.get('same_tab', False)

    def json(self):
        return {
            'type': self.type,
            'message': self.link_url,
            'linkText': self.link_text,
            'columns': self.column,
            'sameTab': self.same_tab,
        }


class FileOutput(Output):
    type = 'file-output'

    def __init__(self, file, **kwargs):
        self.file = file
        self.download_text = kwargs.get('download_text', 'Download here')
        self.column = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'message': self.file if isinstance(self.file, str) else upload_file(self.file),
            'downloadText': self.download_text,
            'columns': self.column
        }


class HTMLOutput(Output):
    type = 'html-output'

    def __init__(self, html, **kwargs):
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

    def __init__(self, df, **kwargs):
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

    def __init__(self, fig, **kwargs):
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

    def __init__(self, url_or_html, **kwargs):
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
