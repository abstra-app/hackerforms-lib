from hackerforms.common import Input
from typing import Union, List, Dict


class DropdownInput(Input):
    type = "dropdown-input"

    def __init__(
        self, key: str, label: str, options: Union[List[str], List[Dict]], **kwargs
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
