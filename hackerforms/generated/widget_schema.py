from hackerforms.widgets.input_types import *
from hackerforms.widgets.output_types import *
from hackerforms.reactive import Reactive
from typing import List, Union, Dict, Any
from hackerforms.common import Input
import io


class WidgetSchema:
    def __init__(self):
        self.widgets: List = []

    def reactive(self, callback):
        self.widgets.append(Reactive(callback))
        return self

    def convert_answer(self, form_answers: Dict) -> Dict:
        """Convert the answer from the form to the expected format
        Args:
            answer: The answer from the form
        Returns:
            The converted answer
        """
        answer: Dict = {}
        inputs = self.get_input_widgets()
        for input in inputs:
            answer[input.key] = input.convert_answer(form_answers.get(input.key))
        return answer

    def get_input_widgets(self):
        concrete_widgets = []
        for widget in self.widgets:
            if isinstance(widget, Reactive):
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

    def read_answer_sheet(
        self, label: str, options: list, number_of_questions: int, **kwargs
    ):

        """Retrieve the answers from a test on a usual answersheet

        Position Args:
                label (str): The label to display to the user
                options (list): The options which can be chosen as an answer
                number_of_questions (int): Number of questions the answersheet will cover

        Keyword Args:
                required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          list: The values/value selected by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(
            AnswerSheetInput(key, label, options, number_of_questions, **kwargs)
        )
        return self

    def read_cards(self, label: str, options: list, **kwargs):

        """Read a text value from the user simple text input

                Position Args:
                        label (str): The text related to this field
                        options (list): The options to display to the user, eg. [
        {'title': 'Option 1', 'subtitle': 'Subtitle 1', 'image': 'https://image_1.png', 'description': 'option 1 description', 'topLeftExtra': 'Left 1', 'topRightExtra': 'Right 1' },
        {'title': 'Option 2', 'subtitle': 'Subtitle 2', 'image': 'https://image_2.png', 'description': 'option 2 description', 'topLeftExtra': 'Left 2', 'topRightExtra': 'Right 2' }]

                Keyword Args:
                        multiple (bool): Whether the user can select multiple options. Defaults to False.
                        initial_value (list): The initial value to display to the user. Defaults to None.
                        required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                        hint (str): A tooltip displayed to the user. Defaults to None.
                        searchable (bool): Whether to show a search bar. Defaults to False.
                        full_width (bool): Whether the input should use full screen width. Defaults to False.
                        layout (str): Whether the cards layout should be 'list' or 'grid'. Defaults to 'list'.%%%
                        disabled (bool): Wether the input is disabled. Defaults to False.
                        end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

                Returns:
                  list, any: The options/option selected by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(CardsInput(key, label, options, **kwargs))
        return self

    def read_checkbox(self, label: str, **kwargs):

        """Read a checkbox value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (null): The initial value to display to the user. Defaults to None.
                required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.

        Returns:
          list(str) or list(float): The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(CheckboxInput(key, label, **kwargs))
        return self

    def read_checklist(self, label: str, options: list, **kwargs):

        """Read a checklist value from the user

        Position Args:
                label (str): The label to display to the user
                options (list): TN options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Args:
                initial_value (null): The initial value to display to the user. Defaults to None.
                required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.

        Returns:
          list or any: The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(ChecklistInput(key, label, options, **kwargs))
        return self

    def read_cnpj(self, label: str, **kwargs):

        """Read a cnpj value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (null): The initial value to display to the user. Defaults to None.
                placeholder (str): The placeholder text to display to the user. Defaults to "00.000.000/0001-00".
                required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.

        Returns:
          list(str) or list(float): The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(CnpjInput(key, label, **kwargs))
        return self

    def read_code(self, label: str, **kwargs):

        """Read a piece of code from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                language (str): The programming language. Defaults to None.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(CodeInput(key, label, **kwargs))
        return self

    def read_cpf(self, label: str, **kwargs):

        """Read a cpf value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                placeholder (str): The placeholder text to display to the user. Defaults to "000.000.000-00".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(CpfInput(key, label, **kwargs))
        return self

    def read_currency(self, label: str, **kwargs):

        """Read currency value from the user

        Position Args:
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
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(CurrencyInput(key, label, **kwargs))
        return self

    def read_date(self, label: str, **kwargs):

        """Read a date value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (datetime.date or time.struct_time or str (YYYY-MM-DD)): The initial value to display to the user. Defaults to None.
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(DateInput(key, label, **kwargs))
        return self

    def read_dropdown(self, label: str, options: list, **kwargs):

        """Read a dropdown value from the user

        Position Args:
                label (str): The label to display to the user
                options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Args:
                multiple (bool): Whether the user can select multiple options. Defaults to False.
                initial_value (null): The initial value to display to the user. Defaults to None.
                placeholder (str): The placeholder text to display to the user. Defaults to "Choose an option".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value selected by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(DropdownInput(key, label, options, **kwargs))
        return self

    def read_email(self, label: str, **kwargs):

        """Read an email value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                placeholder (str): The placeholder text to display to the user. Defaults to "Your email here".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                invalid_email_message (str): Invalid e-mail message
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(EmailInput(key, label, **kwargs))
        return self

    def read_file(self, label: str, **kwargs):

        """Read a file value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
                max_file_size (float): Maximum size allowed to be transfered in total in MB.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          A dict containing the file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of files in case of multiple flag set as True
        """

        key = kwargs.pop("key", label)

        self.widgets.append(FileInput(key, label, **kwargs))
        return self

    def read_image(self, label: str, **kwargs):

        """Read a image file value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          A dict containing the image file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of images in case of multiple flag set as True
        """

        key = kwargs.pop("key", label)

        self.widgets.append(ImageInput(key, label, **kwargs))
        return self

    def read_list(self, item_schema: Any, **kwargs):

        """Read a list value from the user

        Position Args:
                item_schema (Any): The schema for the items of the list

        Keyword Args:
                initial_value (any): The initial value to display to the user. Defaults to [{}].
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                min (float): Min value accepted by the input. Defaults to None.
                max (float): Max value accepted by the input. Defaults to None.
                add_button_text (str): Label to be displayed on the add button. Defaults to "+".
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The values entered by the user
        """

        key = kwargs.pop("key", "result")

        self.widgets.append(ListInput(key, item_schema, **kwargs))
        return self

    def read_multiple_choice(self, label: str, options: list, **kwargs):

        """Read a multiple choice value from the user

        Position Args:
                label (str): The label to display to the user
                options (list): TN options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Args:
                multiple (bool): Whether the user can select multiple options. Defaults to False.
                min (number): The minimal amount of options that should be selected. Defaults to None.
                max (number): The maximum amount of options that should be selected. Defaults to None.
                initial_value (null): The initial value to display to the user. Defaults to None.
                required (bool or str): WNther the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.

        Returns:
          list or any: The values/value selected by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(MultipleChoiceInput(key, label, options, **kwargs))
        return self

    def read_nps(self, label: str, **kwargs):

        """Gets NPS feedback from user

        Position Args:
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
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(NpsInput(key, label, **kwargs))
        return self

    def read_number(self, label: str, **kwargs):

        """Read a number value from the user

        Position Args:
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
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(NumberInput(key, label, **kwargs))
        return self

    def read_number_slider(self, label: str, **kwargs):

        """Read a number value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to 0.
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                min (float): Min value accepted by the input. Defaults to None.
                max (float): Max value accepted by the input. Defaults to None.
                step (float): The value to be incremented or decremented while using the input button. Defaults to None.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(NumberSliderInput(key, label, **kwargs))
        return self

    def read_pandas_row_selection(self, df: Any, **kwargs):

        """Display a pandas dataframe as a table and allow the user to select rows

        Position Args:
                df (Any): The pandas dataframe to be displayed

        Keyword Args:
                required (null): Whether the input is required or not. Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The list of selected rows
        """

        key = kwargs.pop("key", "result")

        self.widgets.append(PandasRowSelectionInput(key, df, **kwargs))
        return self

    def read_password(self, label: str, **kwargs):

        """Read a password value from the user

        Position Args:
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
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(PasswordInput(key, label, **kwargs))
        return self

    def read_phone(self, label: str, **kwargs):

        """Read a phone value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str or dict): The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to "".
                placeholder (str): The placeholder text to display to the user. Defaults to "".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          A dict containing the value entered by the user ({"raw": str, "masked": str})
        """

        key = kwargs.pop("key", label)

        self.widgets.append(PhoneInput(key, label, **kwargs))
        return self

    def read_rating(self, label: str, **kwargs):

        """Read a rating value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to 0.
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                max (float): Max value accepted by the input. Defaults to None.
                char (str): Which char should be displayed as icon?
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(RatingInput(key, label, **kwargs))
        return self

    def read_tag(self, label: str, **kwargs):

        """Read a tag value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (list): The initial value to display to the user. Defaults to [].
                placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          list(str) or list(float): The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(TagInput(key, label, **kwargs))
        return self

    def read(self, label: str, **kwargs):

        """Read a text value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                mask (str): A mask to apply to the input. Defaults to None.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(TextInput(key, label, **kwargs))
        return self

    def read_textarea(self, label: str, **kwargs):

        """Read a textarea value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          The value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(TextareaInput(key, label, **kwargs))
        return self

    def read_time(self, label: str, **kwargs):

        """Read a time value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                format (str): Whether the input is in the format 24hs or AM/PM. Defaults to "24hs".
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          A datetime.time object representing the value entered by the user
        """

        key = kwargs.pop("key", label)

        self.widgets.append(TimeInput(key, label, **kwargs))
        return self

    def read_toggle(self, label: str, **kwargs):

        """Read a toggle value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                on_text (str): Text of On Toggle option
                off_text (str): Text of Off Toggle option
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.

        Returns:
          bool: if the toggle was checked
        """

        key = kwargs.pop("key", label)

        self.widgets.append(ToggleInput(key, label, **kwargs))
        return self

    def read_video(self, label: str, **kwargs):

        """Read a video file value from the user

        Position Args:
                label (str): The label to display to the user

        Keyword Args:
                initial_value (str): The initial value to display to the user. Defaults to "".
                required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
                hint (str): A tooltip displayed to the user. Defaults to None.
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
                disabled (bool): Wether the input is disabled. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.

        Returns:
          A dict containing the video uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of videos in case of multiple flag set as True
        """

        key = kwargs.pop("key", label)

        self.widgets.append(VideoInput(key, label, **kwargs))
        return self

    def display_file(self, file: Union[str, io.IOBase], **kwargs):

        """Display a button for the user to download a file

        Position Args:
                file (Union[str, io.IOBase]): The file to download

        Keyword Args:
                download_text (str): The text to display on the button that will download the file. Defaults to "Download here".
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(FileOutput(file, **kwargs))
        return self

    def display_html(self, html: str, **kwargs):

        """Display a html snippet to the user

        Position Args:
                html (str): The html snippet to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(HtmlOutput(html, **kwargs))
        return self

    def display_iframe(self, url_or_html: str, **kwargs):

        """Display an inline iframe to the user

        Position Args:
                url_or_html (str): The link to the document or the own document to display to the user

        Keyword Args:
                width (int): The width of the iframe. Defaults to "800".
                height (int): The height of the iframe. Defaults to "600".
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(IframeOutput(url_or_html, **kwargs))
        return self

    def display_image(self, image: Union[str, io.IOBase], **kwargs):

        """Display an image to the user

        Position Args:
                image (Union[str, io.IOBase]): The image to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                subtitle (str): The subtitle of the image. Defaults to "".
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(ImageOutput(image, **kwargs))
        return self

    def display_latex(self, text: str, **kwargs):

        """Display a latex formula to the user

        Position Args:
                text (str): The latex formula to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(LatexOutput(text, **kwargs))
        return self

    def display_link(self, link_url: str, **kwargs):

        """Display a link to the user

        Position Args:
                link_url (str): The url of the link to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                link_text (str): The text to display on the link. Defaults to "Click here".
                same_tab (bool): Whether to open the link in the same tab or not. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(LinkOutput(link_url, **kwargs))
        return self

    def display_markdown(self, text: str, **kwargs):

        """Display a formatted text to the user

        Position Args:
                text (str): The formatted text to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(MarkdownOutput(text, **kwargs))
        return self

    def display_pandas(self, df: Any, **kwargs):

        """Display a pandas dataframe to the user

        Position Args:
                df (Any): The dataframe to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                display_index (bool): Whether to show a index column. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(PandasOutput(df, **kwargs))
        return self

    def display_plotly(self, fig: Any, **kwargs):

        """Display a plotly figure to the user

        Position Args:
                fig (Any): The figure to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(PlotlyOutput(fig, **kwargs))
        return self

    def display_progress(self, current: float, total: float, **kwargs):

        """Display a progress bar. This widget is shown on screen until the script shows a new widget. This widget does not work on Pages, and must be used only with its function.

        Position Args:
                current (float): The progress being made. Defaults to 50.
                total (float): Total progress. Defaults to 100.

        Keyword Args:
                text (str): The text displayed with this progress step. Defaults to "".
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(ProgressOutput(current, total, **kwargs))
        return self

    def display(self, text: str, **kwargs):

        """Display a text to the user

        Position Args:
                text (str): The text to display to the user

        Keyword Args:
                full_width (bool): Whether the input should use full screen width. Defaults to False.
                end_program (bool): Whether the program should end after the widget is shown. Defaults to False.


        """

        self.widgets.append(TextOutput(text, **kwargs))
        return self

    input = read
