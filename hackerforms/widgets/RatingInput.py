from hackerforms.common import Input


class RatingInput(Input):
    type = "rating-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a number value from the user using a slider

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to 0.
            required (Union[bool, str]): Whether the input is required or not eg. "this field is required". Defaults to True.
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
        self.disabled = kwargs.get("disabled", False)

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
            "disabled": self.disabled,
        }

    def convert_answer(self, answer: float) -> float:
        """
        Returns:
            float: The value entered by the user
        """
        return answer
