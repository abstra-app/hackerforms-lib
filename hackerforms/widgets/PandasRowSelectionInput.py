from hackerforms.common import Input
from typing import List, Any
import json


class PandasRowSelectionInput(Input):
    type = "pandas-row-selection-input"

    def __init__(self, key: str, df: Any, **kwargs):
        super().__init__(key)
        self.df = df
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.disabled = kwargs.get("disabled", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "table": json.loads(self.df.to_json(orient="table")),
            "required": self.required,
            "columns": self.columns,
            "fullWidth": self.full_width,
            "disabled": self.disabled,
        }

    def convert_answer(self, answer) -> List:
        """
        Returns:
            list: The list of selected rows
        """
        return answer
