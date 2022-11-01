"""
hackerforms_postgres.client
~~~~~~~~~~~~~~~~~

This module provides a Client object to connect to Postgres Database
"""

from typing import List, Union
from hackerforms.crud.client import Client
from hackerforms.crud.hackerforms_postgres.postgres_connector import PostgresConnector
from hackerforms.crud import services
from hackerforms.crud.exceptions import (
    ContextColumnNotFound,
    PrimaryKeyNotDefined,
    TableColumnsUndefined,
    TableNotFound,
    WrongContextColumnType,
)

from hackerforms.crud.hackerforms_postgres.types import PostgresContraintColumn
from hackerforms.crud.types import ContextParams, PythonColumns

from hackerforms.crud.hackerforms_postgres.sql.expressions import (
    get_columns_contraints,
    insert_new_row,
    table_exists,
    get_columns_and_types,
    get_column_values,
)
from hackerforms.crud.hackerforms_postgres.utils import (
    list_of_tuples_to_dict,
)

from hackerforms.crud.utils import (
    tuple_to_str,
)


class PostgresClient(Client):
    """A Hackerforms postgres Client.

    Provides a new database connection.

    The connection parameters can be specified as a string:
      client = Client("dbname=test user=postgres password=secret")
    or using a set of keyword arguments:
      client = Client(database="test", user="postgres", password="secret")

    The basic connection parameters are:
      - *dbname*: the database name
      - *database*: the database name (only as keyword argument)
      - *user*: user name used to authenticate
      - *password*: password used to authenticate
      - *host*: database host address (defaults to UNIX socket if not provided)
      - *port*: connection port number (defaults to 5432 if not provided)
    """

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
                raise ContextColumnNotFound(table, column)

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
        print("table table", table)
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
