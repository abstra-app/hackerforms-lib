from hackerforms.common import Input
import datetime


class TimeInput(Input):
    type = "time-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a time value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (Union[bool, str]): Whether the input is required or not eg. "this field is required". Defaults to True.
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
        self.disabled = kwargs.get("disabled", False)

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
            "disabled": self.disabled,
        }

    @staticmethod
    def __convert_answer(answer) -> datetime.time:
        return datetime.time(answer["hour"], answer["minute"]) if answer else None

    def convert_answer(self, answer) -> datetime.time:
        """
        Returns:
            datetime.time: A datetime.time object representing the value entered by the user
        """
        return self.__convert_answer(answer)
