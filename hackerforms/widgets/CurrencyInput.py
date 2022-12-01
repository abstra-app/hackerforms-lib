from hackerforms.common import Input


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
