def get_column_values_query(table, *args):
    columns = ""
    for arg in args:
        columns += f"{arg},"
    columns = columns[:-1]
    return f"select {columns} from {table}"


def insert_new_row_query(table, page):
    query = f"insert into {table}{tuple(page.keys())} "
    query = query.replace("'", "")
    query += f"values {tuple(page.values())}"
    return query
