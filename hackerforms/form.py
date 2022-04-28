from typing import List, Dict
from .socket import send, receive
from .input_types import *
from .output_types import *


class Form:
    '''A form page that can be displayed to the user

    This is a page that can be displayed to the user. It can be used to
    show data as well as collect informations. After configuring the
    inputs and outputs, use the run method to display the form to the
    user and collect the answers.
    '''
    def __init__(self, button_text: str = 'Next'):
        '''
        Args:
            button_text: The text of the button that is used to submit the form
        '''
        self.button_text = button_text
        self.fields: List[Union[Input, Output]] = []

    def read(self, message: str, key: str = ''):
        '''Add a text input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(TextInput(key or message, message))
        return self

    def read_textarea(self, message: str, key: str = ''):
        '''Add a textarea input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(TextareaInput(key or message, message))
        return self

    def read_number(self, message: str, key: str = ''):
        '''Add a number input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(NumberInput(key or message, message))
        return self

    def read_email(self, message: str, key: str = ''):
        '''Add a email input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(EmailInput(key or message, message))
        return self

    def read_phone(self, message: str, key: str = ''):
        '''Add a phone input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(PhoneInput(key or message, message))
        return self

    def read_date(self, message: str, key: str = ''):
        '''Add a date input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(DateInput(key or message, message))
        return self

    def read_file(self, message: str, key: str = ''):
        '''Add a file input on the page

        The file will be returned in the form result as a dict with the format { "file": File, "url": str, "content": bytes }

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(FileInput(key or message, message))
        return self

    def read_dropdown(self, name: str, options: Union[List[str], List[Dict]], multiple: bool = False, key: str = ''):
        '''Add a dropdown input on the page

        Args:
            name: The name of the dropdown
            options: The options of the dropdown, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
             multiple: Whether the user can select multiple options
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(DropdownInput(key or name, name, options, multiple))
        return self

    def read_multiple_choice(self, message: str, options: Union[List[str], List[Dict]], multiple: bool = False, key: str = ''):
        '''Add a multiple choice input on the page

        Args:
            message: The message that will be displayed to the user
            options: The options of the multiple choice, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
            multiple: Whether the user can select multiple options
            key: The key of the input's value on the form result. Defaults to the message arg
        
        Returns:
            The form object
        '''
        self.fields.append(MultipleChoiceInput(
            key or message, message, options, multiple))
        return self

    def display(self, msg: str):
        '''Add a message to the page

        Args:
            msg: The message to display to the user
        
        Returns:
            The form object
        '''
        self.fields.append(TextOutput(msg))
        return self

    def display_image(self, image_str: str, subtitle: str = ""):
        '''Add an image to the page

        Args:
            image_str: The url or base64 encoding of the image to display to the user
            subtitle: The subtitle of the image
        
        Returns:
            The form object
        '''
        self.fields.append(ImageOutput(image_str, subtitle))
        return self

    def display_link(self, link_url: str, link_text: str = "Click here"):
        '''Add a link to the page

        Args:
            link_url: The url of the link
            link_text: The text of the link
        
        Returns:
            The form object
        '''
        self.fields.append(LinkOutput(link_url, link_text))
        return self

    def display_file(self, file, download_text: str = "Download here"):
        '''Add a button for the user to download a file to the page

        Args:
            file: The file to download
            download_text: The text of the button

        Returns:
            The form object
        '''
        self.fields.append(FileOutput(file, download_text))
        return self

    def display_html(self, html: str):
        '''Add an html snippet to the page

        Args:
            html: The html to display to the user
        
        Returns:
            The form object
        '''
        self.fields.append(HTMLOutput(html))
        return self

    def display_pandas(self, df):
        '''Add a pandas dataframe to the page

        Args:
            df: The pandas dataframe to display to the user
        
        Returns:
            The form object
        '''
        self.fields.append(PandasOutput(df))
        return self

    def display_plotly(self, fig):
        '''Add a plotly figure to the page

        Args:
            fig: The plotly figure to display to the user
        
        Returns:
            The form object
        '''
        self.fields.append(PlotlyOutput(fig))
        return self

    def run(self):
        '''Run the form

        Returns:
            The form result as a dict with the keys being the key of the input and the value being the value of the input
        '''
        send({
            'type': 'form',
            'fields': [field.json() for field in self.fields],
            'buttonText': self.button_text
        })
        form_answers: Dict = receive('payload')
        answer: Dict = {}

        inputs = list(
            filter(lambda field: isinstance(field, Input), self.fields))

        if len(inputs) == 1:
            input = inputs[0]
            return input.convertAnswer(form_answers[input.key])

        for input in inputs:
            answer[input.key] = input.convertAnswer(form_answers[input.key])
        return answer
