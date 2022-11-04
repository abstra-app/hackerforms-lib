from hackerforms.crud.search_page import SearchPage


class PostgresSearchPage(SearchPage):
    def __init__(self, table, connector):
        super().__init__(table, connector)

    def build_search_query(self, filters):
        query = f"select "
        for column in self.display_columns:
            query += f"{column}, "
        query = query[:-2]
        query += f" from {self.table} where "

        filter_keys_with_nonempty_values = [
            key
            for key in filters
            if filters.get(key) != "" and key in self.column_from_key.keys()
        ]
        if len(filter_keys_with_nonempty_values) == 0:
            return None
        for i, key in enumerate(filter_keys_with_nonempty_values):
            value = filters.get(key)
            if i < len(filter_keys_with_nonempty_values) - 1:
                query += f"{self.column_from_key[key]} like '%{value}%' and "
            else:
                query += f"{self.column_from_key[key]} like '%{value}%';"

        return query