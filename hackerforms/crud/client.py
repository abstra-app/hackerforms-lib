"""
hackerforms.crud.client
~~~~~~~~~~~~~~~~~~~~~~~

This module provides an abstract class to define the api for users dealing with cruds.

"""

from abc import ABC

from hackerforms.crud.connector import Connector
from hackerforms.crud.exceptions import MissingParameter
from hackerforms.crud.row_page import RowPage
from hackerforms.crud.search_page import SearchPage
from hackerforms.generated.page import Page

class Client(ABC):
    """Abstract class that all client implementations derive from.
    
        Its constructor receives a connector, rowpage and searchpage interfaces.
    """
    def __init__(self, connector: Connector, row_page: RowPage, search_page: SearchPage):
        self.connector = connector
        self.row_page = row_page
        self.search_page = search_page

    def dropdown(self, **kwargs) -> list[dict[str, any]]:
        """Returns a list of dropdown options with primary_key as value and chosen column as label.

            :param `table` kwargs: parameter to inform the table in which the rows will be looked for.
            :param `column` kwargs: paramater to inform the tables' column whose values will populate the dropdown labels.
            :param `primary_key` kwargs: parameter to informs the primary key of the table

            Example::
                >>> supplier_options = db.dropdown(table="suppliers", column="company_name", primary_key='supplier_id')
                >>> supplier = read_dropdown("supplier", options=supplier_options)
        """
        table = kwargs.get("table", None)
        column = kwargs.get("column", None)
        primary_key = kwargs.get("primary_key", None)

        if not table:
            raise MissingParameter("table")
        if not column:
            raise MissingParameter("column")
        if not primary_key:
            raise MissingParameter("primary_key")

        columns = (primary_key, column) if primary_key != column else (primary_key, )
        data = self.connector.select(
            self.get_column_values(table, *columns)
        )
        options = [{"label": col, "value": pk} for (pk, col) in data]

        return options

    def RowPage(self, **kwargs) -> Page:
        """Returns A RowPage instance in which the user can map widgets to table columns for insert new row to database table
        or update an existing row.

        :param `table` kwargs: parameter to inform the table in which the mapping will be done .

        To see examples, go into RowPage class spec.
        """
        table = kwargs.get("table", None)
        if not table:
            raise MissingParameter("table")

        return self.row_page(table, self.connector)

    def SearchPage(self,  **kwargs):
        """Returns A SearchPage instance in which the user can define widgets as filters for searching table rows in database.

        :param `table` kwargs: parameter to inform the table in which the search will be done.

        To see examples, go into SearchPage class spec.
        """
        table = kwargs.get("table", None)
        if not table:
            raise MissingParameter("table")
        

        return self.search_page(table, self.connector)


    def get_column_values(self, table, *args):
        """This class must be implemented by the client implementations and returns a query be used by the connector.
        
        :param `table` kwargs: parameter to inform the table in which the rows will be looked for.
        : param `args`: tuple of columns that are the target of the query.   
        
        """
        pass
