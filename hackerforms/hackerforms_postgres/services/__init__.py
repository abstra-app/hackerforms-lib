from typing import List, Union
from hackerforms.generated.page import Page
from hackerforms.hackerforms_postgres.services.page_builder import (
    NewPageBuilder,
    SearchPageBuilder,
)
from hackerforms.hackerforms_postgres.types import (
    ContextParams,
)
from hackerforms.hackerforms_postgres.utils import widget_from_column_type


def new_page(table_metadata: any, context: Union[ContextParams, None]
) -> Page:
    table_name = table_metadata['table_name']
    columns = table_metadata['columns']
    primary_key = table_metadata['primary_key']

    page_builder = NewPageBuilder.createPage(table_name)
    for name, _type in columns.items():
      if name not in context and name != primary_key:
          page_builder.add_widget(widget_from_column_type[_type], name)
    page_builder.close()
    page: Page = page_builder.eval_page()
    return page


def search_page(
    table_name: str, search_by_column: str, values: List, **kwargs
) -> Union[str, int]:
    page_builder = SearchPageBuilder.createPage(table_name, search_by_column, values)
    page: Page = page_builder.eval_page()
    return page[search_by_column]
