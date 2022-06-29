from abc import abstractmethod, ABC
from typing import List, Union, Dict, Optional, Any
from datetime import date
import datetime
import json

from .response_types import FileResponse, PhoneResponse

class Input(ABC):
    type: str

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def convert_answer(self, answer):
        pass

class TextInput(Input):
    type = 'text-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a text value from the user simple text input

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            placeholder (str): The placeholder text to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"

        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', '')
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

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
            'fullWidth': self.full_width
        }

    def convert_answer(self, answer: str) -> str:
        '''
        Returns:
            str: The value entered by the user
        '''
        return answer



class ExecuteJs(Input):
    type = 'execute-js'

    def __init__(self, key: str, code: str, **kwargs):
        super().__init__(key)
        self.key = key
        self.code = code
        self.context = kwargs.get('context', {})

    def json(self):
        return {
            'type': self.type,
            'code': self.code,
            'context': self.context,
            'key': self.key,
        }

    def convert_answer(self, answer: str) -> str:
        '''
        Returns:
            string: Serialized return value of the executed JavaScript
        '''
        return answer



class TagInput(Input):

    type = 'tag-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a tag value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str or float): The initial value to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', [])
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

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
            'fullWidth': self.full_width
        }

    def convert_answer(self, answer: List[Union[str,float]]) -> List[Union[str,float]]:
        '''
        Returns:
            List[Union[str,float]]: The value entered by the user
        '''
        
        return answer



class DateInput(Input):
    type = 'date-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a date value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"

        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'message': self.message,
            'initialValue': self.initial_value.isoformat() if self.initial_value else '',
            'required': self.required,
            'columns': self.columns,
            'fullWidth': self.full_width
        }

    def convert_answer(self, answer: str) -> Optional[datetime.date]:
        '''
        Returns:
            datetime.date: The value entered by the user
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

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a file value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"

        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.multiple = kwargs.get('multiple', False)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'message': self.message,
            "initialValue": self.initial_value,
            'required': self.required,
            'columns': self.columns,
            'multiple': self.multiple,
            'fullWidth': self.full_width
        }

    def convert_answer(self, answer) -> Optional[FileResponse]:
        '''
        Returns:
            FileResponse: The file uploaded by the user the user
        '''
        if not answer:
            return None

        if not self.multiple:
            return FileResponse(answer)

        return [FileResponse(item) for item in answer]


class ImageInput(Input):
    type = 'image-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a image file value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.multiple = kwargs.get('multiple', False)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'message': self.message,
            "initialValue": self.initial_value,
            'columns': self.columns,
            'required': self.required,
            'multiple': self.multiple,
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer) -> Optional[FileResponse]:
        '''
        Returns:
            FileResponse: The image file uploaded by the user the user
        '''
        if not answer:
            return None

        if not self.multiple:
            return FileResponse(answer)

        return [FileResponse(item) for item in answer]


class MultipleChoiceInput(Input):
    type = 'multiple-choice-input'

    def __init__(self, key: str, message: str, options: Union[List[str], List[Dict]], **kwargs):
        '''Read a multiple choice value from the user

        Positional Arg(s):
            message (str): The message to display to the user
            options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Arg(s):
            multiple (bool): Whether the user can select multiple options
            button_text (str): The text to display on the button that will submit the value
            initial_value: The initial value to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.options = options
        self.multiple = kwargs.get('multiple', False)
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

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
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer: Union[List, Any]) -> Union[List, Any]:
        '''
        Returns:
            list, any: The values/value selected by the user
        '''
        return answer



class CardsInput(Input):
    type = 'cards-input'

    def __init__(self, key: str, label: str, options, **kwargs):
        '''Read cards from the user

        Positional Arg(s):
            label (str): The text related to this field
            options (list): The options to display to the user, eg. [
                                {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'}, 
                                {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

        Keyword Arg(s):
            multiple (bool): Whether the user can select multiple options
            button_text (str): The text to display on the button that will submit the value
            initial_value (list): The initial value to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.label = label
        self.options = options
        self.multiple = kwargs.get('multiple', False)
        self.searchable = kwargs.get('searchable', False)
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'label': self.label,
            'hint': self.hint,
            'options': self.options,
            'multiple': self.multiple,
            'searchable': self.searchable,
            'initialValue': self.initial_value,
            'required': self.required,
            'columns': self.columns,
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer: Union[List, Any]) -> Union[List, Any]:
        '''
        Returns:
            list, any: The options/option selected by the user
        '''
        return answer



class DropdownInput(Input):
    type = 'dropdown-input'

    def __init__(self, key: str, message: str, options: Union[List[str], List[Dict]], **kwargs):
        '''Read a dropdown value from the user

        Positional Arg(s):
            message (str): The message to display to the user
            options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Arg(s):
            multiple (bool): Whether the user can select multiple options
            button_text (str): The text to display on the button that will submit the value
            initial_value: The initial value to display to the user
            placeholder (str): The placeholder text to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.options = options
        self.initial_value = kwargs.get('initial_value', None)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.multiple = kwargs.get('multiple', False)
        self.placeholder = kwargs.get('placeholder', 'Choose an option')
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'options': self.options,
            'hint': self.hint,
            'multiple': self.multiple,
            'placeholder': self.placeholder,
            'initialValue': self.initial_value,
            'required': self.required,
            'columns': self.columns,
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer: str) -> str:
        '''
        Returns:
            str: The value selected by the user
        '''
        return answer



class TextareaInput(Input):
    type = 'textarea-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a text value from the user with a text area input

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            placeholder (str): The placeholder text to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"

        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.columns = kwargs.get('columns', 1)
        self.hint = kwargs.get('hint', None)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'message': self.message,
            'initialValue': self.initial_value,
            'placeholder': self.placeholder,
            'required': self.required,
            'columns': self.columns,
            'hint': self.hint,
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer: str) -> str:
        '''
        Returns:
            str: The value entered by the user
        '''
        return answer



class NumberInput(Input):
    type = 'number-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a number value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            message (str): The message to display to the user
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            placeholder (str): The placeholder text to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', 0)
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', 'Your answer here')
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

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
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer: int) -> int:
        '''
        Returns:
            int: The value entered by the user
        '''
        return answer



class EmailInput(Input):
    type = 'email-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read an email value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            placeholder (str): The placeholder text to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', 'Your email here')
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

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
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer: str) -> str:
        '''
        Returns:
            str: The value entered by the user
        '''
        return answer



class PhoneInput(Input):
    type = 'phone-input'

    def __init__(self, key: str, message: str, **kwargs):
        '''Read a phone number value from the user

        Positional Arg(s):
            message (str): The message to display to the user

        Keyword Arg(s):  
            button_text (str): The text to display on the button that will submit the value
            initial_value (str): The initial value to display to the user
            placeholder (str): The placeholder text to display to the user
            required (bool or str): Whether the input is required or not eg. "this field is required"
        '''
        super().__init__(key)
        self.message = message
        self.initial_value = kwargs.get('initial_value', '')
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.placeholder = kwargs.get('placeholder', '')
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

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
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer) -> Optional[PhoneResponse]:
        '''
        Returns:
            PhoneResponse: The value entered by the user
        '''
        return PhoneResponse(raw=answer['raw'], masked=answer['masked']) if answer else None


class ListInput(Input):
    type = 'list-input'

    def __init__(self, key: str, item_schema: Any, **kwargs):
        '''Read a list value from the user

        Positional Arg(s):
            item_schema (ListItemSchema): The schema for the items of the list

        Keyword Arg(s):
            button_text (str): The text to display on the button that will submit the value
        '''
        super().__init__(key)
        self.item_schema = item_schema
        self.initial_value = kwargs.get('initial_value', [{}])
        self.min = kwargs.get('min', None)
        self.max = kwargs.get('max', None)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.add_button_text = kwargs.get('add_button_text', '+')
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'itemSchema': self.item_schema.json(),
            'initialValue': self.initial_value,
            'columns': self.columns,
            'min': self.min,
            'max': self.max,
            'addButtonText': self.add_button_text,
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answers) -> List:
        '''
        Returns:
            list: The values entered by the user
        '''
        return [self.item_schema.convert_answer(answer) for answer in answers]

class PandasRowSelectionInput(Input):

    type = 'pandas-row-selection-input'

    def __init__(self, key: str, df: Any, **kwargs):
        """Display a pandas dataframe as a table and allow the user to select rows

            Positional Arg(s):
                df (pandas.DataFrame): The pandas dataframe to be displayed

            Keyword Arg(s):
                required: Whether the input is required or not
                button_text (string): The text to display on the next step button
            
        """
        super().__init__(key)
        self.df = df
        self.required = kwargs.get('required', True)
        self.hint = kwargs.get('hint', None)
        self.columns = kwargs.get('columns', 1)
        self.full_width = kwargs.get('full_width', False)

    def json(self):
        return {
            'type': self.type,
            'key': self.key,
            'hint': self.hint,
            'table': json.loads(self.df.to_json(orient="table")),
            'required': self.required,
            'columns': self.columns,
            'fullWidth': self.full_width,
        }

    def convert_answer(self, answer) -> List:
        '''
        Returns:
            The list of selected rows
        '''
        return answer