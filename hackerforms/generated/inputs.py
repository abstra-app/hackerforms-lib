###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################

import typing
import io
from .page import Page


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

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().execute_js(code, **kwargs).run(button_text))


def read_cards(label: str, options: typing.Any, **kwargs):
    """Read cards from the user

    Positional Args:
      label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},{'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

    Keyword Args:
      multiple (bool): Whether the user can select multiple options
      button_text (str): The text to display on the button that will submit the value
      initial_value (list): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          list, any: The options/option selected by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_cards(label, options, **kwargs).run(button_text)
    )


def read_date(message: str, **kwargs):
    """Read a date value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (datetime.date or time.struct_time or str (YYYY-MM-DD)): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          datetime.date: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_date(message, **kwargs).run(button_text))


def read_dropdown(
    message: str,
    options: typing.Union[typing.List[str], typing.List[typing.Dict]],
    **kwargs
):
    """Read a dropdown value from the user

    Positional Args:
      message (str): The message to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

    Keyword Args:
      multiple (bool): Whether the user can select multiple options
      button_text (str): The text to display on the button that will submit the value
      initial_value: The initial value to display to the user
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          str: The value selected by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_dropdown(message, options, **kwargs).run(button_text)
    )


def read_email(message: str, **kwargs):
    """Read an email value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          str: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_email(message, **kwargs).run(button_text))


def read_file(message: str, **kwargs):
    """Read a file value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          FileResponse: The file uploaded by the user the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_file(message, **kwargs).run(button_text))


def read_html_list(label: str, options: typing.Any, **kwargs):
    """Read list of html values from the user

    Positional Args:
      label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'html': '<div class="container"><p>Info 1A</><p>Info 1B</p></div>', 'value': 'info1'},{'html': '<div class="container"><p>Info 2A</><p>Info 2B</p></div>', 'value': 'info2'}]

    Keyword Args:
      css (str): The css related to the html item in options
      multiple (bool): Whether the user can select multiple options
      button_text (str): The text to display on the button that will submit the value
      initial_value (list): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          list, any: The options/option selected by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_html_list(label, options, **kwargs).run(button_text)
    )


def read_image(message: str, **kwargs):
    """Read a image file value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          FileResponse: The image file uploaded by the user the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_image(message, **kwargs).run(button_text))


def read_list(item_schema: typing.Any, **kwargs):
    """Read a list value from the user

    Positional Args:
      item_schema (ListItemSchema): The schema for the items of the list

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value

      Returns:
          list: The values entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_list(item_schema, **kwargs).run(button_text))


def read_multiple_choice(
    message: str,
    options: typing.Union[typing.List[str], typing.List[typing.Dict]],
    **kwargs
):
    """Read a multiple choice value from the user

    Positional Args:
      message (str): The message to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

    Keyword Args:
      multiple (bool): Whether the user can select multiple options
      button_text (str): The text to display on the button that will submit the value
      initial_value: The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          list, any: The values/value selected by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_multiple_choice(message, options, **kwargs).run(button_text)
    )


def read_number(message: str, **kwargs):
    """Read a number value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      message (str): The message to display to the user
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          int: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_number(message, **kwargs).run(button_text))


def read_pandas_row_selection(df: typing.Any, **kwargs):
    """Display a pandas dataframe as a table and allow the user to select rows

    Positional Args:
      df (pandas.DataFrame): The pandas dataframe to be displayed

    Keyword Args:
      required: Whether the input is required or not
      button_text (string): The text to display on the next step button

      Returns:
          The list of selected rows
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_pandas_row_selection(df, **kwargs).run(button_text)
    )


def read_password(message: str, **kwargs):
    """Read a password value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"
      lowercase_required (bool or str): Whether the input must have at least one lowercase character
      uppercase_required (bool or str): Whether the input must have at least one uppercase character
      special_required (bool or str): Whether the input must have at least one special character
      digit_required (bool or str): Whether the input must have at least one digit
      min_length (int): Minimum length of the password
      max_length (int): Maximum length of the password
      size (int): Size of the password
      pattern (str): A regex pattern for the accepted password

      Returns:
          str: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_password(message, **kwargs).run(button_text))


def read_phone(message: str, **kwargs):
    """Read a phone number value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          PhoneResponse: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_phone(message, **kwargs).run(button_text))


def read_tag(message: str, **kwargs):
    """Read a tag value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str or float): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          List[Union[str,float]]: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_tag(message, **kwargs).run(button_text))


def read(message: str, **kwargs):
    """Read a text value from the user simple text input

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          str: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read(message, **kwargs).run(button_text))


def read_textarea(message: str, **kwargs):
    """Read a text value from the user with a text area input

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      placeholder (str): The placeholder text to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          str: The value entered by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_textarea(message, **kwargs).run(button_text))


def read_time(message: str, **kwargs):
    """Read a time value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"
      format (str): Whether the input is in the format 24hs or AM/PM. Default is 24hs.

      Returns:
          str: The value selected by the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_time(message, **kwargs).run(button_text))


def read_video(message: str, **kwargs):
    """Read a video file value from the user

    Positional Args:
      message (str): The message to display to the user

    Keyword Args:
      button_text (str): The text to display on the button that will submit the value
      initial_value (str): The initial value to display to the user
      required (bool or str): Whether the input is required or not eg. "this field is required"

      Returns:
          FileResponse: The video file uploaded by the user the user
    """
    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_video(message, **kwargs).run(button_text))


def get_single_value(answer: typing.Dict):
    return list(answer.values())[0]
