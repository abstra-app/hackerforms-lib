from typing import List, Dict
from .apis import upload_file
from .socket import send, receive


def display(msg: str, button_text: str = "Next") -> None:
    return display_group([{
        'message': msg,
        'type': 'text-output',
        'buttonText': button_text
    }])


def display_image(image_str: str, button_text: str = "Next", subtitle: str = "") -> None:
    return display_group([{
        'message': image_str,
        'type': 'image-output',
        'buttonText': button_text,
        "subtitle": subtitle
    }])


def display_link(link_url: str, button_text: str = "Next", link_text: str = "Click here") -> None:
    return display_group([{
        'message': link_url,
        'type': 'link-output',
        'buttonText': button_text,
        "linkText": link_text
    }])


def display_file(file, button_text: str = "Next", download_text: str = "Download here") -> None:
    return display_group([{
        'message': file if isinstance(file, str) else upload_file(file),
        'type': 'file-output',
        'buttonText': button_text,
        "downloadText": download_text
    }])

def display_html(html, button_text: str = "Next", download_text: str = "Download here") -> None:
    return display_group([{
        'message': html,
        'type': 'html-output',
        'buttonText': button_text
    }])

def display_group(fields: List[Dict], button_text: str = "Next"):
    send({
        'type': 'outputs',
        'fields': fields,
        'buttonText': button_text
    })
    receive()
