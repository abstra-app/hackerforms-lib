from typing import List, Union, Dict
from .type_classes import *
from .page import *

def read(message: str, button_text: str = 'Next') -> str:
    '''Read a text value from the user simple text input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read(message).run(button_text))

def read_textarea(message: str, button_text: str = 'Next') -> str:
    '''Read a text value from the user with a text area input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read_textarea(message).run(button_text))

def read_number(message: str, button_text: str = 'Next') -> int:
    '''Read a number value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        int: The value entered by the user
    '''
    return get_single_value(Page().read_number(message).run(button_text))

def read_email(message: str, button_text: str = 'Next') -> str:
    '''Read an email value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read_email(message).run(button_text))

def read_phone(message: str, button_text: str = 'Next') -> PhoneResponse:
    '''Read a phone number value from the user

    Args:
        message (str): The message to display to the user  
        button_text (str): The text to display on the button that will submit the value

    Returns:
        PhoneResponse: The value entered by the user
    '''
    return get_single_value(Page().read_phone(message).run(button_text))

def read_date(message: str, button_text: str = 'Next') -> str:
    '''Read a date value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return get_single_value(Page().read_date(message).run(button_text))

def read_file(message: str, button_text: str = 'Next') -> FileResponse:
    '''Read a file value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        FileResponse: The file uploaded by the user the user
    '''
    return get_single_value(Page().read_file(message).run(button_text))

def read_dropdown(message: str, options: Union[List[str], List[Dict]], multiple: bool = False, button_text: str = 'Next'):
    '''Read a dropdown value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value selected by the user
    '''
    return get_single_value(Page().read_dropdown(message, options, multiple).run(button_text))

def read_multiple_choice(message: str, options: Union[List[str], List[Dict]], multiple: bool = False, button_text: str = 'Next'): 
    '''Read a multiple choice value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value

    Returns:
        list, any: The values/value selected by the user
    '''
    return get_single_value(Page().read_multiple_choice(message, options, multiple).run(button_text))

def get_single_value(answer: Dict):
    return list(answer.values())[0]