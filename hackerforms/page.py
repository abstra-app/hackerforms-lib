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

    def read(self, message: str, **kwargs):
        '''Add a text input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(
            TextInput(key, message, **kwargs))
        return self

    def read_textarea(self, message: str, **kwargs):
        '''Add a textarea input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(TextareaInput(key, message, **kwargs))
        return self

    def read_tag(self, message: str, **kwargs):
        '''Add a tag input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placehlder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input
            hint: The hint of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(TagInput(key, message, **kwargs))
        return self

    def read_number(self, message: str, **kwargs):
        '''Add a number input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(NumberInput(key, message, **kwargs))
        return self

    def read_email(self, message: str, **kwargs):
        '''Add a email input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(EmailInput(key, message, **kwargs))
        return self

    def read_phone(self, message: str, **kwargs):
        '''Add a phone input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(PhoneInput(
            key, message, **kwargs))
        return self

    def read_date(self, message: str, **kwargs):
        '''Add a date input on the page

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(
            DateInput(key, message, **kwargs))
        return self

    def read_file(self, message: str, **kwargs):
        '''Add a file input on the page

        The file will be returned in the form result as a dict with the format { "file": File, "url": str, "content": bytes }

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(
            FileInput(key, message, **kwargs))
        return self

    def read_image(self, message: str, **kwargs):
        '''Add a image file input on the page

        The file will be returned in the form result as a dict with the format { "file": File, "url": str, "content": bytes }

        Positional Arg:
            message: The message that will be displayed to the user

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(ImageInput(key, message, **kwargs))
        return self

    def read_dropdown(self, name: str, options, **kwargs):
        '''Add a dropdown input on the page

        Positional Arg:
            name: The name of the dropdown

        Keyword Arg:
            options: The options of the dropdown, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]
            multiple: Whether the user can select multiple options
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            placeholder: The placeholder of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', name)
        self.widgets.append(DropdownInput(key, name, options, **kwargs))
        return self

    def read_multiple_choice(self, message: str, options: Union[List[str], List[Dict]], **kwargs):
        '''Add a multiple choice input on the page

        Positional Arg:
            message: The message that will be displayed to the user
            options: The options of the multiple choice, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Arg:
            multiple: Whether the user can select multiple options
            key: The key of the input's value on the form result. Defaults to the message arg
            initial_value: The initial value of the input
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', message)
        self.widgets.append(MultipleChoiceInput(
            key, message, options, **kwargs))
        return self

    def read_cards(self, label: str, options, **kwargs):
        '''Add a cards input on the page

        Positional Arg:
            label: The text that will be displayed to the user
            options: The options of the multiple choice, eg. [
                {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'}, 
                {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

        Keyword Arg:

            multiple: Whether the user can select multiple options
            initial_value: The initial value of the input
            key: The key of the input's value on the form result. Defaults to the label arg
            required: Whether the input is required or not
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', label)
        self.widgets.append(CardsInput(key, label, options, **kwargs))
        return self

    def read_list(self, item_schema, **kwargs):
        '''Add a list input on the page

        Positional Arg:
            item_schema: The schema for the items of the list

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            columns: The number of columns of the input
            hint: The hint that will be displayed to the user
            initial_value: The initial value of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', '')
        self.widgets.append(ListInput(key, item_schema, **kwargs))
        return self

    def execute_js(self, code: str, **kwargs):
        """Execute JavaScript on the page

        Args:
            code: The JS code to be executed
        Keyword Arg:
            context (dict): variables to be passed to the JS code
            key (string): The key of the return value on the form result. Defaults to empty string

        Returns:
            string: Serialized return value of the executed JavaScript
        """

        key = kwargs.pop('key', 'js_result')
        self.widgets.append(ExecuteJs(key, code, **kwargs))
        return self

    def select_pandas_rows(self, df, **kwargs):
        '''Display a pandas dataframe as a table on the page and allow the user to select rows

        Positional Arg:
            df: The pandas dataframe to be displayed

        Keyword Arg:
            key: The key of the input's value on the form result. Defaults to the message arg
            required: Whether the input is required or not
            hint: The hint that will be displayed to the user
            columns: The number of columns of the input

        Returns:
            The form object
        '''
        key = kwargs.pop('key', 'rows')
        self.widgets.append(PandasRowSelectionInput(key, df, **kwargs))
        return self

    def display(self, message, **kwargs):
        '''Add a message to the page

        Keyword Arg:
            message: The message to display to the user
            columns: The number of columns of the message

        Returns:
            The form object
        '''
        self.widgets.append(TextOutput(message, **kwargs))
        return self

    def display_markdown(self, text, **kwargs):
        '''Add a formatted text to the page

        Positional Arg:
            text: The formatted text to display to the user

        Keyword Arg:
            columns: The number of columns of the text

        Returns:
            The form object
        '''
        self.widgets.append(MarkdownOutput(text, **kwargs))
        return self

    def display_image(self, image_str, **kwargs):
        '''Add an image to the page

        Positional Arg:
            image_str: The url or base64 encoding of the image to display to the user

        Keyword Arg:
            subtitle: The subtitle of the image
            columns: The number of columns of the image

        Returns:
            The form object
        '''
        self.widgets.append(ImageOutput(image_str, **kwargs))
        return self

    def display_link(self, link_url, **kwargs):
        '''Add a link to the page

        Positional Arg:
            link_url: The url of the link

        Keyword Arg:
            link_text: The text of the link
            columns: The number of columns of the link
            same_tab: Whether the link should open in the same tab or not

        Returns:
            The form object
        '''
        self.widgets.append(LinkOutput(link_url, **kwargs))
        return self

    def display_file(self, file, **kwargs):
        '''Add a button for the user to download a file to the page

        Positional Arg:
            file: The file to download

        Keyword Arg:
            download_text: The text of the button
            columns: The number of columns of the button

        Returns:
            The form object
        '''
        self.widgets.append(FileOutput(file, **kwargs))
        return self

    def display_html(self, html, **kwargs):
        '''Add an html snippet to the page

        Positional Arg:
            html: The html to display to the user

        Keyword Arg:
            columns: The number of columns of the html

        Returns:
            The form object
        '''
        self.widgets.append(HTMLOutput(html, **kwargs))
        return self

    def display_pandas(self, df, **kwargs):
        '''Add a pandas dataframe to the page

        Positional Arg:
            df: The pandas dataframe to display to the user

        Keyword Arg:
            columns: The number of columns of the dataframe

        Returns:
            The form object
        '''
        self.widgets.append(PandasOutput(df, **kwargs))
        return self

    def display_plotly(self, fig, **kwargs):
        '''Add a plotly figure to the page

        Positional Arg:
            fig: The plotly figure to display to the user

        Keyword Arg:
            columns: The number of columns of the figure

        Returns:
            The form object
        '''
        self.widgets.append(PlotlyOutput(fig, **kwargs))
        return self

    def display_iframe(self, url_or_html, **kwargs):
        '''Add an iframe to the page

        Positional Arg:
            url_or_html:  The link to the document or the own document to display

        Keyword Arg:
            width: The width of the iframe
            height: The height of the iframe
            columns: The number of columns of the iframe

        Returns:
            The iframe object
        '''
        self.widgets.append(IFrameOutput(url_or_html, **kwargs))
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
