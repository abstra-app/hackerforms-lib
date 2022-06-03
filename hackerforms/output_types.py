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
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }

class MarkdownOutput(Output):
    type = 'markdown-output'
    def __init__(self, text: str):
        self.text = text

    def json(self):
        return {
            'type': self.type,
            'text': self.text,
        }
    
class ImageOutput(Output):
    type = 'image-output'
    def __init__(self, image_str: str, subtitle: str = ""):
        self.image_str = image_str
        self.subtitle = subtitle

    def json(self):
        return {
            'type': self.type,
            'image_str': self.image_str,
            'subtitle': self.subtitle,
        }
    
class LinkOutput(Output):
    type = 'link-output'
    def __init__(self, link_url: str, link_text: str = "Click here"):
        self.link_url = link_url
        self.link_text = link_text

    def json(self):
        return {
            'type': self.type,
            'message': self.link_url,
            'linkText': self.link_text,
        }

class FileOutput(Output):
    type = 'file-output'
    def __init__(self, file, download_text: str = "Download here"):
        self.file = file
        self.download_text = download_text

    def json(self):
        return {
            'type': self.type,
            'message': self.file if isinstance(self.file, str) else upload_file(self.file),
            'downloadText': self.download_text,
        }
    
class HTMLOutput(Output):
    type = 'html-output'
    def __init__(self, html):
        self.html = html

    def json(self):
        return {
            'type': self.type,
            'html': self.html
        }
    
class PandasOutput(Output):
    type = 'pandas-output'
    def __init__(self, df):
        self.df = df
    
    def json(self):
        return {
            'type': self.type,
            'table': json.loads(self.df.to_json(orient="table"))
        }

class PlotlyOutput(Output):
    type = 'plotly-output'
    def __init__(self, fig):
        self.fig = fig

    def json(self):
        return {
            'type': self.type,
            'figure': json.loads(self.fig.to_json())
        }
    
class IFrameOutput(Output):
    type = 'iframe-output'
    def __init__(self, url_or_html, width, height):
        if url(url_or_html):
            self.url = url_or_html
        else:
            self.url = f"data:text/html,{quote(url_or_html)}" 
        
        self.width = width
        self.height = height
    
    def json(self):
        return {
            'type': self.type,
            'url': self.url,
            'width': self.width,
            'height': self.height,
        }
