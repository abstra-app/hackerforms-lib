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

    def convert_answer(self, answer):
        return answer


class TextInput(Input):
    type = 'text-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder
        }


class DateInput(Input):
    type = 'date-input'

    def __init__(self, key: str, message: str, initial_value: date = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value.isoformat() if self.initial_value else ''
        }

    def convert_answer(self, answer: str):
        '''Convert answer from string to date

        Args:
            answer (str): Date format YYYY-MM-DD
        '''
        if not answer:
            return None

        split_answer = answer.split('-')
        year = int(split_answer[0])
        month = int(split_answer[1])
        day = int(split_answer[2])
        return date(year, month, day)


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

    def convert_answer(self, answer):
        return FileResponse(answer) if answer else None


class MultipleChoiceInput(Input):
    type = 'multiple-choice-input'

    def __init__(self, key: str, message: str, options: Union[List[str], List[Dict]], multiple: bool = False, initial_value: Union[Union[str, float], List[Union[str, float]]] = ""):
        super().__init__(key)
        self.message = message
        self.options = options
        self.multiple = multiple
        self.initial_value = initial_value

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'options': self.options,
            'multiple': self.multiple,
            'initialValue': self.initial_value
        }


class DropdownInput(Input):
    type = 'dropdown-input'

    def __init__(self, key: str, name: str, options: Union[List[str], List[Dict]], multiple: bool = False, initial_value: Union[Union[str, float], List[Union[str, float]]] = "", placeholder: str = "Choose your option"):
        super().__init__(key)
        self.name = name
        self.options = options
        self.multiple = multiple
        self.placeholder = placeholder
        self.initial_value = initial_value

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.name,
            'options': self.options,
            'multiple': self.multiple,
            'placeholder': self.placeholder,
            'initialValue': self.initial_value
        }


class TextareaInput(Input):
    type = 'textarea-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder
        }


class NumberInput(Input):
    type = 'number-input'

    def __init__(self, key: str, message: str, initial_value: float = 0, placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder
        }


class EmailInput(Input):
    type = 'email-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder
        }


class PhoneInput(Input):
    type = 'phone-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = ""):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder
        }

    def convert_answer(self, answer):
        return PhoneResponse(raw=answer['raw'], masked=answer['masked']) if answer else None
