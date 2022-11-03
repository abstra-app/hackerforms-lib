from typing import Dict

from hackerforms.crud.row_page import RowPage
from hackerforms.crud.postgres.sql.queries import insert_new_row_query


class PostgresRowPage(RowPage):
    def __init__(self, table, insert_method):
        super().__init__(table, insert_method)

    def insert_data(self, table: str, data: Dict[str, any]):
        query = insert_new_row_query(table, data)
        self.connector.insert(query)