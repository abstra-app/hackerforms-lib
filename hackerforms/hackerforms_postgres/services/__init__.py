from typing import Union
from hackerforms.hackerforms_postgres.services.page_builder import NewPageBuilder
from hackerforms.hackerforms_postgres.types import ContextParams, PostgresColumns
from hackerforms.hackerforms_postgres.utils import widget_from_column_type



def new_page(table_name: str, colums: PostgresColumns, context: Union[ContextParams, None]):
  page_builder = NewPageBuilder.createPage(table_name)
  for name, _type in colums.items():
    page_builder.add_widget(widget_from_column_type[_type], name)
  page_builder.close()
  page = page_builder.eval_page()
  print(page)
  
