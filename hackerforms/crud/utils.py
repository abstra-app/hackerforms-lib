from typing import Tuple


def tuple_to_str(tuple: Tuple, sep="-") -> str:
    cast_values = list(map(lambda val: str(val), tuple))
    return f"{sep}".join(cast_values)
