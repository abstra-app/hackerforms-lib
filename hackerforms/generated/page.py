
###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################

import typing
from typing import Dict
from ..socket import send, receive
from .input_types import *
from .output_types import *

class WidgetSchema:
  def __init__(self):
    self.widgets: List[Union[Input, Output]] = []

  def convert_answer(self, form_answers: Dict) -> Dict:
    '''Convert the answer from the form to the expected format
    Args:
        answer: The answer from the form
    Returns:
        The converted answer
    '''
    answer: Dict = {}
    inputs = list(
        filter(lambda widget: isinstance(widget, Input), self.widgets))
    
    for input in inputs:
        answer[input.key] = input.convert_answer(form_answers[input.key])
    return answer

  def json(self):
    '''Get the json representation of the form
    Returns:
        The json representation of the form
    '''
    return [widget.json() for widget in self.widgets]

  def execute_js(self, code: str, **kwargs):
    '''Execute JavaScript on the page

    Args:
        code: The JS code to be executed
    Keyword Arg:
        context (dict): variables to be passed to the JS code
        key (string): The key of the return value on the form result. Defaults to empty string

    Returns:
        string: Serialized return value of the executed JavaScript
    '''

    key = kwargs.get('key', 'js_result')
    self.widgets.append(ExecuteJs(key, code, **kwargs))
    return self

  
  
  def read_cards(self, label: str, **kwargs):
    '''Read cards from the user

      Positional Arg(s):
        label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},{'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]
      
      Keyword Arg(s):
        multiple (bool): Whether the user can select multiple options
        initial_value (list): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the label arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'label')
    self.widgets.append(CardsInput(key, label, **kwargs))
    return self
  
  def read_date(self, message: str, **kwargs):
    '''Read a date value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(DateInput(key, message, **kwargs))
    return self
  
  def read_dropdown(self, message: str, options: typing.Union[typing.List[str], typing.List[typing.Dict]], **kwargs):
    '''Read a dropdown value from the user

      Positional Arg(s):
        message (str): The message to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
      
      Keyword Arg(s):
        multiple (bool): Whether the user can select multiple options
        initial_value: The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(DropdownInput(key, message, options, **kwargs))
    return self
  
  def read_email(self, message: str, **kwargs):
    '''Read an email value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(EmailInput(key, message, **kwargs))
    return self
  
  def read_file(self, message: str, **kwargs):
    '''Read a file value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(FileInput(key, message, **kwargs))
    return self
  
  def read_image(self, message: str, **kwargs):
    '''Read a image file value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(ImageInput(key, message, **kwargs))
    return self
  
  def read_list(self, item_schema: typing.Any, **kwargs):
    '''Read a list value from the user

      Positional Arg(s):
        item_schema (ListItemSchema): The schema for the items of the list
      
      Keyword Arg(s):
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to empty string
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', '')
    self.widgets.append(ListInput(key, item_schema, **kwargs))
    return self
  
  def read_multiple_choice(self, message: str, options: typing.Union[typing.List[str], typing.List[typing.Dict]], **kwargs):
    '''Read a multiple choice value from the user

      Positional Arg(s):
        message (str): The message to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
      
      Keyword Arg(s):
        multiple (bool): Whether the user can select multiple options
        initial_value: The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(MultipleChoiceInput(key, message, options, **kwargs))
    return self
  
  def read_number(self, message: str, **kwargs):
    '''Read a number value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        message (str): The message to display to the user
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(NumberInput(key, message, **kwargs))
    return self
  
  def read_pandas_row_selection(self, df: typing.Any, **kwargs):
    '''Display a pandas dataframe as a table and allow the user to select rows

      Positional Arg(s):
        df (pandas.DataFrame): The pandas dataframe to be displayed
      
      Keyword Arg(s):
        required: Whether the input is required or not
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to empty string
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', '')
    self.widgets.append(PandasRowSelectionInput(key, df, **kwargs))
    return self
  
  def read_phone(self, message: str, **kwargs):
    '''Read a phone number value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(PhoneInput(key, message, **kwargs))
    return self
  
  def read_tag(self, message: str, **kwargs):
    '''Read a tag value from the user

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str or float): The initial value to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(TagInput(key, message, **kwargs))
    return self
  
  def read(self, message: str, **kwargs):
    '''Read a text value from the user simple text input

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''

    key = kwargs.get('key', 'message')
    self.widgets.append(TextInput(key, message, **kwargs))
    return self
  
  def read_textarea(self, message: str, **kwargs):
    '''Read a text value from the user with a text area input

      Positional Arg(s):
        message (str): The message to display to the user
      
      Keyword Arg(s):
        initial_value (str): The initial value to display to the user
        placeholder (str): The placeholder text to display to the user
        required (bool or str): Whether the input is required or not eg. "this field is required"
        columns: The number of columns of the input
        key: The key of the input's value on the form result. Defaults to the message arg
        

      Returns:
        The form object
    '''
    key = kwargs.get('key', 'message')
    self.widgets.append(TextareaInput(key, message, **kwargs))
    return self

  
  
  def display_file(self, file: typing.Any, **kwargs):
    '''Display a button for the user to download a file
      

      Positional Arg(s):
        file (File): The file to download
        
      
      Keyword Arg(s):
        download_text (str): The text to display on the button that will download the file
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(FileOutput(file, **kwargs))
    return self
  
  def display_html(self, html: str, **kwargs):
    '''Display a html snippet to the user
      

      Positional Arg(s):
        html (str): The html snippet to display to the user
        
      
      Keyword Arg(s):
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(HTMLOutput(html, **kwargs))
    return self
  
  def display_iframe(self, url_or_html: str, **kwargs):
    '''Display an inline iframe to the user
      

      Positional Arg(s):
        url_or_html (str): The link to the document or the own document to display to the user
        
      
      Keyword Arg(s):
        width (int): The width of the iframe
        height (int): The height of the iframe
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(IFrameOutput(url_or_html, **kwargs))
    return self
  
  def display_image(self, image_str: str, **kwargs):
    '''Display an image to the user
      

      Positional Arg(s):
        image_str (str): The url or base64 encoding of the image to display to the user
        
      
      Keyword Arg(s):
        subtitle (str): The subtitle of the image
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(ImageOutput(image_str, **kwargs))
    return self
  
  def display_link(self, link_url: str, **kwargs):
    '''Display a link to the user
      

      Positional Arg(s):
        link_url (str): The url of the link to display to the user
        
      
      Keyword Arg(s):
        link_text (str): The text to display on the link
        same_tab (bool): Whether to open the link in the same tab or not
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(LinkOutput(link_url, **kwargs))
    return self
  
  def display_markdown(self, text: str, **kwargs):
    '''Display a formatted text to the user
      

      Positional Arg(s):
        text (str): The formatted text to display to the user
        
      
      Keyword Arg(s):
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(MarkdownOutput(text, **kwargs))
    return self
  
  def display_pandas(self, df: typing.Any, **kwargs):
    '''Display a pandas dataframe to the user
      

      Positional Arg(s):
        df (pandas.DataFrame): The dataframe to display to the user
        
      
      Keyword Arg(s):
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(PandasOutput(df, **kwargs))
    return self
  
  def display_plotly(self, fig: typing.Any, **kwargs):
    '''Display a plotly figure to the user
      

      Positional Arg(s):
        fig (plotly.Figure): The figure to display to the user
        
      
      Keyword Arg(s):
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(PlotlyOutput(fig, **kwargs))
    return self
  
  def display(self, message: str, **kwargs):
    '''Display a message to the user
      

      Positional Arg(s):
        message (str): The message to display to the user
        
      
      Keyword Arg(s):
        columns: The number of columns of the input
        

      Returns:
        The form object
    '''
    self.widgets.append(TextOutput(message, **kwargs))
    return self

class Page(WidgetSchema):
    '''A form page that can be displayed to the user

    This is a page that can be displayed to the user. It can be used to
    show data as well as collect informations. After configuring the
    inputs and outputs, use the run method to display the form to the
    user and collect the answers.
    '''

    def __init__(self):
        super().__init__()

    def run(self, button_text: str = 'Next', columns: float = 1) -> Dict:
        '''Run the form

        Args:
            button_text: The text of the button that is used to submit the form
            columns: The number of columns of the form

        Returns:
            The form result as a dict with the keys being the key of the input and the value being the value of the input
        '''
        send({
            'type': 'form',
            'widgets': self.json(),
            'buttonText': button_text,
            'columns': columns
        })
        form_answers: Dict = receive('payload')

        return self.convert_answer(form_answers)


class ListItemSchema(WidgetSchema):
    '''A schema for a list item

    This schema is used to define the schema of a list item.
    '''

    def __init__(self):
        super().__init__()

    def convert_answer(self, form_answers: Dict) -> Dict:
        '''Convert the answer from the form to the expected format

        Args:
            answer: The answer from the form

        Returns:
            The converted answer
        '''
        answer: Dict = form_answers
        inputs = list(
            filter(lambda widget: isinstance(widget, Input), self.widgets))

        for input in inputs:
            answer[input.key] = input.convert_answer(form_answers[input.key])
        return answer