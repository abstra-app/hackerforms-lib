from hackerforms.common import Output
from typing import Any
import pandas
import json


class PandasOutput(Output):
    type = "pandas-output"

    def __init__(self, df: pandas.DataFrame, **kwargs):
        """Display a pandas dataframe to the user

        Positional Args:
            df (pandas.DataFrame): The dataframe to display to the user

        Keyword Args:
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            display_index (bool): Whether to show a index column. Defaults to False.

        """
        self.df = df
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)
        self.display_index = kwargs.get("display_index", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "table": json.loads(self.df.to_json(orient="table")),
            "columns": self.columns,
            "fullWidth": self.full_width,
            "displayIndex": self.display_index,
        }
