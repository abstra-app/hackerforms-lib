"""
hackerforms.crud.postgres.postgres_connector
~~~~~~~~~~~~~~~~~~~~~~~

This module provides a concrete implementation for Postgres Connector.

"""

import psycopg2
from hackerforms.crud.client import Connector


class PostgresConnector(Connector):
    """Connector implementation for Postgres Data Sources
    It receives the connection parameters from the Client Instance.

    """
    def __init__(self, dsn=None, **kwargs):
        connection: psycopg2.connect = psycopg2.connect(dsn, **kwargs)
        super().__init__(connection)

    def select(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        return output

    def insert(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
