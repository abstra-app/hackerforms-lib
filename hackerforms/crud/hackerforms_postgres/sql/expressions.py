table_exists = (
    lambda table: f"select exists(select relname from pg_class where relname='{table}')"
)

get_columns_and_types = (
    lambda table: f"select column_name, data_type from information_schema.columns where table_name = '{table}';"
)


def get_columns_contraints(table: str) -> str:
    """SQL statement that search all the columns that are unique, primary and foreign keys."""

    return f"""
        SELECT c.table_name, c.column_name, t.table_catalog as database,
        t.table_schema as schema, t.constraint_name as constraint_name, 
        t.constraint_type as constraint_type
            FROM information_schema.table_constraints AS t
                INNER JOIN information_schema.constraint_column_usage AS c
                    ON t.constraint_name = c.constraint_name
                    AND c.constraint_schema = t.table_schema
            WHERE t.constraint_type IN ('UNIQUE', 'PRIMARY KEY', 'FOREIGN KEY' ) 
                AND t.table_name = '{table}';
    """


def get_column_values(table, *args):
    columns = ""
    for arg in args:
        columns += f"{arg},"
    columns = columns[:-1]
    return f"select {columns} from {table}"


def insert_new_row(table, page):
    statement = f"insert into {table}{tuple(page.keys())} "
    statement = statement.replace("'", "")
    statement += f"values {tuple(page.values())}"
    return statement
