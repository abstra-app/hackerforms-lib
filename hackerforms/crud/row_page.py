"""
hackerforms.crud.row_page
~~~~~~~~~~~~~~~~~~~~~~~

This module provides a base class for all the row page implementations.

"""


from typing import Dict

from hackerforms.crud.crud_page import CRUDPage


class RowPage(CRUDPage):
    """Base class for the concrete row page implementations

    Its constructor receives the target table (or entity in api)
    and the the connector to manipulate data source

    TODO::
        - update of a table's row value

    """

    def __init__(self, table, connector):
        super().__init__()
        self.connector = connector
        self.table = table

    def insert(self, **kwargs):
        """It returns the page instance with the form for user submitting
        a new row value for inserting in the table

        :param `context` kwargs: a dict with values that must be inserted within the row. Its keys are column names and the values are the respective data to be inserted. Be aware that all columns set here override columns if the same are set mapping to the widgets form.

         Example::

                >>> categories = db.dropdown(table="categories", column="category_name", primary_key='category_id') # [{'label': 'category_name', 'value': 'category_id'}]
                >>> suppliers = db.dropdown(table="suppliers", column="company_name", primary_key='supplier_id')
                >>> page = (
                ...    db.RowPage(table="products")
                ...     .read_dropdown("category", options=categories, column="category_id")
                ...     .read_dropdown("supplier", options=suppliers, column="supplier_id")
                ...     .read("product name", key="product_name", column="product_name")
                ...     .read_number("quantity per unit", column="quantity_per_unit")
                ...     .read_currency("unit price", column="unit_price")
                ...     .read_number("units in stock", column="units_in_stock")
                ...     .read_number("units in order", column="units_on_order")
                ...     .read_number("discontinued", column="discontinued")
                ...     .insert(context={"product_id": 811, })
                ... )

            Note: primary keys generations are not currently handled by hackerforms package, so
            it must be generated and provided in the context in case of its value not be handled
            by the data source.

            TODO::
                - deal primary key colision
                - abstract primary key generation as option
        """

        context = kwargs.get("context", None)

        page = self.page.run()
        data = {self.column_from_key[key]: value for (key, value) in page.items()}

        if context:
            data = {**data, **context}

        insert_query = self.get_insert_data_query(self.table, data)
        self.connector.insert(insert_query)
        return page

    def get_insert_data_query(self, table: str, data: Dict[str, any]):
        """Abstract method that returns insert data query"""
        pass
