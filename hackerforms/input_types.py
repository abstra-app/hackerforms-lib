from abc import abstractmethod, ABC
from typing import List, Union, Dict
from datetime import date

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

    @staticmethod
    def test_instance():
        return TextInput('name', 'What is your name?')

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

    def convertAnswer(self, answer: str):
        '''Convert answer from string to date

        Args:
            answer (str): Date format YYYY-MM-DD
        '''
        split_answer = answer.split('-')
        year = int(split_answer[0])
        month = int(split_answer[1])
        day = int(split_answer[2])
        return date(year, month, day)

    @staticmethod
    def test_instance():
        return DateInput('birthday', 'What is your birthday?')

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

    @staticmethod
    def test_instance():
        return FileInput('file', 'Upload a file')

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
    
    @staticmethod
    def test_instance():
        return MultipleChoiceInput('color', 'What is your favorite color?', ['Red', 'Blue', 'Green'])

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
    
    @staticmethod
    def test_instance():
        return DropdownInput('color', 'What is your favorite color?', ['Red', 'Blue', 'Green'])

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

    @staticmethod
    def test_instance():
        return TextareaInput('description', 'What is your description?')

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
    
    @staticmethod
    def test_instance():
        return NumberInput('age', 'How old are you?')

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

    @staticmethod
    def test_instance():
        return EmailInput('email', 'What is your email?')


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

    @staticmethod
    def test_instance():
        return PhoneInput('phone', 'What is your phone number?')

inputs = [
    TextInput,
    DateInput,
    FileInput,
    MultipleChoiceInput,
    DropdownInput,
    TextareaInput,
    NumberInput,
    EmailInput,
    PhoneInput
]