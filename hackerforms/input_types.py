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

    def __init__(self, key: str, message: str, initialValue: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initialValue = initialValue
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initialValue,
            'placeholder': self.placeholder
        }


class DateInput(Input):
    type = 'date-input'

    def __init__(self, key: str, message: str, initialValue: str = ""):
        super().__init__(key)
        self.message = message
        self.initialValue = initialValue

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initialValue
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

    def __init__(self, key: str, message: str, options: Union[List[str], List[Dict]], multiple: bool = False, initialValue: Union[List[str], List[Dict]] = [{"label": "1", "value": "1"}, {"label": "2", "value": "2"}], placeholder: str = "Choose your option"):
        super().__init__(key)
        self.message = message
        self.options = options
        self.multiple = multiple
        self.placeholder = placeholder
        self.initialValue = initialValue

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'options': self.options,
            'multiple': self.multiple,
            'placeholder': self.placeholder,
            'initialValue': self.initialValue
        }


class DropdownInput(Input):
    type = 'dropdown-input'

    def __init__(self, key: str, name: str, options: Union[List[str], List[Dict]], multiple: bool = False, initialValue: Union[List[str], List[Dict]] = [{"label": "1", "value": "1"}, {"label": "2", "value": "2"}], placeholder: str = "Choose your option"):
        super().__init__(key)
        self.name = name
        self.options = options
        self.multiple = multiple
        self.placeholder = placeholder
        self.initialValue = initialValue

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.name,
            'options': self.options,
            'multiple': self.multiple,
            'placeholder': self.placeholder,
            'initialValue': self.initialValue
        }


class TextareaInput(Input):
    type = 'textarea-input'

    def __init__(self, key: str, message: str, initialValue: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initialValue = initialValue
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initialValue,
            'placeholder': self.placeholder
        }


class NumberInput(Input):
    type = 'number-input'

    def __init__(self, key: str, message: str, initialValue: float = 0, placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initialValue = initialValue
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initialValue,
            'placeholder': self.placeholder
        }


class EmailInput(Input):
    type = 'email-input'

    def __init__(self, key: str, message: str, initialValue: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initialValue = initialValue
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initialValue,
            'placeholder': self.placeholder
        }


class PhoneInput(Input):
    type = 'phone-input'

    def __init__(self, key: str, message: str, initialValue: str = "", placeholder: str = "Your answer here"):
        super().__init__(key)
        self.message = message
        self.initialValue = initialValue
        self.placeholder = placeholder

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initialValue,
            'placeholder': self.placeholder
        }

    def convertAnswer(self, answer):
        return PhoneResponse(raw=answer['raw'], masked=answer['masked'])
