from ..input_types import inputs
import json

def test_function():
  fields_metadata = load_metadata()["fields"]
  generated_fields = load_field_examples()
  assert_field_examples_contains_all_fields(generated_fields, fields_metadata)
  for field_example in generated_fields:
    assert_field_exists_in_metadata(field_example, fields_metadata)
    assert_fields_props_are_right(field_example, fields_metadata[field_example["type"]])

def load_metadata():
  with open("./metadata.json") as f:
    return json.load(f)

def load_field_examples():
  return [input.example().json() for input in inputs]

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
  return True

  

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