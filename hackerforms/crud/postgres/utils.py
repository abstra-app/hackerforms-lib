from datetime import date, datetime, timedelta
from time import time
from typing import List, Tuple
import decimal
import uuid

from hackerforms.crud.postgres.types import (
    PostgresColumnType,
    PostgresColumns,
)
from hackerforms.crud.types import PythonColumns

postgres_to_py_columns = {
    "NULL": None,
    "bool": bool,
    "real": float,
    "double": float,
    "smallint": int,
    "integer": int,
    "bigint": int,
    "numeric": decimal.Decimal,
    "varchar": str,
    "character varying": str,
    "text": str,
    "bytea": bytes,
    "date": date,
    "time": time,
    "timestamp": datetime,
    "timestampz": datetime,
    "interval": timedelta,
    "ARRAY": list,
    "hstore": dict,
    "json": any,
    "uuid": uuid.UUID,
}


widget_from_column_type = {
    "bool": "",
    "real": "read_number",
    "double": "read_number",
    "smallint": "read_number",
    "integer": "read_number",
    "bigint": "read_number",
    "numeric": "read_number",
    "varchar": "read",
    "character varying": "read",
    "text": "read_textarea",
    "bytea": "read_file",
    "date": "read_date",
    "time": "read_time",
    "timestamp": "read_time",
    "timestampz": "read_time",
    "interval": "",
    "ARRAY": "",
    "hstore": "",
    "json": "",
    "uuid": "read",
}


def list_of_tuples_to_dict(
    tuples: List[PostgresColumnType],
) -> Tuple[PythonColumns, PostgresColumns]:
    return {tup[0]: convert_postgres_column_type_to_python(tup[1]) for tup in tuples}, {
        tup[0]: tup[1] for tup in tuples
    }
