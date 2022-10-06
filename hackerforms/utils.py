import os
import json
from typing import Dict


def deserialize(string: str) -> Dict:
    return json.loads(string)


def serialize(obj: Dict) -> bytes:
    return bytes(json.dumps(obj, allow_nan=False), "UTF-8")

def persist_session_id(session_id: str):
    if os.getenv('ENV') == 'e2e' and os.getenv("E2EPATH"):
        with open(f'{os.getenv("E2EPATH")}/session-id.txt', 'w') as f:
            f.write(session_id)