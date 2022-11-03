import psycopg2
from typing import Dict
from hackerforms.crud.client import Connector
from hackerforms.crud.postgres.sql.queries import (
    insert_new_row_query,
    get_column_values_query,
)


class PostgresConnector(Connector):
    def __init__(self, dsn=None, **kwargs):
        self.connection: psycopg2.connect = psycopg2.connect(dsn, **kwargs)

    def select(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        return output

    def insert(self, table: str, data: Dict):
        query = insert_new_row_query(table, data)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
