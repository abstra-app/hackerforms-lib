from hackerforms.crud.client import Client
from hackerforms.crud.postgres.postgres_connector import PostgresConnector
from hackerforms.crud.page_factory import page_factory
from hackerforms.crud.postgres.sql.queries import get_column_values_query

class PostgresClient(Client):
    def __init__(self, dsn=None, **kwargs):
        row_page, search_page = page_factory("postgres")
        connector = PostgresConnector(dsn, **kwargs)
        super().__init__(connector, row_page, search_page)

    def get_column_values(self, table, *args):
        return get_column_values_query(table, *args)


