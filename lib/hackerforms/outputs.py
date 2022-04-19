from .apis import upload_file
from .socket import send, receive


def display(msg: str, button_text: str = "Next") -> None:
    send({
        'message': msg,
        'type': 'text-output',
        'buttonText': button_text
    })
    receive()


def display_image(image_str: str, button_text: str = "Next", subtitle: str = "") -> None:
    send({
        'message': image_str,
        'type': 'image-output',
        'buttonText': button_text,
        "subtitle": subtitle
    })
    receive()


def display_link(link_url: str, button_text: str = "Next", link_text: str = "Click here") -> None:
    send({
        'message': link_url,
        'type': 'link-output',
        'buttonText': button_text,
        "linkText": link_text
    })
    receive()


def display_file(file, button_text: str = "Next", download_text: str = "Download here") -> None:
    send({
        'message': file if isinstance(file, str) else upload_file(file),
        'type': 'file-output',
        'buttonText': button_text,
        "downloadText": download_text
    })
    receive()

def display_html(html, button_text: str = "Next", download_text: str = "Download here") -> None:
    send({
        'message': html,
        'type': 'html-output',
        'buttonText': button_text
    })
    receive()
