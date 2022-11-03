from typing import List

from hackerforms.crud.connector import Connector
from hackerforms.crud.exceptions import MissingParameter
from hackerforms.generated.page import Page


class Client:
    def __init__(self, connector: Connector, row_page):
        self.connector = connector
        self.row_page = row_page

    def dropdown(self, **kwargs):
        table = kwargs.get("table", None)
        column = kwargs.get("column", None)
        if not table:
            raise MissingParameter("table")
        if not column:
            raise MissingParameter("column")

        self.check_table_existence(table)

        pk_column = self.get_primary_key_column(table)

        if pk_column != column:
            data = self.connector.select(
                self.get_column_values(table, *(pk_column, column))
            )
            options = [{"label": col, "value": pk} for (pk, col) in data]
        else:
            data = self.connector.select(self.get_column_values(table, column))
            options = [item[0] for item in data]

        return options

    def RowPage(self, **kwargs) -> Page:
        table = kwargs.get("table", None)
        if not table:
            raise MissingParameter("table")

        self.check_table_existence(table)

        return self.row_page(table, self.connector.insert)

    def get_column_values(self, table, *args):
        pass

    def check_table_existence(self, table):
        pass

    def get_primary_key_column(self, table):
        pass
