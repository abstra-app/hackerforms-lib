"""
postgres.client
~~~~~~~~~~~~~~~~~

This module provides a Client object to connect to Postgres Database
"""

from typing import List
from hackerforms.crud.client import Client
from hackerforms.crud.postgres.postgres_connector import PostgresConnector
from hackerforms.crud.exceptions import (
    PrimaryKeyNotDefined,
    TableNotFound,
)

from hackerforms.crud.postgres.types import PostgresContraintColumn

from hackerforms.crud.row_page_factory import row_page_factory

from hackerforms.crud.postgres.sql.queries import (
    get_columns_contraints_query,
    table_exists,
    get_column_values_query,
)


class PostgresClient(Client):
    def __init__(self, dsn=None, **kwargs):
        row_page = row_page_factory("postgres")
        super().__init__(PostgresConnector(dsn, **kwargs), row_page)

    def get_column_values(self, table, *args):
        return get_column_values_query(table, *args)

    def check_table_existence(self, table):
        exists = self.connector.select(table_exists(table))[0]
        if not exists:
            raise TableNotFound(table)

    def get_primary_key_column(self, table) -> PostgresContraintColumn:
        data = self.connector.select(get_columns_contraints_query(table))
        constrained_columns: List[PostgresContraintColumn] = list(
            map(lambda row: PostgresContraintColumn(*row), data)
        )
        columns: List[PostgresContraintColumn] = list(
            filter(lambda c: c.constraint_type == "PRIMARY KEY", constrained_columns)
        )
        if not columns:
            raise PrimaryKeyNotDefined(table)

        return columns[0].column_name
