"""
hackerforms_postgres.client
~~~~~~~~~~~~~~~~~

This module provides a Client object to connect to Postgres Database
"""

import random
from typing import List, Union
import psycopg2 as pg
from hackerforms.hackerforms_postgres import services
from hackerforms.hackerforms_postgres.exceptions import (
    ContextColumnNotFound,
    PrimaryKeyNotDefined,
    TableColumnsUndefined,
    TableNotFound,
    WrongContextColumnType,
)

from hackerforms.hackerforms_postgres.types import (
    ContextParams,
    PostgresContraintColumn,
    PythonColumns,
)
from hackerforms.hackerforms_postgres.sql.expression import (
    get_columns_contraints,
    insert_new_row,
    table_exists,
    get_columns_and_types,
    get_column_values,
)
from hackerforms.hackerforms_postgres.utils import list_of_tuples_to_dict, tuple_to_str


class Client:
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
        self.client: pg.connect = pg.connect(dsn, **kwargs)

    def insert_page(self, table: str, context: ContextParams = None):
        try:
            self.cursor = self.client.cursor()
            self.__check_table_existence(table)
            py_columns, postgres_columns = self.__get_columns_names(table)
            
            if context:
                self.__validate_context(table, context, py_columns)
            
            primary_key_column = self.__get_primary_key_column(table)
            page = services.new_page({'table_name': table, 'primary_key': primary_key_column, 'columns': postgres_columns} , context)
            page[primary_key_column] = random.randint(20, 100)
            page = {**page, **context}
            self.cursor.execute(insert_new_row(table, page))
            self.client.commit()
            return page
        except pg.Error as ex:
            print(ex)

        except Exception as ex:
            print(ex)

        finally:
            self.cursor.close()

    def search_page(self, table: str, **kwargs) -> Union[str, int]:
        search_by_column = kwargs.get("search_by", None)
        try:
            self.cursor = self.client.cursor()
            self.__check_table_existence(table)
            if search_by_column:
                unique_column = self.__validate_unique_column(table, search_by_column)
                if unique_column:
                    self.cursor.execute(get_column_values(table, search_by_column))
                else:
                    pk_column = self.__get_primary_key_column(table)
                    self.cursor.execute(
                        get_column_values(table, *(pk_column, search_by_column))
                    )
            else:
                search_by_column = self.__get_primary_key_column(table)
                self.cursor.execute(get_column_values(table, search_by_column))
            values = list(map(lambda row: tuple_to_str(row), self.cursor.fetchall()))
            return services.search_page(table, search_by_column, values, **kwargs)
        except Exception as ex:
            print(ex)
        finally:
            self.cursor.close()

    def __get_columns_names(self, table: str) -> PythonColumns:
        self.cursor.execute(get_columns_and_types(table))
        columns = self.cursor.fetchall()
        if len(columns):
            return list_of_tuples_to_dict(columns)
        else:
            raise TableColumnsUndefined(table)

    def __check_table_existence(self, table):
        self.cursor.execute(table_exists(table))
        exists = self.cursor.fetchone()[0]
        if not exists:
            raise TableNotFound(table)

    def __validate_context(
        self, table: str, context: ContextParams, columns: PythonColumns
    ):
        for column, value in context.items():
            if column not in columns.keys():
                raise ContextColumnNotFound(table, column)

            if not isinstance(value, columns[column]):

                raise WrongContextColumnType(table, column, value, columns[column])

    def __validate_unique_column(self, table: str, search_by_column: str) -> bool:
        self.cursor.execute(get_columns_contraints(table))
        constrained_columns: List[PostgresContraintColumn] = list(
            map(lambda row: PostgresContraintColumn(*row), self.cursor.fetchall())
        )
        column = list(
            filter(
                lambda c: c.column_name == search_by_column
                and c.constraint_type in ("PRIMARY KEY", "UNIQUE"),
                constrained_columns,
            )
        )
        return len(column) > 0

    def __get_primary_key_column(self, table) -> PostgresContraintColumn:
        self.cursor.execute(get_columns_contraints(table))
        constrained_columns: List[PostgresContraintColumn] = list(
            map(lambda row: PostgresContraintColumn(*row), self.cursor.fetchall())
        )
        columns: List[PostgresContraintColumn] = list(
            filter(lambda c: c.constraint_type == "PRIMARY KEY", constrained_columns)
        )
        if not columns:
            raise PrimaryKeyNotDefined(table)

        return columns[0].column_name
