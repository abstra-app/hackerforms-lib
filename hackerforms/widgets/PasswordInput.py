from hackerforms.common import Input


class PasswordInput(Input):
    type = "password-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a password value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            placeholder (str): The placeholder text to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            lowercase_required (bool or str): Whether the input must have at least one lowercase character. Defaults to True.
            uppercase_required (bool or str): Whether the input must have at least one uppercase character. Defaults to True.
            special_required (bool or str): Whether the input must have at least one special character. Defaults to True.
            digit_required (bool or str): Whether the input must have at least one digit. Defaults to True.
            min_length (int): Minimum length of the password. Defaults to 8.
            max_length (int): Maximum length of the password. Defaults to None.
            size (int): Size of the password. Defaults to None.
            pattern (str): A regex pattern for the accepted password. Defaults to None.
            autocomplete (str): The autocomplete HTML attribute. Defaults to "current-password".
        """
        super().__init__(key)
        self.label = label
        self.hint = kwargs.get("hint", None)
        self.required = kwargs.get("required", True)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.lowercase_required = kwargs.get("lowercase_required", True)
        self.uppercase_required = kwargs.get("uppercase_required", True)
        self.special_required = kwargs.get("special_required", True)
        self.digit_required = kwargs.get("digit_required", True)
        self.min_length = kwargs.get("min_length", 8)
        self.max_length = kwargs.get("max_length", None)
        self.size = kwargs.get("size", None)
        self.pattern = kwargs.get("pattern", None)
        self.autocomplete = kwargs.get("autocomplete", "current-password")
        self.placeholder = kwargs.get("placeholder", "")
        self.disabled = kwargs.get("disabled", False)
        self.secret = True

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "hint": self.hint,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "lowercaseRequired": self.lowercase_required,
            "uppercaseRequired": self.uppercase_required,
            "specialRequired": self.special_required,
            "digitRequired": self.digit_required,
            "minLength": self.min_length,
            "maxLength": self.max_length,
            "size": self.size,
            "pattern": self.pattern,
            "autocomplete": self.autocomplete,
            "placeholder": self.placeholder,
            "disabled": self.disabled,
            "secret": self.secret,
        }

    def convert_answer(self, answer: str) -> str:
        """
        Returns:
            str: The value entered by the user
        """
        return answer
