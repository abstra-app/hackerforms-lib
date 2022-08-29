import json
from typing import Dict
from .stdio import stderr_write


def deserialize(string: str) -> Dict:
    try:
        return json.loads(string)
    except Exception as e:
        stderr_write(f"failed to decode json: {string}")
        raise e


def serialize(obj: Dict) -> bytes:
    return bytes(json.dumps(obj), "UTF-8")
