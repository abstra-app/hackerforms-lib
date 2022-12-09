import os
import json
import webbrowser

from typing import Dict


def deserialize(string: str) -> Dict:
    return json.loads(string)


def serialize(obj: Dict) -> bytes:
    return bytes(json.dumps(obj, allow_nan=False), "UTF-8")


def persist_session_id(session_id: str):
    if os.getenv("ENV") == "e2e" and os.getenv("E2EPATH"):
        with open(f'{os.getenv("E2EPATH")}/session-id.txt', "w") as f:
            f.write(session_id)


def open_browser(frontend_host, session_id):
    if os.getenv("ENV") != "e2e":
        url = f"{frontend_host}/local/{session_id}"
        if not webbrowser.open(url):
            print(f"Open your browser at: {url}")


def get_single_value(answer: Dict):
    return list(answer.values())[0]
