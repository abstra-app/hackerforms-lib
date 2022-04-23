from abc import abstractmethod, ABC
from .apis import upload_file

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
    def __init__(self, html, download_text: str = "Download here"):
        self.html = html
        self.download_text = download_text

    def json(self):
        return {
            'type': self.type,
            'message': self.html,
            'downloadText': self.download_text,
        }