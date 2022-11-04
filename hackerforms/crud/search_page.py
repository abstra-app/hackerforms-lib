"""
hackerforms.crud.search_page
~~~~~~~~~~~~~~~~~~~~~~~

This module provides a base class for all the search page implementations.

"""

import pandas as pd

from hackerforms.crud.crud_page import CRUDPage
from hackerforms.generated.page import Page


class SearchPage(CRUDPage):
    """Base class for the concrete search page implementations

    Its constructor receives the target table (or entity in api)
    and the the connector to search for rows in data source

    TODO:
        - to provide a way of searching based on relationship tables
    """

    def __init__(self, table, connector):
        super().__init__()
        self.connector = connector
        self.table = table

    def search(self, **kwargs):
        """It returns the page instance with the filter fields defined by the user and a selectable table rows listing search results.


        :param `context` kwargs: a dict with values that must be set as filter by default. Its keys are column names and the values are the respective data to bet set as filter. Be aware that all columns set here override widget filters if the same ones are mapping to the widgets filters.
        :param `display_columns`: table columns to list in results

        Example::

            >>>  product = (db.SearchPage(table="products")
            ...           .read("Product Name", column="product_name")
            ...           .search(display_columns=['product_id', 'product_name', 'unit_price', 'discontinued']))


        TODO:
          - param `multiple` kwargs : if the user can choose multiple rows from the results

        NOTES:
          - It uses the realtime widget for reactive update of table results.

        """
        self.context = kwargs.get("context", None)
        self.display_columns = kwargs.get("display_columns", None)

        return self.page.realtime(self.search_func).run()

    def search_func(self, filters):
        """Callback function that is passed as parameter to the realtime widget.
        This function builds the query every time the filters are updated and returns a new dataframe widget.

        :param `filters` args: dict with the updated filters values.

        """
        query = self.build_search_query(filters)
        if not query:
            return Page().display("Fill the filters above")

        data = self.connector.select(query)
        df = pd.DataFrame.from_records(data, columns=self.display_columns)
        return Page().read_pandas_row_selection(df, full_width=True)

    def build_search_query(self, filters) -> str:
        """Abstract method for building the search query"""
        pass
