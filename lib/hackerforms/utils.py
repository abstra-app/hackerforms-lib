import json
from typing import Dict


def deserialize(string: str) -> Dict:
    return json.loads(string)


def serialize(obj: Dict) -> bytes:
    return bytes(json.dumps(obj), 'UTF-8')
