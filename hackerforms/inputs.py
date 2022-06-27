from typing import List, Union, Dict

from .type_classes import *
from .page import *


def read(message: str, **kwargs) -> str:
    '''Read a text value from the user simple text input

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read(message, **kwargs).run(button_text))


def read_textarea(message: str, **kwargs) -> str:
    '''Read a text value from the user with a text area input

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_textarea(message, **kwargs).run(button_text))


def read_tag(message: str, **kwargs) -> List[Union[str, float]]:
    '''Read a tag value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str or float): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        List[Union[str,float]]: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_tag(message, **kwargs).run(button_text))


def read_number(message: str, **kwargs) -> int:
    '''Read a number value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        int: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_number(message, **kwargs).run(button_text))


def read_email(message: str, **kwargs) -> str:
    '''Read an email value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_email(message, **kwargs).run(button_text))


def read_phone(message: str, **kwargs) -> PhoneResponse:
    '''Read a phone number value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:  
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        PhoneResponse: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_phone(message, **kwargs).run(button_text))


def read_date(message: str, **kwargs) -> str:
    '''Read a date value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        datetime.date: The value entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_date(message, **kwargs).run(button_text))


def read_file(message: str, **kwargs) -> FileResponse:
    '''Read a file value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        FileResponse: The file uploaded by the user the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_file(message, **kwargs).run(button_text))


def read_image(message: str, **kwargs) -> FileResponse:
    '''Read a image file value from the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        FileResponse: The image file uploaded by the user the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_image(message, **kwargs).run(button_text))


def read_dropdown(message: str, options: Union[List[str], List[Dict]], **kwargs) -> Union[str, List[str]]:
    '''Read a dropdown value from the user

    Positional Arg:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

    Keyword Arg:
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value
        initial_value: The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        str: The value selected by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_dropdown(message, options, **kwargs).run(button_text))


def read_multiple_choice(message: str, options: Union[List[str], List[Dict]], **kwargs) -> Union[str, List[str]]:
    '''Read a multiple choice value from the user

    Positional Arg:
        message (str): The message to display to the user
        options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

    Keyword Arg:
        multiple (bool): Whether the user can select multiple options
        button_text (str): The text to display on the button that will submit the value
        initial_value: The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        list, any: The values/value selected by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_multiple_choice(message, options, **kwargs).run(button_text))


def read_list(item_schema, **kwargs) -> List[str]:
    '''Read a list value from the user

    Positional Arg:
        item_schema (ListItemSchema): The schema for the items of the list

    Keyword Arg:
        button_text (str): The text to display on the button that will submit the value

    Returns:
        list: The values entered by the user
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_list(item_schema, **kwargs).run(button_text))


def read_cards(label: str, options: List[Dict], **kwargs):
    '''Display multiple clickable cards to the user

    Positional Arg:
        label (str): The text related to this field
        options (list): The options to display to the user, eg. [
                            {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'}, 
                            {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

    Keyword Arg:
        multiple (bool): Whether the user can select multiple options
        search (bool): Enable a search input
        button_text (str): The text to display on the button that will submit the value
        initial_value (list): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"

    Returns:
        list, any: The options/option selected by the user
    '''

    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().read_cards(label, options, **kwargs).run(button_text))

def execute_js(code: str, **kwargs):
    """Execute JavaScript on the page

    Args:
        code: The JS code to be executed
    Keyword Arg:
        context (dict): variables to be passed to the JS code
        button_text (string): The text to display on the next step button

    Returns:
      string: Serialized return value of the executed JavaScript

    """

    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().execute_js(code, **kwargs).run(button_text))

def select_pandas_rows(df, **kwargs) -> PhoneResponse:
    '''Display a pandas dataframe as a table and allow the user to select rows

    Positional Arg:
        df (pandas.DataFrame): The pandas dataframe to be displayed

    Keyword Arg:
        required: Whether the input is required or not
        button_text (string): The text to display on the next step button

    Returns:
        The list of selected rows
    '''
    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().select_pandas_rows(df, **kwargs).run(button_text))

def get_single_value(answer: Dict):
    return list(answer.values())[0]
