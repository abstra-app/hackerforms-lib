from typing import Any, Dict
from hackerforms.page import Page
from hackerforms.utils import get_single_value


def read_answer_sheet(label: str, options: list, number_of_questions: int, **kwargs):

    """Retrieve the answers from a test on a usual answersheet

    Position Args:
            label (str): The label to display to the user
            options (list): The options which can be chosen as an answer
            number_of_questions (int): Number of questions the answersheet will cover

    Keyword Args:
            required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      list: The values/value selected by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page()
        .read_answer_sheet(label, options, number_of_questions, **kwargs)
        .run(button_text)
    )


def read_cards(label: str, options: list, **kwargs):

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
                    layout (str): Whether the cards layout should be 'list' or 'grid'. Defaults to 'list'.%%%
                    disabled (bool): Wether the input is disabled. Defaults to False.
                    end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
                    full_width (bool): Whether the input should use full screen width. Defaults to False.

            Returns:
              list, any: The options/option selected by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_cards(label, options, **kwargs).run(button_text)
    )


def read_checkbox(label: str, **kwargs):

    """Read a checkbox value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (null): The initial value to display to the user. Defaults to None.
            required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      list(str) or list(float): The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_checkbox(label, **kwargs).run(button_text))


def read_checklist(label: str, options: list, **kwargs):

    """Read a checklist value from the user

    Position Args:
            label (str): The label to display to the user
            options (list): TN options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

    Keyword Args:
            initial_value (null): The initial value to display to the user. Defaults to None.
            required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      list or any: The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_checklist(label, options, **kwargs).run(button_text)
    )


def read_cnpj(label: str, **kwargs):

    """Read a cnpj value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (null): The initial value to display to the user. Defaults to None.
            placeholder (str): The placeholder text to display to the user. Defaults to "00.000.000/0001-00".
            required (bool or str): Wether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      list(str) or list(float): The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_cnpj(label, **kwargs).run(button_text))


def read_code(label: str, **kwargs):

    """Read a piece of code from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            language (str): The programming language. Defaults to None.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_code(label, **kwargs).run(button_text))


def read_cpf(label: str, **kwargs):

    """Read a cpf value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "000.000.000-00".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_cpf(label, **kwargs).run(button_text))


def read_currency(label: str, **kwargs):

    """Read currency value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            required (bool or str): Whether the input is required or not, eg. "this field is required". Defaults to True.
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            hint (str): A tooltip displayed to the user. Defaults to None.
            min (float): The minimum value allowed, eg. "0". Defaults to None.
            max (float): The maximum value allowed, eg. "100". Defaults to None.
            step (float): The value to be incremented or decremented while using the input button. Defaults to None.
            currency (str): The currency to display to the user, eg. "USD", "BRL, "EUR", "GBP". Defaults to "USD".
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_currency(label, **kwargs).run(button_text))


def read_date(label: str, **kwargs):

    """Read a date value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (datetime.date or time.struct_time or str (YYYY-MM-DD)): The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_date(label, **kwargs).run(button_text))


def read_dropdown(label: str, options: list, **kwargs):

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
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value selected by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_dropdown(label, options, **kwargs).run(button_text)
    )


def read_email(label: str, **kwargs):

    """Read an email value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "Your email here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            invalid_email_message (str): Invalid e-mail message
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_email(label, **kwargs).run(button_text))


def read_file(label: str, **kwargs):

    """Read a file value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
            max_file_size (float): Maximum size allowed to be transfered in total in MB.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      A dict containing the file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of files in case of multiple flag set as True
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_file(label, **kwargs).run(button_text))


def read_image(label: str, **kwargs):

    """Read a image file value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      A dict containing the image file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of images in case of multiple flag set as True
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_image(label, **kwargs).run(button_text))


def read_list(item_schema: Any, **kwargs):

    """Read a list value from the user

    Position Args:
            item_schema (Any): The schema for the items of the list

    Keyword Args:
            initial_value (any): The initial value to display to the user. Defaults to [{}].
            hint (str): A tooltip displayed to the user. Defaults to None.
            min (float): Min value accepted by the input. Defaults to None.
            max (float): Max value accepted by the input. Defaults to None.
            add_button_text (str): Label to be displayed on the add button. Defaults to "+".
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The values entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_list(item_schema, **kwargs).run(button_text))


def read_multiple_choice(label: str, options: list, **kwargs):

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
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      list or any: The values/value selected by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_multiple_choice(label, options, **kwargs).run(button_text)
    )


def read_nps(label: str, **kwargs):

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
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_nps(label, **kwargs).run(button_text))


def read_number(label: str, **kwargs):

    """Read a number value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            min (float): Min value accepted by the input. Defaults to None.
            max (float): Max value accepted by the input. Defaults to None.
            step (float): The value to be incremented or decremented while using the input button. Defaults to None.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_number(label, **kwargs).run(button_text))


def read_number_slider(label: str, **kwargs):

    """Read a number value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            min (float): Min value accepted by the input. Defaults to None.
            max (float): Max value accepted by the input. Defaults to None.
            step (float): The value to be incremented or decremented while using the input button. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_number_slider(label, **kwargs).run(button_text))


def read_pandas_row_selection(df: Any, **kwargs):

    """Display a pandas dataframe as a table and allow the user to select rows

    Position Args:
            df (Any): The pandas dataframe to be displayed

    Keyword Args:
            required (null): Whether the input is required or not. Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The list of selected rows
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(
        Page().read_pandas_row_selection(df, **kwargs).run(button_text)
    )


def read_password(label: str, **kwargs):

    """Read a password value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            placeholder (str): The placeholder text to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
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
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_password(label, **kwargs).run(button_text))


def read_phone(label: str, **kwargs):

    """Read a phone value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str or dict): The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      A dict containing the value entered by the user ({"raw": str, "masked": str})
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_phone(label, **kwargs).run(button_text))


def read_rating(label: str, **kwargs):

    """Read a rating value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            max (float): Max value accepted by the input. Defaults to None.
            char (str): Which char should be displayed as icon?
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_rating(label, **kwargs).run(button_text))


def read_tag(label: str, **kwargs):

    """Read a tag value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (list): The initial value to display to the user. Defaults to [].
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      list(str) or list(float): The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_tag(label, **kwargs).run(button_text))


def read(label: str, **kwargs):

    """Read a text value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            mask (str): A mask to apply to the input. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read(label, **kwargs).run(button_text))


def read_textarea(label: str, **kwargs):

    """Read a textarea value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      The value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_textarea(label, **kwargs).run(button_text))


def read_time(label: str, **kwargs):

    """Read a time value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            format (str): Whether the input is in the format 24hs or AM/PM. Defaults to "24hs".
            hint (str): A tooltip displayed to the user. Defaults to None.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      A datetime.time object representing the value entered by the user
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_time(label, **kwargs).run(button_text))


def read_toggle(label: str, **kwargs):

    """Read a toggle value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            on_text (str): Text of On Toggle option
            off_text (str): Text of Off Toggle option
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      bool: if the toggle was checked
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_toggle(label, **kwargs).run(button_text))


def read_video(label: str, **kwargs):

    """Read a video file value from the user

    Position Args:
            label (str): The label to display to the user

    Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
            disabled (bool): Wether the input is disabled. Defaults to False.
            end_program (bool): Whether the program should end after the widget is shown. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

    Returns:
      A dict containing the video uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of videos in case of multiple flag set as True
    """

    button_text = kwargs.get("button_text", "Next")
    return get_single_value(Page().read_video(label, **kwargs).run(button_text))
