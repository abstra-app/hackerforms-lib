from abc import abstractmethod, ABC
from typing import List, Union, Dict

from .type_classes import FileResponse
from .socket import send, receive

class Form:
    def __init__(self, title: str, button_text: str = 'Next'):
        self.title = title
        self.button_text = button_text
        self.inputs: List[Input] = []

    def read_text(self, message: str):
        self.inputs.append(TextInput(message))
        return self

    def read_textarea(self, message: str):
        self.inputs.append(TextareaInput(message))
        return self
        
    def read_number(self, message: str):
        self.inputs.append(NumberInput(message))
        return self

    def read_email(self, message: str):
        self.inputs.append(EmailInput(message))
        return self

    def read_phone(self, message: str):
        self.inputs.append(PhoneInput(message))
        return self

    def read_date(self, message: str):
        self.inputs.append(DateInput(message))
        return self

    def read_file(self, message: str):
        self.inputs.append(FileInput(message))
        return self

    def read_dropdown(self, name: str, options: Union[List[str], List[Dict]]):
        self.inputs.append(DropdownInput(name, options))
        return self

    def read_multiple_choice(self, message: str,
                            options: Union[List[str], List[Dict]],
                            multiple: bool = False):
        self.inputs.append(MultipleChoiceInput(message, options, multiple))
        return self

    def run(self):
        send({
            'type': 'form-input',
            'fields': [input.json() for input in self.inputs],
            'buttonText': self.button_text
        })
        answers = receive('payload')

        return [input.convertAnswer(answers[index]) for index, input in enumerate(self.inputs)]

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
        self.options = options
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
