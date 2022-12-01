from hackerforms.common import Input
from typing import List, Any
import json


class PandasRowSelectionInput(Input):
    type = "pandas-row-selection-input"

    def __init__(self, key: str, df: Any, **kwargs):
        """Display a pandas dataframe as a table and allow the user to select rows

        Positional Args:
            df (pandas.DataFrame): The pandas dataframe to be displayed

        Keyword Args:
            required: Whether the input is required or not. Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        super().__init__(key)
        self.df = df
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "table": json.loads(self.df.to_json(orient="table")),
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }

    def convert_answer(self, answer) -> List:
        """
        Returns:
            list: The list of selected rows
        """
        return answer
