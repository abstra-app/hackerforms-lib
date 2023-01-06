from hackerforms.common import Input


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
        self.disabled = kwargs.get("disabled", False)

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
            "disabled": self.disabled,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer
