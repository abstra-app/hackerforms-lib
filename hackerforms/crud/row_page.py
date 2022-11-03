from hackerforms.generated.page import Page


class RowPage:
    def __init__(self, table, connector):
        self.table = table
        self.page = Page()
        self.column_from_key = {}
        self.connector = connector

    def __validate_args(self, *args, **kwargs):
        column = kwargs.get("column", None)
        if not column or not args:
            raise Exception

    def __add_to_column_map(self, *args, **kwargs):
        key = kwargs.get("key", None) or args[0]
        column = kwargs.get("column")
        self.column_from_key[key] = column

    def read(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read(*args, **kwargs)
        return self

    def read_code(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_code(*args, **kwargs)
        return self

    def read_currency(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_currency(*args, **kwargs)
        return self

    def read_date(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_date(*args, **kwargs)
        return self

    def read_dropdown(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_dropdown(*args, **kwargs)
        return self

    def read_email(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_email(*args, **kwargs)
        return self

    def read_file(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_file(*args, **kwargs)
        return self

    def read_html_list(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_html_list(*args, **kwargs)
        return self

    def read_image(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_image(*args, **kwargs)
        return self

    def read_list(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_list(*args, **kwargs)
        return self

    def read_multiple_choice(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_multiple_choice(*args, **kwargs)
        return self

    def read_nps(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_nps(*args, **kwargs)
        return self

    def read_number(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_number(*args, **kwargs)
        return self

    def read_pandas_row_selection(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_pandas_row_selection(*args, **kwargs)
        return self

    def read_password(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_password(*args, **kwargs)
        return self

    def read_phone(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_phone(*args, **kwargs)
        return self

    def read_tag(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_tag(*args, **kwargs)
        return self

    def read_textarea(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_textarea(*args, **kwargs)
        return self

    def read_time(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_time(*args, **kwargs)
        return self

    def read_video(self, *args, **kwargs):
        self.__validate_args(*args, **kwargs)
        self.__add_to_column_map(*args, **kwargs)
        self.page = self.page.read_video(*args, **kwargs)
        return self

    def insert(self, **kwargs):
        context = kwargs.get("context", None)

        page = self.page.run()
        data = {self.column_from_key[key]: value for (key, value) in page.items()}

        if context:
            data = {**data, **context}
        self.connector.insert(self.table, data)
        return page
