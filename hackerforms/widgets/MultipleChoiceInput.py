from hackerforms.common import Input
from typing import List, Dict, Union, Any


class MultipleChoiceInput(Input):
    type = "multiple-choice-input"

    def __init__(
        self, key: str, label: str, options: Union[List[str], List[Dict]], **kwargs
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
        self.disabled = kwargs.get("disabled", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "options": self.options,
            "hint": self.hint,
            "multiple": self.multiple,
            "initialValue": self.initial_value or ([] if self.multiple else None),
            "required": self.required and not self.multiple,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "min": self.min,
            "max": self.max,
            "disabled": self.disabled,
        }

    def convert_answer(self, answer: Union[List, Any]) -> Union[List, Any]:
        """
        Returns:
            list or any: The values/value selected by the user
        """
        return answer
