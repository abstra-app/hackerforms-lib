from hackerforms.common import Input
from typing import Union, Optional
import datetime
import time


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
    def convert_value(value: Union[datetime.date, time.struct_time, str]) -> str:
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

    def convert_answer(self, answer: str) -> Optional[datetime.date]:
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
