from hackerforms.common import Input
from typing import Optional
from hackerforms.response_types import PhoneResponse


class PhoneInput(Input):
    type = "phone-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a phone number value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str or dict): The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to "".
            placeholder (str): The placeholder text to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.placeholder = kwargs.get("placeholder", "")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def _initial_value_to_json(self, initial_value):
        if isinstance(initial_value, str):
            return {"countryCode": "+1", "nationalNumber": initial_value}
        return {
            "countryCode": initial_value["country_code"]
            if "country_code" in initial_value
            else "",
            "nationalNumber": initial_value["national_number"]
            if "national_number" in initial_value
            else "",
        }

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "initialValue": self._initial_value_to_json(self.initial_value),
            "placeholder": self.placeholder,
            "required": self.required,
            "hint": self.hint,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> Optional[PhoneResponse]:
        """
        Returns:
            PhoneResponse: A dict containing the value entered by the user ({"raw": str, "masked": str})
        """
        return (
            PhoneResponse(
                masked=answer["masked"],
                raw=answer["raw"],
                country_code=answer["countryCode"],
                national_number=answer["nationalNumber"],
            )
            if answer
            else None
        )
