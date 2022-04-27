from typing import List, Union, Dict
from .form import *

def read(message: str, button_text: str = 'Next'):
    '''Read a text value from the user simple text input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return Form(button_text).read(message).run()

def read_textarea(message: str, button_text: str = 'Next'):
    '''Read a text value from the user with a text area input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return Form(button_text).read_textarea(message).run()

def read_number(message: str, button_text: str = 'Next'):
    '''Read a number value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        int: The value entered by the user
    '''
    return Form(button_text).read_number(message).run()

def read_email(message: str, button_text: str = 'Next'):
    '''Read an email value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return Form(button_text).read_email(message).run()

def read_phone(message: str, button_text: str = 'Next'):
    '''Read a phone number value from the user

    Args:
        message (str): The message to display to the user  
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return Form(button_text).read_phone(message).run()

def read_date(message: str, button_text: str = 'Next'):
    '''Read a date value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value entered by the user
    '''
    return Form(button_text).read_date(message).run()

def read_file(message: str, button_text: str = 'Next'):
    '''Read a file value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        { "file": File, "url": string, "content": bytes }: The file uploaded by the user the user
    '''
    return Form(button_text).read_file(message).run()

def read_dropdown(message: str, options: Union[List[str], List[Dict]], button_text: str = 'Next'):
    '''Read a dropdown value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user
        button_text (str): The text to display on the button that will submit the value

    Returns:
        str: The value selected by the user
    '''
    return Form(button_text).read_dropdown(message, options).run()

def read_multiple_choice(message: str, options: Union[List[str], List[Dict]], multiple: bool = False, button_text: str = 'Next'): 
    '''Read a multiple choice value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value

    Returns:
        list, any: The values/value selected by the user
    '''
    return Form(button_text).read_multiple_choice(message, options, multiple).run()
