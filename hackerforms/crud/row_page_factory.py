from hackerforms.crud.postgres.postgres_row_page import PostgresRowPage


def row_page_factory(name: str):

    if name == "postgres":
        return PostgresRowPage

    raise NotImplementedError
