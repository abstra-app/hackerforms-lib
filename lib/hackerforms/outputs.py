from abc import abstractmethod, ABC
from typing import List, Dict
from .apis import upload_file
from .socket import send, receive

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

def display_text(msg: str, button_text: str = "Next") -> None:
    return display([TextOutput(msg)], button_text)

def display_image(image_str: str, subtitle: str = "", button_text: str = "Next") -> None:
    return display([ImageOutput(image_str, subtitle)], button_text)

def display_link(link_url: str, link_text: str = "Click here", button_text: str = "Next") -> None:
    return display([LinkOutput(link_url, link_text)], button_text)

def display_file(file, download_text: str = "Download here", button_text: str = "Next") -> None:
    return display([FileOutput(file, download_text)], button_text)

def display_html(html: str, button_text: str = "Next", download_text: str = "Download here") -> None:
    return display([HTMLOutput(html, download_text)], button_text)

def display(outputs: List[Output], button_text: str = "Next"):
    send({
        'type': 'outputs',
        'fields': [output.json() for output in outputs],
        'buttonText': button_text
    })
    receive()
