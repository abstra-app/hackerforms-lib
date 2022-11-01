from abc import ABC
import random
from typing import Union
from hackerforms.crud import services

from hackerforms.crud.connector import Connector
from hackerforms.crud.types import ContextParams, PythonColumns
from hackerforms.crud.utils import tuple_to_str


class Client:
    def __init__(self, connector: Connector):
        self.connector = connector

    def insert_page(self, table: str, context: ContextParams = None):
        try:
            self.check_table_existence(table)
            py_columns, postgres_columns = self.get_columns_names(table)
            if context:
                self.validate_context(table, context, py_columns)

            primary_key_column = self.get_primary_key_column(table)
            page = services.new_page(
                {
                    "table_name": table,
                    "primary_key": primary_key_column,
                    "columns": postgres_columns,
                },
                context,
            )
            page[primary_key_column] = random.randint(20, 100)
            page = {**page, **context}
            self.connector.insert(self.get_new_row_query(table, page))
            return page

        except Exception as ex:
            print(ex)

    def search_page(self, table: str, **kwargs) -> Union[str, int]:
        search_by_column = kwargs.get("search_by", None)
        try:
            self.check_table_existence(table)
            if search_by_column:
                unique_column = self.validate_unique_column(table, search_by_column)
                if unique_column:
                    data = self.connector.select(
                        self.get_column_values(table, search_by_column)
                    )
                else:
                    pk_column = self.get_primary_key_column(table)
                    data = self.connector.select(
                        self.get_column_values(table, *(pk_column, search_by_column))
                    )
            else:
                search_by_column = self.get_primary_key_column(table)
                data = self.connector.select(
                    self.get_column_values(table, search_by_column)
                )
            values = list(map(lambda row: tuple_to_str(row), data))
            return services.search_page(table, search_by_column, values, **kwargs)
        except Exception as ex:
            print(ex)

    def get_column_values(self, table, *args):
        pass

    def get_new_row_query(self, table: str, page) -> str:
        pass

    def get_columns_names(self, table: str) -> PythonColumns:
        pass

    def check_table_existence(self, table):
        pass

    def validate_context(
        self, table: str, context: ContextParams, columns: PythonColumns
    ):
        pass

    def validate_unique_column(self, table: str, search_by_column: str) -> bool:
        pass

    def get_primary_key_column(self, table):
        pass
