from typing import Dict, Tuple, Union
from collections import namedtuple

ContextParam = Union[str, bool, int, float]
ContextParams = Dict[str, ContextParam]

PostgresColumnType = Tuple[str, str]
PythonColumns = dict[str, str]
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
