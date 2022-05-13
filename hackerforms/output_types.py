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
    
    @staticmethod
    def example():
        return TextOutput('Hello, world!')

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
    
    @staticmethod
    def example():
        return ImageOutput('https://i.imgur.com/XyqQZ.jpg', 'A cute cat')

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

    @staticmethod
    def example():
        return LinkOutput('https://www.google.com', 'Google')

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
    
    @staticmethod
    def example():
        return FileOutput('https://www.google.com', 'Google')

class HTMLOutput(Output):
    type = 'html-output'
    def __init__(self, html):
        self.html = html

    def json(self):
        return {
            'type': self.type,
            'html': self.html
        }
    
    @staticmethod
    def example():
        return HTMLOutput('<h1>Hello, world!</h1>')

class PandasOutput(Output):
    type = 'pandas-output'
    def __init__(self, df):
        self.df = df
    
    def json(self):
        return {
            'type': self.type,
            'table': json.loads(self.df.to_json(orient="table"))
        }

    @staticmethod
    def example():
        import pandas as pd
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        return PandasOutput(df)

class PlotlyOutput(Output):
    type = 'plotly-output'
    def __init__(self, fig):
        self.fig = fig

    def json(self):
        return {
            'type': self.type,
            'figure': json.loads(self.fig.to_json())
        }
    
    @staticmethod
    def example():
        import plotly.graph_objs as go
        import plotly.express as px
        fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6])
        return PlotlyOutput(fig)

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

    @staticmethod
    def example():
        return IFrameOutput('https://www.google.com', '100%', '100%')

outputs = [
    TextOutput,
    ImageOutput,
    LinkOutput,
    FileOutput,
    HTMLOutput,
    PandasOutput,
    PlotlyOutput,
    IFrameOutput
]