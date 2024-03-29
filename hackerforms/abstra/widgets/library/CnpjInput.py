from ..widget_base import Input


class CnpjInput(Input):
    type = "cnpj-input"

    def __init__(self, key: str, label: str, **kwargs):
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.placeholder = kwargs.get("placeholder", "00.000.000/0001-00")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.disabled = kwargs.get("disabled", False)
        self.invalid_message = kwargs.get("invalid_message", "")

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
            "invalidMessage": self.invalid_message,
        }

    def convert_answer(self, answer: str) -> str:
        return answer
