from hackerforms.crud.row_page import RowPage


class PostgresRowPage(RowPage):
    def __init__(self, table, insert_method):
        super().__init__(table, insert_method)
