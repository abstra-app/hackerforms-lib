
"""
hackerforms.crud.postgres.postgres_row_page
~~~~~~~~~~~~~~~~~~~~~~~

This module provides a concrete implementation for Postgres Row Page.

"""

from typing import Dict

from hackerforms.crud.row_page import RowPage
from hackerforms.crud.postgres.sql.queries import insert_new_row_query


class PostgresRowPage(RowPage):
    """RowPage implementation for Postgres Data Sources
    It receives the table and connector instances from the client.

    """
    def __init__(self, table, connector):
        super().__init__(table, connector)

    def get_insert_data_query(self, table: str, data: Dict[str, any]):
        return insert_new_row_query(table, data)
