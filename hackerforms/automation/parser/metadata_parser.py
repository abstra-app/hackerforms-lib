import json
import os


METADATA_FILEPATH = os.path.join(
    os.path.dirname(__file__), "..", "tests", "metadata.json"
)


def load_widget_metadata():
    with open(METADATA_FILEPATH) as f:
        widgets = json.load(f)["widgets"]
        return widgets
