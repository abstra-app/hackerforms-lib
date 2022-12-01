from hackerforms.common import Input


class NpsInput(Input):
    type = "nps-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Gets NPS feedback from user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            min (int): Min value accepted by the input. Defaults to 0.
            max (int): Max value accepted by the input. Defaults to 10.
            min_hint (str): Text to display next to the min value. Defaults to "Not at all likely".
            max_hint (str): Text to display next to the max value. Defaults to "Extremely likely".
            initial_value (str): The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.min = kwargs.get("min", 0)
        self.max = kwargs.get("max", 10)
        self.min_hint = kwargs.get("min_hint", "Not at all likely")
        self.max_hint = kwargs.get("max_hint", "Extremely likely")
        self.columns = kwargs.get("columns", 1)
        self.hint = kwargs.get("hint", None)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "min": self.min,
            "max": self.max,
            "minHint": self.min_hint,
            "maxHint": self.max_hint,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "hint": self.hint,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer: int) -> int:
        """
        Returns:
            int: The value entered by the user
        """
        return answer
