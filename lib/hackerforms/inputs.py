from typing import List, Union, Dict

from .type_classes import FileResponse
from .socket import send, receive


def read(msg: str, button_text: str = "Next") -> str:
    return read_form([{
        'message': msg,
        'type': 'text-input',
        'buttonText': button_text,
    }], button_text)


def read_date(msg: str, button_text: str = "Next") -> str:
    return read_form([{
        'message': msg,
        'type': 'date-input',
        'buttonText': button_text,
    }], button_text)


def read_file(msg: str, button_text: str = "Next") -> FileResponse:
    return read_form([{
        'message': msg,
        'type': 'file-input',
        'buttonText': button_text
    }], button_text)


def read_multiple_choice(msg: str,
                         options: Union[List[str], List[Dict]],
                         button_text: str = "Next",
                         multiple: bool = False) -> str:
    return read_form([{
        'message': msg,
        'type': 'multiple-choice-input',
        'options': options,
        'multiple': multiple
    }], button_text)


def read_dropdown(name: str, options: Union[List[str], List[Dict]], button_text: str = "Next") -> str:
    return read_form([{
        'message': name,
        'type': 'dropdown-input',
        'options': options
    }], button_text)

def read_form(fields: List[Dict], button_text: str = "Next"):
    send({
        'type': 'form-input',
        'fields': fields,
        'buttonText': button_text
    })
    answers = receive('payload')
    
    def convertAnswer(field: Dict, answer: any):
        if field['type'] == 'file-input':
            return FileResponse(answer)
        else:
            return answer
    
    return list(map(convertAnswer, fields, answers))
