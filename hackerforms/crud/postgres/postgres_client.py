"""
hackerforms.crud.postgres.postgres_client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides a concrete implementation for Postgres Client.
"""


from hackerforms.crud.client import Client
from hackerforms.crud.postgres.postgres_connector import PostgresConnector
from hackerforms.crud.page_factory import page_factory
from hackerforms.crud.postgres.sql.queries import get_column_values_query


class PostgresClient(Client):
    """Client Implementation for Postgres Data Sources

    To instantiate, it's required the database connection parameters, whose can be specified as a string:
        >>> db = PostgresClient("dbname=test user=postgres password=secret")
    or using a set of keyword arguments:
        >>> db = PostgresClient(database="test", user="postgres", password="secret")

    Or as a mix of both. The basic connection parameters are:
    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)

    """

    def __init__(self, dsn=None, **kwargs):
        row_page, search_page = page_factory("postgres")
        connector = PostgresConnector(dsn, **kwargs)
        super().__init__(connector, row_page, search_page)

    def get_column_values(self, table, *args):
        return get_column_values_query(table, *args)
