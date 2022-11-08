###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################

import typing
import io
from ..socket import send, receive
from .input_types import *
from .output_types import *
from .validation import validate_widget_props
from .realtime import Realtime


class WidgetSchema:
    def __init__(self):
        self.widgets: typing.List[typing.Union[Input, Output]] = []

    def realtime(self, callback):
        self.widgets.append(Realtime(callback))
        return self

    def convert_answer(self, form_answers: typing.Dict) -> typing.Dict:
        """Convert the answer from the form to the expected format
        Args:
            answer: The answer from the form
        Returns:
            The converted answer
        """
        answer: typing.Dict = {}
        inputs = self.get_input_widgets()
        for input in inputs:
            answer[input.key] = input.convert_answer(form_answers.get(input.key))
        return answer

    def get_input_widgets(self):
        concrete_widgets = []
        for widget in self.widgets:
            if isinstance(widget, Realtime):
                concrete_widgets.extend(widget.get_widgets())
            else:
                concrete_widgets.append(widget)

        inputs = list(
            filter(lambda widget: isinstance(widget, Input), concrete_widgets)
        )
        return inputs

    def json(self, payload):
        output = []
        for widget in self.widgets:
            widget_json = widget.json(payload=payload)
            if isinstance(widget_json, list):
                output.extend(widget_json)
            else:
                output.append(widget_json)

        return output

    def read_cards(self, label: str, options: typing.Any, **kwargs):
        """Read cards from the user

        Positional Args:
          label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},{'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

        Keyword Args:
          multiple (bool): Whether the user can select multiple options. Defaults to False.
          initial_value (list): The initial value to display to the user. Defaults to None.
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          searchable (bool): Whether to show a search bar. Defaults to False.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(CardsInput(key, label, options, **kwargs))
        return self

    def read_code(self, label: str, **kwargs):
        """Read a code snippet from the user with a text highlight

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          language (str): The programming language. Defaults to None.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(CodeInput(key, label, **kwargs))
        return self

    def read_currency(self, label: str, **kwargs):
        """Read a number value from the user with a currency mask

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
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(CurrencyInput(key, label, **kwargs))
        return self

    def read_date(self, label: str, **kwargs):
        """Read a date value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (datetime.date or time.struct_time or str (YYYY-MM-DD)): The initial value to display to the user. Defaults to None.
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(DateInput(key, label, **kwargs))
        return self

    def read_dropdown(
        self,
        label: str,
        options: typing.Union[typing.List[str], typing.List[typing.Dict]],
        **kwargs
    ):
        """Read a dropdown value from the user

        Positional Args:
          label (str): The label to display to the useroptions (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Args:
          multiple (bool): Whether the user can select multiple options. Defaults to False.
          initial_value: The initial value to display to the user. Defaults to None.
          placeholder (str): The placeholder text to display to the user. Defaults to "Choose an option".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(DropdownInput(key, label, options, **kwargs))
        return self

    def read_email(self, label: str, **kwargs):
        """Read an email value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          placeholder (str): The placeholder text to display to the user. Defaults to "Your email here".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(EmailInput(key, label, **kwargs))
        return self

    def read_file(self, label: str, **kwargs):
        """Read a file value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(FileInput(key, label, **kwargs))
        return self

    def read_html_list(self, label: str, options: typing.Any, **kwargs):
        """Read list of html values from the user

        Positional Args:
          label (str): The text related to this fieldoptions (list): The options to display to the user, eg. [{'html': '<div class="container">Info 1A</div>', 'value': 'info1'},{'html': '<div class="container">Info 2B</div>', 'value': 'info2'}]

        Keyword Args:
          initial_value (list): The initial value to display to the user. Defaults to None.
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          multiple (bool): Whether the user can select multiple options. Defaults to False.
          css (str): The css related to the html item in options. Defaults to None.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(HTMLListInput(key, label, options, **kwargs))
        return self

    def read_image(self, label: str, **kwargs):
        """Read a image file value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(ImageInput(key, label, **kwargs))
        return self

    def read_list(self, item_schema: typing.Any, **kwargs):
        """Read a list value from the user

        Positional Args:
          item_schema (ListItemSchema): The schema for the items of the list

        Keyword Args:
          initial_value (any): The initial value to display to the user. Defaults to [{}].
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          min (float): Min value accepted by the input. Defaults to None.
          max (float): Max value accepted by the input. Defaults to None.
          add_button_text (str): Label to be displayed on the add button. Defaults to "+".
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the "result" arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", "result")
        self.widgets.append(ListInput(key, item_schema, **kwargs))
        return self

    def read_multiple_choice(
        self,
        label: str,
        options: typing.Union[typing.List[str], typing.List[typing.Dict]],
        **kwargs
    ):
        """Read a multiple choice value from the user

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
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(MultipleChoiceInput(key, label, options, **kwargs))
        return self

    def read_nps(self, label: str, **kwargs):
        """Gets NPS feedback from user

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
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(NpsInput(key, label, **kwargs))
        return self

    def read_number(self, label: str, **kwargs):
        """Read a number value from the user

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
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(NumberInput(key, label, **kwargs))
        return self

    def read_pandas_row_selection(self, df: typing.Any, **kwargs):
        """Display a pandas dataframe as a table and allow the user to select rows

        Positional Args:
          df (pandas.DataFrame): The pandas dataframe to be displayed

        Keyword Args:
          required: Whether the input is required or not. Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the "result" arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", "result")
        self.widgets.append(PandasRowSelectionInput(key, df, **kwargs))
        return self

    def read_password(self, label: str, **kwargs):
        """Read a password value from the user

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
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(PasswordInput(key, label, **kwargs))
        return self

    def read_phone(self, label: str, **kwargs):
        """Read a phone number value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str or dict): The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to "".
          placeholder (str): The placeholder text to display to the user. Defaults to "".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(PhoneInput(key, label, **kwargs))
        return self

    def read_tag(self, label: str, **kwargs):
        """Read a tag value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (list): The initial value to display to the user. Defaults to [].
          placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(TagInput(key, label, **kwargs))
        return self

    def read(self, label: str, **kwargs):
        """Read a text value from the user simple text input

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          mask (str): A mask to apply to the input. Defaults to None.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """

        key = kwargs.pop("key", label)
        self.widgets.append(TextInput(key, label, **kwargs))
        return self

    def read_textarea(self, label: str, **kwargs):
        """Read a text value from the user with a text area input

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(TextareaInput(key, label, **kwargs))
        return self

    def read_time(self, label: str, **kwargs):
        """Read a time value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          format (str): Whether the input is in the format 24hs or AM/PM. Defaults to "24hs".
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(TimeInput(key, label, **kwargs))
        return self

    def read_video(self, label: str, **kwargs):
        """Read a video file value from the user

        Positional Args:
          label (str): The label to display to the user

        Keyword Args:
          initial_value (str): The initial value to display to the user. Defaults to "".
          required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
          hint (str): A tooltip displayed to the user. Defaults to None.
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
          columns: The number of columns of the input
          key: The key of the input's value on the form result. Defaults to the label arg


        Returns:
          The form object
        """
        key = kwargs.pop("key", label)
        self.widgets.append(VideoInput(key, label, **kwargs))
        return self

    def display_file(self, file: typing.Union[str, io.IOBase], **kwargs):
        """Display a button for the user to download a file


        Positional Args:
          file (file-like or str (path, url, base64)): The file to download


        Keyword Args:
          download_text (str): The text to display on the button that will download the file. Defaults to "Download here".
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(FileOutput(file, **kwargs))
        return self

    def display_html(self, html: str, **kwargs):
        """Display a html snippet to the user


        Positional Args:
          html (str): The html snippet to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(HTMLOutput(html, **kwargs))
        return self

    def display_iframe(self, url_or_html: str, **kwargs):
        """Display an inline iframe to the user


        Positional Args:
          url_or_html (str): The link to the document or the own document to display to the user


        Keyword Args:
          width (int): The width of the iframe. Defaults to "800".
          height (int): The height of the iframe. Defaults to "600".
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(IFrameOutput(url_or_html, **kwargs))
        return self

    def display_image(self, image: typing.Union[str, io.IOBase], **kwargs):
        """Display an image to the user


        Positional Args:
          image (file-like or str (path, url, base64)): The image to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          subtitle (str): The subtitle of the image. Defaults to "".
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(ImageOutput(image, **kwargs))
        return self

    def display_link(self, link_url: str, **kwargs):
        """Display a link to the user


        Positional Args:
          link_url (str): The url of the link to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          link_text (str): The text to display on the link. Defaults to "Click here".
          same_tab (bool): Whether to open the link in the same tab or not. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(LinkOutput(link_url, **kwargs))
        return self

    def display_markdown(self, text: str, **kwargs):
        """Display a formatted text to the user


        Positional Args:
          text (str): The formatted text to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(MarkdownOutput(text, **kwargs))
        return self

    def display_pandas(self, df: typing.Any, **kwargs):
        """Display a pandas dataframe to the user


        Positional Args:
          df (pandas.DataFrame): The dataframe to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          display_index (bool): Whether to show a index column. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(PandasOutput(df, **kwargs))
        return self

    def display_plotly(self, fig: typing.Any, **kwargs):
        """Display a plotly figure to the user


        Positional Args:
          fig (plotly.Figure): The figure to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(PlotlyOutput(fig, **kwargs))
        return self

    def display_progress(self, dividend: float, divisor: float, **kwargs):
        """Display a progress bar


        Positional Args:
          dividend (float): The progress being made. Defaults to 50.
          divisor (float): Total progress. Defaults to 100.


        Keyword Args:
          text (str): The text displayed with this progress step. Defaults to "".
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(ProgressOutput(dividend, divisor, **kwargs))
        return self

    def display(self, text: str, **kwargs):
        """Display a text to the user


        Positional Args:
          text (str): The text to display to the user


        Keyword Args:
          full_width (bool): Whether the input should use full screen width. Defaults to False.
          columns: The number of columns of the input


        Returns:
          The form object
        """
        self.widgets.append(TextOutput(text, **kwargs))
        return self

    input = read


class PageResponse(dict):
    def __init__(self, data, action):
        self.action = action
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __contains__(self, key):
        return key in self.data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __cmp__(self, cmp_dict):
        return self.__cmp__(self.data, cmp_dict)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def clear(self):
        return self.data.clear()

    def copy(self):
        return PageResponse(self.data.copy(), self.action)

    def has_key(self, key):
        return key in self.data

    def update(self, *args, **kwargs):
        return self.data.update(*args, **kwargs)

    def pop(self, *args):
        return self.data.pop(*args)


class Page(WidgetSchema):
    """A form page that can be displayed to the user

    This is a page that can be displayed to the user. It can be used to
    show data as well as collect informations. After configuring the
    inputs and outputs, use the run method to display the form to the
    user and collect the answers.
    """

    def __init__(self):
        super().__init__()

    def run(
        self, actions="Next", columns: float = 1, validate: typing.Callable = None
    ) -> typing.Dict:
        """Run the form

        Args:
            button_text: The text of the button that is used to submit the form
            columns: The number of columns of the form

        Returns:
            The form result as a dict with the keys being the key of the input and the value being the value of the input
        """

        widgets_json = self.__get_validated_page_widgets_json({})

        if self.__is_progress_screen():
            self.__send_form_message(widgets=widgets_json, columns=columns, actions=[])
            return

        self.__send_form_message(
            widgets=widgets_json,
            columns=columns,
            actions=self.__actions_property(actions),
        )
        response: typing.Dict = self.__user_event_messages(validate=validate)

        return PageResponse(
            self.convert_answer(response["payload"]),
            response.get("action"),
        )

    def __user_event_messages(self, **kwargs):
        response: typing.Dict = receive()

        while response["type"] == "user-event":
            payload = response["payload"]
            widgets_json = self.__get_validated_page_widgets_json(payload)
            self.__send_user_event_message(
                widgets=widgets_json,
                validation=self.__build_validation_object(
                    validation=kwargs.get("validate"), payload=payload
                ),
            )

            response = receive()

        return response

    def __get_validated_page_widgets_json(self, raw_payload):
        widgets_json = self.json(self.convert_answer(raw_payload))
        for widget in widgets_json:
            validate_widget_props(widget)
        return widgets_json

    def __actions_property(self, actions):
        if isinstance(actions, list):
            return actions
        elif actions is None:
            return []
        return [actions]

    def __is_progress_screen(self):
        return len(self.widgets) == 1 and self.widgets[0].type == "progress-output"

    def __build_validation_object(self, validation, payload):
        validation_status = True
        validation_message = ""

        if validation:
            validation_response = validation(payload)
            if type(validation_response) == bool:
                validation_status = validation_response
                validation_message = ""
            elif type(validation_response) == str:
                validation_status = False
                validation_message = validation_response

        return {"status": validation_status, "message": validation_message}

    def __send_form_message(self, widgets, actions, columns):
        send(
            {
                "type": "form",
                "widgets": widgets,
                "columns": columns,
                "actions": actions,
            }
        )

    def __send_user_event_message(self, widgets, validation):
        send(
            {
                "type": "user-event",
                "widgets": widgets,
                "validation": validation,
            }
        )


class ListItemSchema(WidgetSchema):
    """A schema for a list item

    This schema is used to define the schema of a list item.
    """

    def __init__(self):
        super().__init__()
