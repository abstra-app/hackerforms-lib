table_exists = (
    lambda table: f"select exists(select relname from pg_class where relname='{table}')"
)

get_columns_and_types = (
    lambda table: f"select column_name, data_type from information_schema.columns where table_name = '{table}';"
)
