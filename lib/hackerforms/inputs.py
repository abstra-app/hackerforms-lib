from typing import List, Union, Dict

from .type_classes import FileResponse
from .socket import send, receive


def read_text(msg: str) -> Dict:
    return {
        'message': msg,
        'type': 'text-input',
    }


def read_date(msg: str) -> Dict:
    return {
        'message': msg,
        'type': 'date-input',
    }


def read_file(msg: str) -> Dict:
    return {
        'message': msg,
        'type': 'file-input',
    }


def read_multiple_choice(msg: str,
                         options: Union[List[str], List[Dict]],
                         multiple: bool = False) -> Dict:
    return {
        'message': msg,
        'type': 'multiple-choice-input',
        'options': options,
        'multiple': multiple
    }


def read_dropdown(name: str, options: Union[List[str], List[Dict]]) -> Dict:
    return {
        'message': name,
        'type': 'dropdown-input',
        'options': options
    }

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
