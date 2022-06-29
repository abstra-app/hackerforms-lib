import json
import os
from .example_instances import example_instances

METADATA_FILEPATH = os.path.join(os.path.dirname(__file__), 'metadata.json')

def test_function():
    widgets_metadata = load_metadata()["widgets"]
    del widgets_metadata["list-input"]
    generated_widgets = load_widget_test_instances()
    assert_widget_examples_contains_all_widgets(
        generated_widgets, widgets_metadata)
    for widget_example in generated_widgets:
        assert_widget_exists_in_metadata(widget_example, widgets_metadata)
        assert_widgets_props_are_right(
            widget_example, widgets_metadata[widget_example["type"]])

def load_metadata():
    with open(METADATA_FILEPATH) as f:
        return json.load(f)


def load_widget_test_instances():
    return [example_instance.json() for example_instance in example_instances]


def assert_widget_exists_in_metadata(widget_example, widgets_metadata):
    assert widget_example["type"] in widgets_metadata


def assert_widgets_props_are_right(widget_example, metadata_widget):
    for prop in metadata_widget['params']:
        assert prop in widget_example
        assert types_compatible(widget_example[prop], metadata_widget['params'][prop])
    for prop in metadata_widget['optionals']:
        assert prop in widget_example
        assert types_compatible(widget_example[prop], metadata_widget['optionals'][prop])
    for prop in widget_example:
        if prop == "type":
            continue
        assert prop in metadata_widget['params'] or prop in metadata_widget['optionals']


def types_compatible(prop, schema):
    if type(schema["type"]) == list:
        return any(types_compatible(prop, {**schema, "type": type}) for type in schema["type"])

    if schema["type"] == "string":
        return type(prop) == str
    if schema["type"] == "number":
        return type(prop) == int or type(prop) == float
    if schema["type"] == "boolean":
        return type(prop) == bool
    if schema["type"] == "array":
        return type(prop) == list
    if schema["type"] == "object":
        return type(prop) == dict
    if schema["type"] == "null":
        return prop == None
    if schema["type"] == "any":
        return True
    raise Exception(f"Unknown type: {schema['type']}")


def to_generic_type(type):
    if type == str:
        return "string"
    if type == int:
        return "number"
    if type == bool:
        return "boolean"
    if type == list:
        return "array"
    if type == dict:
        return "object"
    if type == None:
        return "null"
    raise Exception(f"Unknown type: {type}")


def assert_widget_examples_contains_all_widgets(generated_widgets, widgets_metadata):
    for widget_type in widgets_metadata:
        if widget_type != "list-input":
            assert any(widget["type"] == widget_type for widget in generated_widgets if widget["type"] != "list-input")
