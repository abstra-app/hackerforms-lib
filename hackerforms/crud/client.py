from hackerforms.crud.connector import Connector
from hackerforms.crud.exceptions import MissingParameter
from hackerforms.crud.row_page import RowPage
from hackerforms.generated.page import Page


class Client:
    def __init__(self, connector: Connector, row_page: RowPage):
        self.connector = connector
        self.row_page = row_page

    def dropdown(self, **kwargs):
        table = kwargs.get("table", None)
        column = kwargs.get("column", None)
        primary_key = kwargs.get("primary_key", None)

        if not table:
            raise MissingParameter("table")
        if not column:
            raise MissingParameter("column")
        if not primary_key:
            raise MissingParameter("primary_key")

        columns = (primary_key, column) if primary_key != column else (primary_key, )
        data = self.connector.select(
            self.get_column_values(table, *columns)
        )
        options = [{"label": col, "value": pk} for (pk, col) in data]

        return options

    def RowPage(self, **kwargs) -> Page:
        table = kwargs.get("table", None)
        if not table:
            raise MissingParameter("table")

        return self.row_page(table, self.connector)

    def get_column_values(self, table, *args):
        pass
