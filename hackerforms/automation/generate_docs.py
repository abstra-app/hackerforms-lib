import os
import json
import inspect
from parser.generate_functions import (
    filter_classes,
    inspect_answer_docs,
    inspect_init_docs,
)
from parser.helpers import get_function_name
import parser.docs_parser as DocsParser
from hackerforms import input_types, output_types

EXAMPLES_PATH = "./abstra-lib/hackerforms/automation/examples"
DOCS_WIDGETS_PATH = "./docs/src/metadata/widgets.json"


def build_widget_metadata(widget_type):
    """This function return ans object with __init__ constructor signature as dict, its docs as string and convert_answer method's docs"""

    _class = widget_type[1]

    for method in inspect.getmembers(_class):
        if "__init__" in method[0]:
            parsed = DocsParser.parse(inspect_init_docs(method))

        if "convert_answer" in method[0]:
            answer_docstring = DocsParser.parse(inspect_answer_docs(method))
            parsed.concat_meta(meta=answer_docstring.meta)

    if not parsed:
        return {}

    metadata = parsed.to_dict()
    metadata["widget_name"] = widget_type[0]

    metadata["type"] = list(
        filter(lambda x: x[0] == "type", inspect.getmembers(_class))
    )[0][1]

    return metadata


def generate_widget_docs(widget_types, postfix):
    widgets_docs = {}

    for widget_type in widget_types:
        function_name = get_function_name(widget_type[0], postfix)
        widget_docs = {}

        # Temporary workaround to deal with function names that don't follow the standard
        if function_name == "read_text" or function_name == "display_text":
            function_name = function_name.replace("_text", "")

        examples = getExampleFromFiles(function_name)

        if examples is None:
            print(
                f"No examples directory found for '{function_name}'. Skipping from docs."
            )
            continue

        widget_docs = build_widget_metadata(widget_type)
        widget_docs["examples"] = examples

        widgets_docs[function_name] = widget_docs

    return widgets_docs


def generate_docs():
    input_classes = inspect.getmembers(input_types, inspect.isclass)
    output_classes = inspect.getmembers(output_types, inspect.isclass)

    input_widget_types = filter_classes(input_classes, "Input")
    output_widget_types = filter_classes(output_classes, "Output")

    docs_metadata = {
        "outputs": generate_widget_docs(output_widget_types, "Output"),
        "inputs": generate_widget_docs(input_widget_types, "Input"),
    }

    json_data = json.dumps(docs_metadata, indent=2)
    save(json_data)


def save(data):
    f = open(DOCS_WIDGETS_PATH, "w")
    f.write(data)
    f.close()


def getExampleFromFiles(function_name):
    try:
        file_list = os.listdir(f"{EXAMPLES_PATH}/{function_name}")
    except:
        return None

    examples = []

    try:
        for example_file in file_list:
            example_key = example_file.split(".")[0]

            example = None
            for example_dict in examples:
                if "key" in example_dict and example_dict["key"] == example_key:
                    example = example_dict
                    break

            if example is None:
                example = {"key": example_key}
                examples.append(example)

            if ".py" in example_file:
                f = open(f"{EXAMPLES_PATH}/{function_name}/{example_file}", "r")
                example["code"] = f.read()
            elif ".json" in example_file:
                f = open(f"{EXAMPLES_PATH}/{function_name}/{example_file}", "r")
                json_dict = json.load(f)
                example.update(json_dict)

    except Exception as error:
        print(f"Error reading example files for '{function_name}'")
        print(error)

    return examples


if __name__ == "__main__":
    generate_docs()
