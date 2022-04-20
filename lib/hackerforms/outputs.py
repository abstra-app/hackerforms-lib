from typing import List, Dict
from .apis import upload_file
from .socket import send, receive


def display_text(msg: str) -> None:
    return {
        'message': msg,
        'type': 'text-output',
    }


def display_image(image_str: str, subtitle: str = "") -> None:
    return {
        'message': image_str,
        'type': 'image-output',
        "subtitle": subtitle
    }


def display_link(link_url: str, link_text: str = "Click here") -> None:
    return {
        'message': link_url,
        'type': 'link-output',
        "linkText": link_text
    }


def display_file(file, download_text: str = "Download here") -> None:
    return {
        'message': file if isinstance(file, str) else upload_file(file),
        'type': 'file-output',
        "downloadText": download_text
    }

def display_html(html, download_text: str = "Download here") -> None:
    return {
        'message': html,
        'type': 'html-output',
    }

def display(fields: List[Dict], button_text: str = "Next"):
    send({
        'type': 'outputs',
        'fields': fields,
        'buttonText': button_text
    })
    receive()
