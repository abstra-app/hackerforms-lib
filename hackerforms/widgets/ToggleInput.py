from hackerforms.common import Input
from typing import Dict


class ToggleInput(Input):
    type = "toggle-input"

    def __init__(self, key: str, label: str, **kwargs):
        super().__init__(key)
        self.label = label
        self.on_text = kwargs.get("on_text", "Yes")
        self.off_text = kwargs.get("off_text", "No")
        self.initial_value = kwargs.get("initial_value", "")
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
            "onText": self.on_text,
            "offText": self.off_text,
            "initialValue": self.initial_value,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "disabled": self.disabled,
        }

    def convert_answer(self, answer: str) -> str:
        return True if answer == "1" else False
