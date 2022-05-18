import json
import os
from .example_instances import example_instances

METADATA_FILEPATH = os.path.join(os.path.dirname(__file__), 'metadata.json')


def test_function():
    fields_metadata = load_metadata()["fields"]
    generated_fields = load_field_test_instances()
    assert_field_examples_contains_all_fields(
        generated_fields, fields_metadata)
    for field_example in generated_fields:
        assert_field_exists_in_metadata(field_example, fields_metadata)
        assert_fields_props_are_right(
            field_example, fields_metadata[field_example["type"]])


def load_metadata():
    with open(METADATA_FILEPATH) as f:
        return json.load(f)


def load_field_test_instances():
    return [example_instance.json() for example_instance in example_instances]


def assert_field_exists_in_metadata(field_example, fields_metadata):
    assert field_example["type"] in fields_metadata


def assert_fields_props_are_right(field_example, field_metadata):
    for prop in field_metadata:
        assert prop in field_example
        assert types_compatible(field_example[prop], field_metadata[prop])
    for prop in field_example:
        if prop == "type":
            continue
        assert prop in field_metadata


def types_compatible(prop, schema):
    if type(schema["type"]) == list:
        print(prop, schema)
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
        return type(prop) == None
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


def assert_field_examples_contains_all_fields(generated_fields, fields_metadata):
    for field_type in fields_metadata:
        assert any(field["type"] == field_type for field in generated_fields)
