from abc import abstractmethod, ABC
import typing
import time
import datetime
import json

from .file_utils import convert_file
from .response_types import FileResponse, PhoneResponse


class Input(ABC):
    type: str

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key

    @abstractmethod
    def json(self, **kwargs):
        pass

    @abstractmethod
    def convert_answer(self, answer):
        pass


class TextInput(Input):
    type = "text-input"

    def __init__(self, key: str, label: str, **kwargs):
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
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.placeholder = kwargs.get("placeholder", "Your answer here")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.mask = kwargs.get("mask", None)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "mask": self.mask,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer


class TagInput(Input):

    type = "tag-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a tag value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (list): The initial value to display to the user. Defaults to [].
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """

        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", [])
        self.placeholder = kwargs.get("placeholder", "Your answer here")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(
        self, answer: typing.List[typing.Union[str, float]]
    ) -> typing.List[typing.Union[str, float]]:
        """
        Returns:
            list(str) or list(float): The value entered by the user
        """

        return answer


class DateInput(Input):
    type = "date-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a date value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (datetime.date or time.struct_time or str (YYYY-MM-DD)): The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    @staticmethod
    def convert_value(value: typing.Union[datetime.date, time.struct_time, str]) -> str:
        if isinstance(value, datetime.date):
            return value.isoformat()
        elif isinstance(value, time.struct_time):
            return (
                datetime.datetime.fromtimestamp(time.mktime(value)).date().isoformat()
            )
        return value

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "label": self.label,
            "initialValue": DateInput.convert_value(self.initial_value)
            if self.initial_value
            else "",
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer: str) -> typing.Optional[datetime.date]:
        """
        Returns:
            datetime.date: The value entered by the user
        """
        if not answer:
            return None

        split_answer = answer.split("-")
        year = int(split_answer[0])
        month = int(split_answer[1])
        day = int(split_answer[2])
        return datetime.date(year, month, day)


class FileInput(Input):
    type = "file-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a file value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.multiple = kwargs.get("multiple", False)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "label": self.label,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "multiple": self.multiple,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> typing.Optional[FileResponse]:
        """
        Returns:
            FileResponse or FileResponse[]: A dict containing the file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of files in case of multiple flag set as True
        """
        if not answer:
            return None

        if not self.multiple:
            return FileResponse(answer)

        return [FileResponse(item) for item in answer]


class ImageInput(Input):
    type = "image-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a image file value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.multiple = kwargs.get("multiple", False)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "label": self.label,
            "initialValue": self.initial_value,
            "columns": self.columns,
            "required": self.required,
            "multiple": self.multiple,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> typing.Optional[FileResponse]:
        """
        Returns:
            FileResponse or FileResponse[]: A dict containing the image file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of images in case of multiple flag set as True
        """
        if not answer:
            return None

        if not self.multiple:
            return FileResponse(answer)

        return [FileResponse(item) for item in answer]


class VideoInput(Input):
    type = "video-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a video file value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.multiple = kwargs.get("multiple", False)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "label": self.label,
            "initialValue": self.initial_value,
            "columns": self.columns,
            "required": self.required,
            "multiple": self.multiple,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> typing.Optional[FileResponse]:
        """
        Returns:
            FileResponse or FileResponse[]: A dict containing the video uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of videos in case of multiple flag set as True
        """
        if not answer:
            return None

        if not self.multiple:
            return FileResponse(answer)

        return [FileResponse(item) for item in answer]


class MultipleChoiceInput(Input):
    type = "multiple-choice-input"

    def __init__(
        self,
        key: str,
        label: str,
        options: typing.Union[typing.List[str], typing.List[typing.Dict]],
        **kwargs
    ):
        """Read a multiple choice value from the user

        Positional Args:
            label (str): The label to display to the user
            options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Args:
            multiple (bool): Whether the user can select multiple options. Defaults to False.
            min (number): The minimal amount of options that should be selected. Defaults to None.
            max (number): The maximum amount of options that should be selected. Defaults to None.
            initial_value: The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.options = options
        self.multiple = kwargs.get("multiple", False)
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.min = kwargs.get("min", None)
        self.max = kwargs.get("max", None)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "options": self.options,
            "hint": self.hint,
            "multiple": self.multiple,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "min": self.min,
            "max": self.max,
        }

    def convert_answer(
        self, answer: typing.Union[typing.List, typing.Any]
    ) -> typing.Union[typing.List, typing.Any]:
        """
        Returns:
            list or any: The values/value selected by the user
        """
        return answer


class CardsInput(Input):
    type = "cards-input"

    def __init__(self, key: str, label: str, options: typing.Any, **kwargs):
        """Read cards from the user

        Positional Args:
            label (str): The text related to this field
            options (list): The options to display to the user, eg. [
                                {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},
                                {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

        Keyword Args:
            multiple (bool): Whether the user can select multiple options. Defaults to False.
            initial_value (list): The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            searchable (bool): Whether to show a search bar. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            direction (str): Whether the cards direction should be 'horizontal' or 'vertical'. Defaults to 'vertical'.
        """
        super().__init__(key)
        self.label = label
        self.options = options
        self.multiple = kwargs.get("multiple", False)
        self.searchable = kwargs.get("searchable", False)
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.direction = kwargs.get("direction", "vertical")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "hint": self.hint,
            "options": [
                {**opt, "image": convert_file(opt.get("image"))} for opt in self.options
            ],
            "multiple": self.multiple,
            "searchable": self.searchable,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "direction": self.direction,
        }

    def convert_answer(
        self, answer: typing.Union[typing.List, typing.Any]
    ) -> typing.Union[typing.List, typing.Any]:
        """
        Returns:
            list, any: The options/option selected by the user
        """
        return answer


class DropdownInput(Input):
    type = "dropdown-input"

    def __init__(
        self,
        key: str,
        label: str,
        options: typing.Union[typing.List[str], typing.List[typing.Dict]],
        **kwargs
    ):
        """Read a dropdown value from the user

        Positional Args:
            label (str): The label to display to the user
            options (list): The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]

        Keyword Args:
            multiple (bool): Whether the user can select multiple options. Defaults to False.
            initial_value: The initial value to display to the user. Defaults to None.
            placeholder (str): The placeholder text to display to the user. Defaults to "Choose an option".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.options = options
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.multiple = kwargs.get("multiple", False)
        self.placeholder = kwargs.get("placeholder", "Choose an option")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "options": self.options,
            "hint": self.hint,
            "multiple": self.multiple,
            "placeholder": self.placeholder,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value selected by the user
        """
        return answer


class TextareaInput(Input):
    type = "textarea-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a text value from the user with a text area input

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.placeholder = kwargs.get("placeholder", "Your answer here")
        self.columns = kwargs.get("columns", 1)
        self.hint = kwargs.get("hint", None)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "placeholder": self.placeholder,
            "required": self.required,
            "columns": self.columns,
            "hint": self.hint,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer


class CodeInput(Input):
    type = "code-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a code snippet from the user with a text highlight

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            language (str): The programming language. Defaults to None.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.language = kwargs.get("language", None)
        self.columns = kwargs.get("columns", 1)
        self.hint = kwargs.get("hint", None)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "language": self.language,
            "required": self.required,
            "columns": self.columns,
            "hint": self.hint,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer


class NpsInput(Input):
    type = "nps-input"

    def __init__(self, key: str, label: str, **kwargs):
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

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.min = kwargs.get("min", 0)
        self.max = kwargs.get("max", 10)
        self.min_hint = kwargs.get("min_hint", "Not at all likely")
        self.max_hint = kwargs.get("max_hint", "Extremely likely")
        self.columns = kwargs.get("columns", 1)
        self.hint = kwargs.get("hint", None)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "min": self.min,
            "max": self.max,
            "minHint": self.min_hint,
            "maxHint": self.max_hint,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "hint": self.hint,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer: int) -> int:
        """
        Returns:
            int: The value entered by the user
        """
        return answer


class NumberInput(Input):
    type = "number-input"

    def __init__(self, key: str, label: str, **kwargs):
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
        """

        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", 0)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.placeholder = kwargs.get("placeholder", "Your answer here")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.min = kwargs.get("min")
        self.max = kwargs.get("max")
        self.step = kwargs.get("step")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "min": self.min,
            "max": self.max,
            "step": self.step,
        }

    def convert_answer(self, answer: float) -> float:
        """
        Returns:
            float: The value entered by the user
        """
        return answer


class NumberSliderInput(Input):
    type = "number-slider-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a number value from the user using a slider

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            min (float): Min value accepted by the input. Defaults to None.
            max (float): Max value accepted by the input. Defaults to None.
            step (float): The value to be incremented or decremented while using the input button. Defaults to None.
        """

        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", 0)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.min = kwargs.get("min")
        self.max = kwargs.get("max")
        self.step = kwargs.get("step")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "min": self.min,
            "max": self.max,
            "step": self.step,
        }

    def convert_answer(self, answer: float) -> float:
        """
        Returns:
            float: The value entered by the user
        """
        return answer


class RatingInput(Input):
    type = "rating-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a number value from the user using a slider

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            max (float): Max value accepted by the input. Defaults to None.
            char (str): Which char should be displayed as icon?
        """

        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", 0)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.max = kwargs.get("max")
        self.char = kwargs.get("char")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "max": self.max,
            "char": self.char,
        }

    def convert_answer(self, answer: float) -> float:
        """
        Returns:
            float: The value entered by the user
        """
        return answer


class EmailInput(Input):
    type = "email-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read an email value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "Your email here".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            invalid_email_message (str): Invalid e-mail message. Defaults to "Hmm… doesn't look like an email".
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.placeholder = kwargs.get("placeholder", "Your email here")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.invalid_email_message = kwargs.get(
            "invalid_email_message", "Hmm… doesn't look like an email"
        )

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "invalidEmailMessage": self.invalid_email_message,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer


class PhoneInput(Input):
    type = "phone-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a phone number value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str or dict): The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.placeholder = kwargs.get("placeholder", "")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def _initial_value_to_json(self, initial_value):
        if isinstance(initial_value, str):
            return {"countryCode": "+1", "nationalNumber": initial_value}

        return {
            "countryCode": initial_value["country_code"]
            if "country_code" in initial_value
            else "",
            "nationalNumber": initial_value["national_number"]
            if "national_number" in initial_value
            else "",
        }

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self._initial_value_to_json(self.initial_value),
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> typing.Optional[PhoneResponse]:
        """
        Returns:
            PhoneResponse: A dict containing the value entered by the user ({"raw": str, "masked": str})
        """
        return (
            PhoneResponse(
                masked=answer["masked"],
                raw=answer["raw"],
                country_code=answer["countryCode"],
                national_number=answer["nationalNumber"],
            )
            if answer
            else None
        )


class ListInput(Input):
    type = "list-input"

    instances = []

    instances = []

    def __init__(self, key: str, item_schema: typing.Any, **kwargs):
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
        """
        super().__init__(key)
        self.item_schema = item_schema
        self.initial_value = kwargs.get("initial_value", [{}])
        self.min = kwargs.get("min", None)
        self.max = kwargs.get("max", None)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.add_button_text = kwargs.get("add_button_text", "+")
        self.full_width = kwargs.get("full_width", False)
        self.required = kwargs.get("required", True)

    def json(self, **kwargs):
        json = {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "itemSchema": self.item_schema.json(
                payload=self.item_schema.convert_answer({})
            ),
            "initialValue": self.initial_value,
            "columns": self.columns,
            "min": self.min,
            "max": self.max,
            "addButtonText": self.add_button_text,
            "fullWidth": self.full_width,
            "required": self.required,
        }

        overloaded_schemas = self.__get_overloaded_schemas(
            kwargs.get("payload").get(self.key) if kwargs.get("payload") else None
        )

        if overloaded_schemas:
            json["overloadedItemSchemas"] = overloaded_schemas

        return json

    def convert_answer(self, answers) -> typing.List:
        """
        Returns:
            list: The values entered by the user
        """
        return [
            self.instances[index].convert_answer(answer)
            if index < len(self.instances)
            else self.item_schema.convert_answer(answer)
            for index, answer in enumerate(answers or [])
        ]

    def __get_overloaded_schemas(self, payload):
        if payload:
            self.instances = [self.item_schema.copy() for _ in payload]
            return [
                self.instances[index].json(payload=payload_item)
                for index, payload_item in enumerate(payload)
            ]
        else:
            return None


class PandasRowSelectionInput(Input):

    type = "pandas-row-selection-input"

    def __init__(self, key: str, df: typing.Any, **kwargs):
        """Display a pandas dataframe as a table and allow the user to select rows

        Positional Args:
            df (pandas.DataFrame): The pandas dataframe to be displayed

        Keyword Args:
            required: Whether the input is required or not. Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        super().__init__(key)
        self.df = df
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "table": json.loads(self.df.to_json(orient="table")),
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> typing.List:
        """
        Returns:
            list: The list of selected rows
        """
        return answer


class HTMLListInput(Input):
    type = "html-list-input"

    def __init__(self, key: str, label: str, options: typing.Any, **kwargs):
        """Read list of html values from the user

        Positional Args:
            label (str): The text related to this field
            options (list): The options to display to the user, eg. [
                                {'html': '<div class="container">Info 1A</div>', 'value': 'info1'},
                                {'html': '<div class="container">Info 2B</div>', 'value': 'info2'}
                            ]

        Keyword Args:
            initial_value (list): The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            multiple (bool): Whether the user can select multiple options. Defaults to False.
            css (str): The css related to the html item in options. Defaults to None.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.options = options
        self.css = kwargs.get("css", None)
        self.multiple = kwargs.get("multiple", False)
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "hint": self.hint,
            "options": self.options,
            "css": self.css,
            "multiple": self.multiple,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(
        self, answer: typing.Union[typing.List, typing.Any]
    ) -> typing.Union[typing.List, typing.Any]:
        """
        Returns:
            list, any: The options/option selected by the user
        """
        return answer


class TimeInput(Input):
    type = "time-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a time value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            format (str): Whether the input is in the format 24hs or AM/PM. Defaults to "24hs".
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """

        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.format = kwargs.get("format", "24hs")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "format": self.format,
            "hint": self.hint,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> datetime.time:
        """
        Returns:
            datetime.time: A datetime.time object representing the value entered by the user
        """
        return datetime.time(answer["hour"], answer["minute"]) if answer else None


class CurrencyInput(Input):
    type = "currency-input"

    def __init__(self, key: str, label: str, **kwargs):
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
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", 0)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.placeholder = kwargs.get("placeholder", "Your answer here")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.min = kwargs.get("min")
        self.max = kwargs.get("max")
        self.step = kwargs.get("step")
        self.currency = kwargs.get("currency", "USD")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self.initial_value,
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "min": self.min,
            "max": self.max,
            "step": self.step,
            "currency": self.currency,
        }

    def convert_answer(self, answer) -> float:
        """
        Returns:
            float: The value entered by the user
        """
        return answer


class PasswordInput(Input):
    type = "password-input"

    def __init__(self, key: str, label: str, **kwargs):
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
        """

        super().__init__(key)
        self.label = label
        self.hint = kwargs.get("hint", None)
        self.required = kwargs.get("required", True)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.lowercase_required = kwargs.get("lowercase_required", True)
        self.uppercase_required = kwargs.get("uppercase_required", True)
        self.special_required = kwargs.get("special_required", True)
        self.digit_required = kwargs.get("digit_required", True)
        self.min_length = kwargs.get("min_length", 8)
        self.max_length = kwargs.get("max_length", None)
        self.size = kwargs.get("size", None)
        self.pattern = kwargs.get("pattern", None)
        self.autocomplete = kwargs.get("autocomplete", "current-password")
        self.placeholder = kwargs.get("placeholder", "")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "hint": self.hint,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "lowercaseRequired": self.lowercase_required,
            "uppercaseRequired": self.uppercase_required,
            "specialRequired": self.special_required,
            "digitRequired": self.digit_required,
            "minLength": self.min_length,
            "maxLength": self.max_length,
            "size": self.size,
            "pattern": self.pattern,
            "autocomplete": self.autocomplete,
            "placeholder": self.placeholder,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer
