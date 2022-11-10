
###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################

import typing
import io
from .page import Page

def execute_js(code: str, **kwargs):
    '''Execute JavaScript on the page
    Args:
        code: The JS code to be executed
    Keyword Arg:
        context (dict): variables to be passed to the JS code
        button_text (string): The text to display on the next step button
    Returns:
      string: Serialized return value of the executed JavaScript
    '''

    button_text = kwargs.get('button_text', 'Next')
    return get_single_value(Page().execute_js(code, **kwargs).run(button_text))

def read_cards(label: str, options: typing.Any, **kwargs):
  '''Read cards from the user

      Positional Args:
        label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},{'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]
      
      Keyword Args:
        multiple (bool): Whether the user can select multiple options. Defaults to False.
        initial_value (list): The initial value to display to the user. Defaults to None.
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        searchable (bool): Whether to show a search bar. Defaults to False.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            list, any: The options/option selected by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_cards(label, options, **kwargs).run(button_text))

def read_code(label: str, **kwargs):
  '''Read a code snippet from the user with a text highlight

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        language (str): The programming language. Defaults to None.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            str: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_code(label, **kwargs).run(button_text))

def read_currency(label: str, **kwargs):
  '''Read a number value from the user with a currency mask

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to 0.
        required (bool or str): Whether the input is required or not, eg. "this field is required". Defaults to True.
        placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        min (float): The minimum value allowed, eg. "0". Defaults to None.
        max (float): The maximum value allowed, eg. "100". Defaults to None.
        step (float): The value to be incremented or decremented while using the input button. Defaults to None.
        currency (str): The currency to display to the user, eg. "USD", "BRL, "EUR", "GBP". Defaults to "USD".
        
        Returns:
            float: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_currency(label, **kwargs).run(button_text))

def read_date(label: str, **kwargs):
  '''Read a date value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (datetime.date or time.struct_time or str (YYYY-MM-DD)): The initial value to display to the user. Defaults to None.
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            datetime.date: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_date(label, **kwargs).run(button_text))

def read_dropdown(label: str, options: typing.Union[typing.List[str], typing.List[typing.Dict]], **kwargs):
  '''Read a dropdown value from the user

      Positional Args:
        label (str): The label to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
      
      Keyword Args:
        multiple (bool): Whether the user can select multiple options. Defaults to False.
        initial_value: The initial value to display to the user. Defaults to None.
        placeholder (str): The placeholder text to display to the user. Defaults to "Choose an option".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            str: The value selected by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_dropdown(label, options, **kwargs).run(button_text))

def read_email(label: str, **kwargs):
  '''Read an email value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        placeholder (str): The placeholder text to display to the user. Defaults to "Your email here".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            str: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_email(label, **kwargs).run(button_text))

def read_file(label: str, **kwargs):
  '''Read a file value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
        
        Returns:
            FileResponse or FileResponse[]: A dict containing the file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of files in case of multiple flag set as True
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_file(label, **kwargs).run(button_text))

def read_html_list(label: str, options: typing.Any, **kwargs):
  '''Read list of html values from the user

      Positional Args:
        label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'html': '<div class="container">Info 1A</div>', 'value': 'info1'},{'html': '<div class="container">Info 2B</div>', 'value': 'info2'}]
      
      Keyword Args:
        initial_value (list): The initial value to display to the user. Defaults to None.
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        multiple (bool): Whether the user can select multiple options. Defaults to False.
        css (str): The css related to the html item in options. Defaults to None.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            list, any: The options/option selected by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_html_list(label, options, **kwargs).run(button_text))

def read_image(label: str, **kwargs):
  '''Read a image file value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
        
        Returns:
            FileResponse or FileResponse[]: A dict containing the image file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of images in case of multiple flag set as True
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_image(label, **kwargs).run(button_text))

def read_list(item_schema: typing.Any, **kwargs):
  '''Read a list value from the user

      Positional Args:
        item_schema (ListItemSchema): The schema for the items of the list
      
      Keyword Args:
        initial_value (any): The initial value to display to the user. Defaults to [{}].
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        min (float): Min value accepted by the input. Defaults to None.
        max (float): Max value accepted by the input. Defaults to None.
        add_button_text (str): Label to be displayed on the add button. Defaults to "+".
        
        Returns:
            list: The values entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_list(item_schema, **kwargs).run(button_text))

def read_multiple_choice(label: str, options: typing.Union[typing.List[str], typing.List[typing.Dict]], **kwargs):
  '''Read a multiple choice value from the user

      Positional Args:
        label (str): The label to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
      
      Keyword Args:
        multiple (bool): Whether the user can select multiple options. Defaults to False.
        min (number): The minimal amount of options that should be selected. Defaults to None.
        max (number): The maximum amount of options that should be selected. Defaults to None.
        initial_value: The initial value to display to the user. Defaults to None.
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            list or any: The values/value selected by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_multiple_choice(label, options, **kwargs).run(button_text))

def read_nps(label: str, **kwargs):
  '''Gets NPS feedback from user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        min (int): Min value accepted by the input. Defaults to 0.
        max (int): Max value accepted by the input. Defaults to 10.
        min_hint (str): Text to display next to the min value. Defaults to "Not at all likely".
        max_hint (str): Text to display next to the max value. Defaults to "Extremely likely".
        initial_value (str): The initial value to display to the user. Defaults to None.
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            int: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_nps(label, **kwargs).run(button_text))

def read_number(label: str, **kwargs):
  '''Read a number value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to 0.
        placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        min (float): Min value accepted by the input. Defaults to None.
        max (float): Max value accepted by the input. Defaults to None.
        step (float): The value to be incremented or decremented while using the input button. Defaults to None.
        
        Returns:
            float: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_number(label, **kwargs).run(button_text))

def read_pandas_row_selection(df: typing.Any, **kwargs):
  '''Display a pandas dataframe as a table and allow the user to select rows

      Positional Args:
        df (pandas.DataFrame): The pandas dataframe to be displayed
      
      Keyword Args:
        required: Whether the input is required or not. Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            list: The list of selected rows
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_pandas_row_selection(df, **kwargs).run(button_text))

def read_password(label: str, **kwargs):
  '''Read a password value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        placeholder (str): The placeholder text to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        lowercase_required (bool or str): Whether the input must have at least one lowercase character. Defaults to True.
        uppercase_required (bool or str): Whether the input must have at least one uppercase character. Defaults to True.
        special_required (bool or str): Whether the input must have at least one special character. Defaults to True.
        digit_required (bool or str): Whether the input must have at least one digit. Defaults to True.
        min_length (int): Minimum length of the password. Defaults to 8.
        max_length (int): Maximum length of the password. Defaults to None.
        size (int): Size of the password. Defaults to None.
        pattern (str): A regex pattern for the accepted password. Defaults to None.
        autocomplete (str): The autocomplete HTML attribute. Defaults to "current-password".
        
        Returns:
            str: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_password(label, **kwargs).run(button_text))

def read_phone(label: str, **kwargs):
  '''Read a phone number value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str or dict): The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to "".
        placeholder (str): The placeholder text to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            PhoneResponse: A dict containing the value entered by the user ({"raw": str, "masked": str})
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_phone(label, **kwargs).run(button_text))

def read_tag(label: str, **kwargs):
  '''Read a tag value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (list): The initial value to display to the user. Defaults to [].
        placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            list(str) or list(float): The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_tag(label, **kwargs).run(button_text))

def read(label: str, **kwargs):
  '''Read a text value from the user simple text input

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        mask (str): A mask to apply to the input. Defaults to None.
        
        Returns:
            str: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read(label, **kwargs).run(button_text))

def read_textarea(label: str, **kwargs):
  '''Read a text value from the user with a text area input

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            str: The value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_textarea(label, **kwargs).run(button_text))

def read_time(label: str, **kwargs):
  '''Read a time value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        format (str): Whether the input is in the format 24hs or AM/PM. Defaults to "24hs".
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        
        Returns:
            datetime.time: A datetime.time object representing the value entered by the user
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_time(label, **kwargs).run(button_text))

def read_video(label: str, **kwargs):
  '''Read a video file value from the user

      Positional Args:
        label (str): The label to display to the user
      
      Keyword Args:
        initial_value (str): The initial value to display to the user. Defaults to "".
        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
        hint (str): A tooltip displayed to the user. Defaults to None.
        full_width (bool): Whether the input should use full screen width. Defaults to False.
        multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
        
        Returns:
            FileResponse or FileResponse[]: A dict containing the video uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of videos in case of multiple flag set as True
        '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read_video(label, **kwargs).run(button_text))

def get_single_value(answer: typing.Dict):
  return list(answer.values())[0]