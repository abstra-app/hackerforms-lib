from typing import List
from hackerforms import Page
from abc import ABC


class PageBuilder(ABC):
    def __init__(self, table_name):
        self._page = "Page()\\\n"
        self.table_name = table_name

    def add_title(self):
        self._page += f"  .display('{self.table_name}')\\\n"
        return self

    def close(self):
        self._page += f"  .run()"

    @property
    def page(self):
        return self._page

    def eval_page(self):
        return eval(self.page)


class NewPageBuilder(PageBuilder):
    def __init__(self, table_name):
        super().__init__(table_name)
        self.add_title()

    def add_widget(self, widget, key):
        self._page += f"  .{widget}('{key}')\\\n"

    @staticmethod
    def createPage(table_name: str):
        return NewPageBuilder(table_name)


class SearchPageBuilder(PageBuilder):
    def __init__(self, table_name: str, search_by: str, values: List):
        super().__init__(table_name)
        self.search_by = search_by
        self.values = values
        self.add_title().add_dropdown().close()

    def add_dropdown(self):
        self._page += f"  .read_dropdown('{self.search_by}', options={self.values})\\\n"
        return self

    @staticmethod
    def createPage(table_name: str, search_by: str, values: List):
        return SearchPageBuilder(table_name, search_by, values)
