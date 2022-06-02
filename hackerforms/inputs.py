from typing import List, Union, Dict
from .type_classes import *
from .page import *


def read(message: str, button_text: str = 'Next', initial_value: str = '', placeholder: str = 'Your answer here', required: Union[bool, str] = True, hint: str = None) -> str:
    '''Read a text value from the user simple text input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read(message, initial_value, placeholder, required, hint=hint).run(button_text))


def read_textarea(message: str, button_text: str = 'Next', initial_value: str = '', placeholder: str = 'Your answer here', required: Union[bool, str] = True, hint: str = None) -> str:
    '''Read a text value from the user with a text area input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read_textarea(message, initial_value, placeholder, required, hint=hint).run(button_text))


def read_tag(message: str, button_text: str = 'Next', initial_value: List[Union[str, float]] = [""], placeholder: str = 'Your answer here', required: Union[bool, str] = True, hint: str = None) -> List[Union[str, float]]:
    '''Read a tag value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str or float): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        List[Union[str,float]]: The value entered by the user
    '''
    return get_single_value(Page().read_tag(message, initial_value, placeholder, required, hint=hint).run(button_text))


def read_number(message: str, button_text: str = 'Next', initial_value: float = 0, placeholder: str = 'Your answer here', required: Union[bool, str] = True, hint: str = None) -> int:
    '''Read a number value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        int: The value entered by the user
    '''
    return get_single_value(Page().read_number(message, initial_value, placeholder, required, hint=hint).run(button_text))


def read_email(message: str, button_text: str = 'Next', initial_value: str = '', placeholder: str = 'Your answer here', required: Union[bool, str] = True, hint: str = None) -> str:
    '''Read an email value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read_email(message, initial_value, placeholder, required, hint=hint).run(button_text))


def read_phone(message: str, button_text: str = 'Next', initial_value: str = '', placeholder: str = '', required: Union[bool, str] = True, hint: str = None) -> PhoneResponse:
    '''Read a phone number value from the user

    Args:
        message (str): The message to display to the user  
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        PhoneResponse: The value entered by the user
    '''
    return get_single_value(Page().read_phone(message, initial_value, placeholder, required, hint=hint).run(button_text))


def read_date(message: str, button_text: str = 'Next', initial_value: date = None, required: Union[bool, str] = True, hint: str = None) -> str:
    '''Read a date value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        datetime.date: The value entered by the user
    '''
    return get_single_value(Page().read_date(message, initial_value, required, hint=hint).run(button_text))


def read_file(message: str, button_text: str = 'Next', initial_value: str = '', required: Union[bool, str] = True, hint: str = None) -> FileResponse:
    '''Read a file value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        FileResponse: The file uploaded by the user the user
    '''
    return get_single_value(Page().read_file(message, initial_value, required, hint=hint).run(button_text))


def read_dropdown(message: str, options: Union[List[str], List[Dict]], multiple: bool = False, button_text: str = 'Next', initial_value = None, placeholder: str = "Choose your option", required: Union[bool, str] = True, hint: str = None) -> Union[str, List[str]]:
    '''Read a dropdown value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value
        initial_value: The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required" 

    Returns:
        str: The value selected by the user
    '''
    return get_single_value(Page().read_dropdown(message, options, multiple, initial_value, placeholder, required, hint=hint).run(button_text))


def read_multiple_choice(message: str, options: Union[List[str], List[Dict]], multiple: bool = False, button_text: str = 'Next', initial_value = None, required: Union[bool, str] = True, hint: str = None):
    '''Read a multiple choice value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value
        initial_value: The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        list, any: The values/value selected by the user
    '''
    return get_single_value(Page().read_multiple_choice(message, options, multiple, initial_value, required, hint=hint).run(button_text))


def read_list(item_schema, button_text: str = 'Next', initial_value=[{}], hint: str = None):
    '''Read a list value from the user

    Args:
        item_schema (ListItemSchema): The schema for the items of the list
        button_text (str): The text to display on the button that will submit the value

    Returns:
        list: The values entered by the user
    '''
    return get_single_value(Page().read_list(item_schema, initial_value=initial_value, hint=hint).run(button_text))


def read_cards(label: str, options: List[Dict], multiple: bool = False, button_text: str = 'Next', initial_value: Union[Union[str, float], List[Union[str, float]]] = None, required: Union[bool, str] = True, hint: str = None):
    '''Display multiple clickable cards to the user

    Args:
        label (str): The text related to this field
        options (list): The options to display to the user, eg. [
                            {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'}, 
                            {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value
        initial_value (list): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        list, any: The options/option selected by the user
    '''

    return get_single_value(Page().read_cards(label, options, multiple, initial_value, required, hint=hint).run(button_text))


def get_single_value(answer: Dict):
    return list(answer.values())[0]
