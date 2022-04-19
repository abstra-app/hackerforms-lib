from typing import List, Union, Dict

from .type_classes import FileResponse
from .socket import send, receive


def read(msg: str, button_text: str = "Next") -> str:
    send({
        'message': msg,
        'type': 'text-input',
        'buttonText': button_text,
    })
    return receive('payload')


def read_date(msg: str, button_text: str = "Next") -> str:
    send({
        'message': msg,
        'type': 'date-input',
        'buttonText': button_text,
    })
    return receive('payload')


def read_file(msg: str, button_text: str = "Next") -> FileResponse:
    send({
        'message': msg,
        'type': 'file-input',
        'buttonText': button_text
    })
    url = receive('payload')
    return FileResponse(url)


def read_multiple_choice(msg: str,
                         options: Union[List[str], List[Dict]],
                         button_text: str = "Next",
                         multiple: bool = False) -> str:
    send({
        'message': msg,
        'type': 'multiple-choice-input',
        'buttonText': button_text,
        'options': options,
        'multiple': multiple
    })
    return receive('payload')


def read_dropdown(name: str, options: Union[List[str], List[Dict]], button_text: str = "Next") -> str:
    send({
        'message': name,
        'type': 'dropdown-input',
        'buttonText': button_text,
        'options': options
    })
    return receive('payload')
