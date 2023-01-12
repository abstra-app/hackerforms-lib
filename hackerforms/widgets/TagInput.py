from hackerforms.common import Input
from typing import List, Union


class TagInput(Input):
    type = "tag-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a tag value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (list): The initial value to display to the user. Defaults to [].
            placeholder (str): The placeholder text to display to the user. Defaults to "Your answer here".
            required (Union[bool, str]): Whether the input is required or not eg. "this field is required". Defaults to True.
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
        self.disabled = kwargs.get("disabled", False)

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
            "disabled": self.disabled,
        }

    def convert_answer(
        self, answer: List[Union[str, float]]
    ) -> List[Union[str, float]]:
        """
        Returns:
            list(str) or list(float): The value entered by the user
        """
        return answer
