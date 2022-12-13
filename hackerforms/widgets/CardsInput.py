from hackerforms.common import Input
from hackerforms.file_utils import convert_file
from typing import Union, List, Any


class CardsInput(Input):
    type = "cards-input"

    def __init__(self, key: str, label: str, options: Any, **kwargs):
        """Read cards from the user

        Positional Args:
            label (str): The text related to this field
            options (list): The options to display to the user, eg. [
                                {'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},
                                {'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]

        Keyword Args:
            multiple (bool): Whether the user can select multiple options. Defaults to False.
            initial_value (list): The initial value to display to the user. Defaults to None.
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            searchable (bool): Whether to show a search bar. Defaults to False.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            layout (str): Whether the cards layout should be 'list' or 'grid'. Defaults to 'grid'.
        """
        super().__init__(key)
        self.label = label
        self.options = options
        self.multiple = kwargs.get("multiple", False)
        self.searchable = kwargs.get("searchable", False)
        self.initial_value = kwargs.get("initial_value", None)
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.layout = kwargs.get("layout", "list")

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "label": self.label,
            "hint": self.hint,
            "options": [
                {**opt, "image": convert_file(opt.get("image"))} for opt in self.options
            ],
            "multiple": self.multiple,
            "searchable": self.searchable,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "layout": self.layout,
        }

    def convert_answer(self, answer: Union[List, Any]) -> Union[List, Any]:
        """
        Returns:
            list, any: The options/option selected by the user
        """
        return answer
