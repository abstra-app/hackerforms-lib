from typing import List, Dict
from .socket import send, receive
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

    def read(self, message: str, initial_value: str = '', placeholder: str = 'Your answer here', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a text input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(
            TextInput(key or message, message, initial_value, placeholder, required, hint=hint))
        return self

    def read_textarea(self, message: str, initial_value: str = '', placeholder: str = 'Your answer here', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a textarea input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(TextareaInput(
            key or message, message, initial_value, placeholder, required, hint=hint))
        return self

    def read_tag(self, message: str, initial_value: List[Union[str, float]] = [""], placeholder: str = 'Your answer here', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a tag input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.fields.append(TagInput(key or message, message,
                                    initial_value, placeholder, required, hint=hint))
        return self

    def read_number(self, message: str, initial_value: float = 0, placeholder: str = 'Your answer here', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a number input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(NumberInput(
            key or message, message, initial_value, placeholder, required, hint=hint))
        return self

    def read_email(self, message: str, initial_value: str = '', placeholder: str = 'Your answer here', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a email input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(EmailInput(
            key or message, message, initial_value, placeholder, required, hint=hint))
        return self

    def read_phone(self, message: str, initial_value: str = '', placeholder: str = '', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a phone input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(PhoneInput(
            key or message, message, initial_value, placeholder, required, hint=hint))
        return self

    def read_date(self, message: str, initial_value: date = None, required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a date input on the page

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(DateInput(key or message, message, initial_value, required, hint=hint))
        return self

    def read_file(self, message: str, initial_value: str = '', required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a file input on the page

        The file will be returned in the form result as a dict with the format { "file": File, "url": str, "content": bytes }

        Args:
            message: The message that will be displayed to the user
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(FileInput(key or message, message, initial_value, required, hint=hint))
        return self

    def read_dropdown(self, name: str, options: Union[List[str], List[Dict]], multiple: bool = False, initial_value = None, placeholder: str = "Choose your option", required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a dropdown input on the page

        Args:
            name: The name of the dropdown
            options: The options of the dropdown, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
            multiple: Whether the user can select multiple options
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(DropdownInput(key or name, name,
                                         options, multiple, initial_value, placeholder, required, hint=hint))
        return self

    def read_multiple_choice(self, message: str, options: Union[List[str], List[Dict]], multiple: bool = False, initial_value = None, required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a multiple choice input on the page

        Args:
            message: The message that will be displayed to the user
            options: The options of the multiple choice, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
            multiple: Whether the user can select multiple options
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(MultipleChoiceInput(
            key or message, message, options, multiple, initial_value, required, hint=hint))
        return self

    def read_cards(self, label, options, multiple=False, initial_value: Union[Union[str, float], List[Union[str, float]]] = None, required: Union[bool, str] = True, key: str = '', hint: str = None):
        '''Add a cards input on the page

        Args:
            label: The text that will be displayed to the user
            options: The options of the multiple choice, eg. [
                        {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'}, 
                        {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]
            multiple: Whether the user can select multiple options
            initial_value: The initial value of the input
            key: The key of the input's value on the form result. Defaults to the label arg
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        self.widgets.append(CardsInput(key or label, label, options, multiple, initial_value, required, hint=hint))
        return self

    def read_list(self, item_schema, initial_value=[{}], key: str = '', hint: str = None):
        '''Add a list input on the page

        Args:
            item_schema: The schema for the items of the list

        Returns:
            The form object
        '''
        self.widgets.append(ListInput(key, item_schema, initial_value=initial_value, hint=hint))
        return self

    def display(self, message: str):
        '''Add a message to the page

        Args:
            message: The message to display to the user

        Returns:
            The form object
        '''
        self.widgets.append(TextOutput(message))
        return self

    def display_markdown(self, text: str):
        '''Add a formatted text to the page

        Args:
            text: The formatted text to display to the user

        Returns:
            The form object
        '''
        self.widgets.append(MarkdownOutput(text))
        return self

    def display_image(self, image_str: str, subtitle: str = ""):
        '''Add an image to the page

        Args:
            image_str: The url or base64 encoding of the image to display to the user
            subtitle: The subtitle of the image

        Returns:
            The form object
        '''
        self.widgets.append(ImageOutput(image_str, subtitle))
        return self

    def display_link(self, link_url: str, link_text: str = "Click here"):
        '''Add a link to the page

        Args:
            link_url: The url of the link
            link_text: The text of the link

        Returns:
            The form object
        '''
        self.widgets.append(LinkOutput(link_url, link_text))
        return self

    def display_file(self, file, download_text: str = "Download here"):
        '''Add a button for the user to download a file to the page

        Args:
            file: The file to download
            download_text: The text of the button

        Returns:
            The form object
        '''
        self.widgets.append(FileOutput(file, download_text))
        return self

    def display_html(self, html: str):
        '''Add an html snippet to the page

        Args:
            html: The html to display to the user

        Returns:
            The form object
        '''
        self.widgets.append(HTMLOutput(html))
        return self

    def display_pandas(self, df):
        '''Add a pandas dataframe to the page

        Args:
            df: The pandas dataframe to display to the user

        Returns:
            The form object
        '''
        self.widgets.append(PandasOutput(df))
        return self

    def display_plotly(self, fig):
        '''Add a plotly figure to the page

        Args:
            fig: The plotly figure to display to the user

        Returns:
            The form object
        '''
        self.widgets.append(PlotlyOutput(fig))
        return self

    def display_iframe(self, url_or_html: str, width: int, height: int):
        '''Add an iframe to the page

        Args:
            url_or_html:  The link to the document or the own document to display
            width: The width of the iframe
            height: The height of the iframe

        Returns:
            The iframe object
        '''
        self.widgets.append(IFrameOutput(url_or_html, width, height))
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

    def run(self, button_text: str = 'Next') -> Dict:
        '''Run the form

        Args:
            button_text: The text of the button that is used to submit the form

        Returns:
            The form result as a dict with the keys being the key of the input and the value being the value of the input
        '''
        send({
            'type': 'form',
            'widgets': self.json(),
            'buttonText': button_text
        })
        form_answers: Dict = receive('payload')

        return self.convert_answer(form_answers)

class ListItemSchema(WidgetSchema):
    '''A schema for a list item

    This schema is used to define the schema of a list item.
    '''

    def __init__(self):
        super().__init__()
