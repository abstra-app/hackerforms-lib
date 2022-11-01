from typing import Dict, Tuple, Union


ContextParam = Union[str, bool, int, float]
ContextParams = Dict[str, ContextParam]

PostgresColumnType = Tuple[str, str]
PythonColumns = dict[str, str]
PostgresColumns = dict[str, str]
