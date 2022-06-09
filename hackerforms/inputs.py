from typing import List, Union, Dict
from .type_classes import *
from .page import *


def read(**kwargs) -> str:
    '''Read a text value from the user simple text input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        str: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read(**kwargs).run(button_text))


def read_textarea(**kwargs) -> str:
    '''Read a text value from the user with a text area input

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        str: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_textarea(**kwargs).run(button_text))


def read_tag(**kwargs) -> List[Union[str, float]]:
    '''Read a tag value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str or float): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        List[Union[str,float]]: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_tag(**kwargs).run(button_text))


def read_number(**kwargs) -> int:
    '''Read a number value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        int: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_number(**kwargs).run(button_text))


def read_email(**kwargs) -> str:
    '''Read an email value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        str: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_email(**kwargs).run(button_text))


def read_phone(**kwargs) -> PhoneResponse:
    '''Read a phone number value from the user

    Args:
        message (str): The message to display to the user  
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        PhoneResponse: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_phone(**kwargs).run(button_text))


def read_date(**kwargs) -> str:
    '''Read a date value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        datetime.date: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_date(**kwargs).run(button_text))


def read_file(**kwargs) -> FileResponse:
    '''Read a file value from the user

    Args:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns (int): The number of columns to use for the input

    Returns:
        FileResponse: The file uploaded by the user the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_file(**kwargs).run(button_text))


def read_dropdown(**kwargs) -> Union[str, List[str]]:
    '''Read a dropdown value from the user

    Args:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value
        initial_value: The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required" 
        columns (int): The number of columns to use for the input

    Returns:
        str: The value selected by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_dropdown(**kwargs).run(button_text))


def read_multiple_choice(**kwargs) -> Union[str, List[str]]:
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
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_multiple_choice(**kwargs).run(button_text))


def read_list(**kwargs) -> List[str]:
    '''Read a list value from the user

    Args:
        item_schema (ListItemSchema): The schema for the items of the list
        button_text (str): The text to display on the button that will submit the value

    Returns:
        list: The values entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_list(**kwargs).run(button_text))


def read_cards(**kwargs):
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

    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_cards(**kwargs).run(button_text))


def get_single_value(answer: Dict):
    return list(answer.values())[0]
