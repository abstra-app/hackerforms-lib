"""
hackerforms_postgres.client
~~~~~~~~~~~~~~~~~

This module provides a Client object to connect to Postgres Database
"""

import psycopg2 as pg
from hackerforms.hackerforms_postgres import services
from hackerforms.hackerforms_postgres.exceptions import ContextColumnNotFound, TableColumnsUndefined, TableNotFound, WrongContextColumnType

from hackerforms.hackerforms_postgres.types import ContextParams, PythonColumns
from hackerforms.hackerforms_postgres.sql.expression import table_exists, get_columns_and_types
from hackerforms.hackerforms_postgres.utils import list_of_tuples_to_dict



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
            py_columns, postgres_columns = self.__get_columns(table)
            if context:
              self.__validate_context(table, context, py_columns)

            return services.new_page(table, postgres_columns, context)

        except pg.Error as ex:
            print(ex)

        except Exception as ex:
            print(ex)

        finally:
          self.cursor.close()

    def __get_columns(self, table: str) -> PythonColumns:
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

    def __validate_context(self, table: str, context: ContextParams, columns: PythonColumns):
      for column, value in context.items():
        if column not in columns.keys():
          raise ContextColumnNotFound(table, column)

        if not isinstance(value, columns[column]):

          raise WrongContextColumnType(table, column, value, columns[column])

      
      