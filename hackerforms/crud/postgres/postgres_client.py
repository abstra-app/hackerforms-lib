"""
postgres.client
~~~~~~~~~~~~~~~~~

This module provides a Client object to connect to Postgres Database
"""

from typing import List
from hackerforms.crud.client import Client
from hackerforms.crud.postgres.postgres_connector import PostgresConnector
from hackerforms.crud.exceptions import (
    ColumnNotFound,
    PrimaryKeyNotDefined,
    TableColumnsUndefined,
    TableNotFound,
    WrongContextColumnType,
)

from hackerforms.crud.postgres.types import PostgresContraintColumn
from hackerforms.crud.types import ContextParams, PythonColumns

from hackerforms.crud.postgres.sql.expressions import (
    get_columns_contraints,
    insert_new_row,
    table_exists,
    get_columns_and_types,
    get_column_values,
)
from hackerforms.crud.postgres.utils import (
    list_of_tuples_to_dict,
)


class PostgresClient(Client):
    def __init__(self, dsn=None, **kwargs):
        super().__init__(PostgresConnector(dsn, **kwargs))

    def get_column_values(self, table, *args):
        print(table)
        return get_column_values(table, *args)

    def get_new_row_query(table: str, page) -> str:
        return insert_new_row(table, page)

    def get_columns_names(self, table: str) -> PythonColumns:
        columns = self.connector.select(get_columns_and_types(table))
        if len(columns):
            return list_of_tuples_to_dict(columns)
        else:
            raise TableColumnsUndefined(table)

    def check_table_existence(self, table):
        exists = self.connector.select(table_exists(table))[0]
        if not exists:
            raise TableNotFound(table)

    def validate_context(
        self, table: str, context: ContextParams, columns: PythonColumns
    ):
        for column, value in context.items():
            if column not in columns.keys():
                raise ColumnNotFound(table, column)

            if not isinstance(value, columns[column]):

                raise WrongContextColumnType(table, column, value, columns[column])

    def validate_unique_column(self, table: str, search_by_column: str) -> bool:
        data = self.connector.select(get_columns_contraints(table))
        constrained_columns: List[PostgresContraintColumn] = list(
            map(lambda row: PostgresContraintColumn(*row), data)
        )

        column = list(
            filter(
                lambda c: c.column_name == search_by_column
                and c.constraint_type in ("PRIMARY KEY", "UNIQUE"),
                constrained_columns,
            )
        )
        return len(column) > 0

    def get_primary_key_column(self, table) -> PostgresContraintColumn:
        data = self.connector.select(get_columns_contraints(table))
        constrained_columns: List[PostgresContraintColumn] = list(
            map(lambda row: PostgresContraintColumn(*row), data)
        )
        columns: List[PostgresContraintColumn] = list(
            filter(lambda c: c.constraint_type == "PRIMARY KEY", constrained_columns)
        )
        if not columns:
            raise PrimaryKeyNotDefined(table)

        return columns[0].column_name
