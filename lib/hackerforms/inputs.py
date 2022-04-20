from abc import abstractmethod, ABC
from typing import List, Union, Dict

from .type_classes import FileResponse
from .socket import send, receive

class Input(ABC):
    type: str

    @abstractmethod
    def json():
        pass

    def convertAnswer(self, answer):
        return answer
    
class TextInput(Input):
    type = 'text-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }

class DateInput(Input):
    type = 'date-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }

class FileInput(Input):
    type = 'file-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }

    def convertAnswer(self, answer):
        return FileResponse(answer)

class MultipleChoiceInput(Input):
    type = 'multiple-choice-input'
    def __init__(self, message: str, options: Union[List[str], List[Dict]], multiple: bool = False):
        self.message = message
        self.option = options
        self.multiple = multiple

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
            'options': self.options,
            'multiple': self.multiple,
        }

class DropdownInput(Input):
    type = 'dropdown-input'
    def __init__(self, name: str, options: Union[List[str], List[Dict]]):
        self.name = name
        self.options = options

    def json(self):
        return {
            'type': self.type,
            'message': self.name,
            'options': self.options,
        }

class TextareaInput(Input):
    type = 'textarea-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }

class NumberInput(Input):
    type = 'number-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }

class EmailInput(Input):
    type = 'email-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }


class PhoneInput(Input):
    type = 'phone-input'
    def __init__(self, message: str):
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'message': self.message,
        }


def read_text(message: str, button_text: str = "Next") -> Dict:
    return read_form([TextInput(message)], button_text)


def read_date(message: str, button_text: str = "Next") -> Dict:
    return read_form([DateInput(message)], button_text)


def read_file(message: str, button_text: str = "Next") -> Dict:
    return read_form([FileInput(message)], button_text)


def read_multiple_choice(message: str,
                         options: Union[List[str], List[Dict]],
                         multiple: bool = False, 
                         button_text: str = "Next") -> Dict:
    
    return read_form([MultipleChoiceInput(message, options, multiple)], button_text)


def read_dropdown(name: str, options: Union[List[str], List[Dict]], button_text: str = "Next") -> Dict:
    return read_form([DropdownInput(name, options)])

def read_textarea(message: str, button_text: str = "Next") -> str:
    return read_form([TextareaInput(message)], button_text)
    
def read_number(message: str, button_text: str = "Next") -> str:
    return read_form([NumberInput(message)], button_text)

def read_email(message: str, button_text: str = "Next") -> str:
    return read_form([EmailInput(message)], button_text)

def read_phone(message: str, button_text: str = "Next") -> dict:
    return read_form([PhoneInput(message)], button_text)

def read_form(inputs: List[Input], button_text: str = "Next"):
    send({
        'type': 'form-input',
        'fields': [input.json() for input in inputs],
        'buttonText': button_text
    })
    answers = receive('payload')

    if len(inputs) == 1:
        return inputs[0].convertAnswer(answers[0])

    return [input.convertAnswer(answers[index]) for index, input in enumerate(inputs)]
