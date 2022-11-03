from typing import Tuple
from collections import namedtuple


PostgresColumnType = Tuple[str, str]
PostgresColumns = dict[str, str]

PostgresContraintColumn = namedtuple(
    "PostgresContraintColumn",
    [
        "table_name",
        "column_name",
        "database_name",
        "schema_name",
        "constraint_name",
        "constraint_type",
    ],
)
