###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################
import json
import os
from .metadata import metadata


def types_compatible(prop, schema):
    if type(schema["type"]) == list:
        return any(
            types_compatible(prop, {**schema, "type": type}) for type in schema["type"]
        )

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


def validate_widget_props(widget_example):
    metadata_widget = metadata[widget_example["type"]]
    for prop in metadata_widget["params"]:
        if not prop in widget_example:
            raise Exception(f"{prop} not in {widget_example.keys()}")
        assert types_compatible(widget_example[prop], metadata_widget["params"][prop])
    for prop in metadata_widget["optionals"]:
        if not prop in widget_example:
            raise Exception(f"{prop} not in {widget_example.keys()}")
        if not (
            widget_example[prop] is None
            or types_compatible(
                widget_example[prop], metadata_widget["optionals"][prop]
            )
        ):
            raise Exception(
                f"{widget_example[prop]}: {type(widget_example[prop])} is not compatible with {metadata_widget['optionals'][prop]}"
            )
    for prop in widget_example:
        if prop == "type":
            continue
        if not (
            prop in metadata_widget["params"] or prop in metadata_widget["optionals"]
        ):
            raise Exception(
                f'{prop} not in {metadata_widget["params"].keys()} nor {metadata_widget["optionals"].keys()}'
            )
