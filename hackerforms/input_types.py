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

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "Your answer here", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint
        }


class TagInput(Input):
    type = 'tag-input'

    def __init__(self, key: str, message: str, initial_value: List[Union[str, float]] = [""], placeholder: str = "Your answer here", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint
        }


class DateInput(Input):
    type = 'date-input'

    def __init__(self, key: str, message: str, initial_value: date = None, required: Union[bool, str] = True, hint: str = None):
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
            'initialValue': self.initial_value.isoformat() if self.initial_value else '',
            'required': self.required
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

    def __init__(self, key: str, message: str, options: Union[List[str], List[Dict]], multiple: bool = False, initial_value = None, required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.options = options
        self.multiple = multiple
        self.initial_value = initial_value
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'options': self.options,
            'hint': self.hint,
            'multiple': self.multiple,
            'initialValue': self.initial_value,
            'required': self.required
        }


class CardsInput(Input):
    type = 'cards-input'

    def __init__(self, key: str, label: str, options, multiple: bool = False, initial_value: Union[Union[str, float], List[Union[str, float]]] = None, required: Union[bool, str] = True, hint: str = None) -> None:
        super().__init__(key)
        self.label = label
        self.options = options
        self.multiple = multiple
        self.initial_value = initial_value
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'label': self.label,
            'hint': self.hint,
            'options': self.options,
            'multiple': self.multiple,
            'initialValue': self.initial_value,
            'required': self.required
        }


class DropdownInput(Input):
    type = 'dropdown-input'

    def __init__(self, key: str, name: str, options: Union[List[str], List[Dict]], multiple: bool = False, initial_value = None, placeholder: str = "Choose your option", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.name = name
        self.options = options
        self.multiple = multiple
        self.placeholder = placeholder
        self.initial_value = initial_value
        self.required = required
        self.hint = hint

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
            'required': self.required
        }


class TextareaInput(Input):
    type = 'textarea-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "Your answer here", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint
        }


class NumberInput(Input):
    type = 'number-input'

    def __init__(self, key: str, message: str, initial_value: float = 0, placeholder: str = "Your answer here", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint
        }


class EmailInput(Input):
    type = 'email-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "Your answer here", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint
        }


class PhoneInput(Input):
    type = 'phone-input'

    def __init__(self, key: str, message: str, initial_value: str = "", placeholder: str = "", required: Union[bool, str] = True, hint: str = None):
        super().__init__(key)
        self.message = message
        self.initial_value = initial_value
        self.placeholder = placeholder
        self.required = required
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'hint': self.hint
        }

    def convert_answer(self, answer):
        return PhoneResponse(raw=answer['raw'], masked=answer['masked']) if answer else None


class ListInput(Input):
    type = 'list-input'

    def __init__(self, key: str, item_schema, initial_value=[{}], hint: str = None):
        super().__init__(key)
        self.item_schema = item_schema
        self.initial_value = initial_value
        self.hint = hint

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'itemSchema': self.item_schema.json(),
            'initialValue': self.initial_value
        }

    def convert_answer(self, answers):
        return [self.item_schema.convert_answer(answer) for answer in answers]
