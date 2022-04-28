from abc import abstractmethod, ABC
from typing import List, Union, Dict

from .type_classes import FileResponse, PhoneResponse

class Input(ABC):
    type: str

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key

    @abstractmethod
    def json():
        pass

    def convertAnswer(self, answer):
        return answer
  
class TextInput(Input):
    type = 'text-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }

class DateInput(Input):
    type = 'date-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }

class FileInput(Input):
    type = 'file-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }

    def convertAnswer(self, answer):
        return FileResponse(answer)

class MultipleChoiceInput(Input):
    type = 'multiple-choice-input'
    def __init__(self, key: str, message: str, options: Union[List[str], List[Dict]], multiple: bool = False):
        super().__init__(key)
        self.message = message
        self.options = options
        self.multiple = multiple

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'options': self.options,
            'multiple': self.multiple,
        }

class DropdownInput(Input):
    type = 'dropdown-input'
    def __init__(self, key: str, name: str, options: Union[List[str], List[Dict]], multiple: bool = False):
        super().__init__(key)
        self.name = name
        self.options = options
        self.multiple = multiple

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.name,
            'options': self.options,
            'multiple': self.multiple,
        }

class TextareaInput(Input):
    type = 'textarea-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }

class NumberInput(Input):
    type = 'number-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }

class EmailInput(Input):
    type = 'email-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }


class PhoneInput(Input):
    type = 'phone-input'
    def __init__(self, key: str, message: str):
        super().__init__(key)
        self.message = message

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
        }

    def convertAnswer(self, answer):
        return PhoneResponse(raw=answer['raw'],masked=answer['masked'])