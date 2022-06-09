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

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', '')
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint,
            'columns': self.columns,
        }


class TagInput(Input):
    type = 'tag-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', [""])
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint,
            'columns': self.columns,
        }


class DateInput(Input):
    type = 'date-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'message': self.message,
            'initialValue': self.initial_value.isoformat() if self.initial_value else '',
            'required': self.required,
            'columns': self.columns,
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

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'message': self.message,
            "initialValue": self.initial_value,
            'required': self.required,
            'columns': self.columns,
        }

    def convert_answer(self, answer):
        return FileResponse(answer) if answer else None


class ImageInput(Input):
    type = 'image-input'

    def __init__(self, key: str, message: str, initial_value: str = "", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'message': self.message,
            "initialValue": self.initial_value,
            'required': self.required
        }

    def convert_answer(self, answer):
        return FileResponse(answer) if answer else None


class MultipleChoiceInput(Input):
    type = 'multiple-choice-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.options = kwargs.get('options')
        self.multiple = kwargs.get('multiple', False)
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'options': self.options,
            'hint': self.hint,
            'multiple': self.multiple,
            'initialValue': self.initial_value,
            'required': self.required,
            'columns': self.columns,
        }


class CardsInput(Input):
    type = 'cards-input'

    def __init__(self, key: str, **kwargs) -> None:
        super().__init__(key)
        self.label = kwargs.get('label')
        self.options = kwargs.get('options')
        self.multiple = kwargs.get('multiple', False)
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'label': self.label,
            'hint': self.hint,
            'options': self.options,
            'multiple': self.multiple,
            'initialValue': self.initial_value,
            'required': self.required,
            'columns': self.columns,
        }


class DropdownInput(Input):
    type = 'dropdown-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.name = kwargs.get('name')
        self.options = kwargs.get('options')
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', 'Choose an option')
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.name,
            'options': self.options,
            'hint': self.hint,
            'multiple': self.multiple,
            'placeholder': self.placeholder,
            'initialValue': self.initial_value,
            'required': self.required,
            'columns': self.columns,
        }


class TextareaInput(Input):
    type = 'textarea-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint,
            'columns': self.columns,
        }


class NumberInput(Input):
    type = 'number-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', 0)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint,
            'columns': self.columns,
        }


class EmailInput(Input):
    type = 'email-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', 'Your email here')
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint,
            'columns': self.columns,
        }


class PhoneInput(Input):
    type = 'phone-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.message = kwargs.get('message')
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', '')
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint,
            'columns': self.columns,
        }

    def convert_answer(self, answer):
        return PhoneResponse(raw=answer['raw'], masked=answer['masked']) if answer else None


class ListInput(Input):
    type = 'list-input'

    def __init__(self, key: str, **kwargs):
        super().__init__(key)
        self.item_schema = kwargs.get('item_schema')
        self.initial_value = kwargs.get('initial_value', [{}])
        self.min = kwargs.get('min', None)
        self.max = kwargs.get('max', None)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'itemSchema': self.item_schema.json(),
            'initialValue': self.initial_value,
            'columns': self.columns,
            'min': self.min,
            'max': self.max
        }

    def convert_answer(self, answers):
        return [self.item_schema.convert_answer(answer) for answer in answers]
