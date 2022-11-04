"""
hackerforms.crud.page_factory
~~~~~~~~~~~~~~~~~~~~~~~

This module provides an abstract factory for crud pages.

"""

from hackerforms.crud.postgres.postgres_row_page import PostgresRowPage
from hackerforms.crud.postgres.postgres_search_page import PostgresSearchPage


def page_factory(name: str):
    """returns a list of concrete implementations of all the related
    crud pages
    """

    if name == "postgres":
        return [PostgresRowPage, PostgresSearchPage]

    raise NotImplementedError
