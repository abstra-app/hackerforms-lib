from typing import Dict, List
import re


def camel_to_snake(sentence):
    """This function converts a CamelCase class name to snake_case.
    The class name must start with capitalized letter.
    Cases like HTMLCaseName is converted into html_case_name.
    """

    snake = ""
    if sentence.isupper():
        snake = sentence.lower()
    else:
        word = ""
        current = 0
        while current < len(sentence) - 1:
            if sentence[current].isupper() and sentence[current + 1].isupper():
                while sentence[current].isupper() and sentence[current + 1].isupper():
                    word += sentence[current].lower()
                    current += 1
                if current >= 2:
                    snake += word
                    word = ""
                    if current < len(sentence) - 1:
                        snake += "_"
            elif sentence[current].isupper():
                word += sentence[current].lower()
                current += 1
                while current < len(sentence) and sentence[current].islower():
                    word += sentence[current]
                    current += 1
                snake += word

                word = ""
                if current < len(sentence) - 1:
                    snake += "_"

            else:
                raise Exception(
                    "The class name does not follow camel case pattern. Please, rename you widget type class name."
                )

    return snake


def get_default_key(method_signature_params: Dict[str, str]) -> str:
    """This function looks for a parameter of type string differente of key to be used as default key
    in page methods

    """
    for param, type in method_signature_params.items():

        if param != "key" and type == "str":
            return param
    return '"result"'


def get_method_signature(annotations: Dict[str, str]) -> Dict[str, str]:
    """This function extract the type of each parameter in method signature and returns
     a dict with param name as key and type as value


    Positional Arg:
      annotations
      Example:  {'key': <class 'str'>, 'name': <class 'str'>, 'options': typing.Union[typing.List[str], typing.List[typing.Dict]]}

    Returns:
      Example: {'key': 'str', 'name': 'str', 'options': 'typing.Union[typing.List[str], typing.List[typing.Dict]]'}

    """

    params = {}
    primitive_pattern = r"<class '(.*)'>"

    for param, type_obj in annotations.items():
        match_primitive = re.search(primitive_pattern, str(type_obj))
        if match_primitive:
            _type = match_primitive.groups()[0]
        else:
            _type = str(type_obj)

        params[param] = _type

    return params


def get_function_name(class_name, postfix="Input"):
    """This function converts a widget type class name to a input, output equivalent function name or page method name.
    It basically removes the Input or Output postfix, turns the string into snake and append read_ ou display_ at the beginning.

    """
    pattern = re.search(f"(.+){postfix}", class_name)
    if not pattern:
        return None

    matched = pattern.groups()[0]
    snake = camel_to_snake(matched)

    if postfix == "Input":
        return "read_" + snake
    else:
        return "display_" + snake


def filter_classes(classes, postfix: str) -> List:
    """This functions gets all Input and Output widgets
    classes and returns a list of tuples (classs_name, class)

    """
    widget_types = []
    for class_ in classes:
        z = re.match(f".+{postfix}", class_[0])
        if z:
            widget_types.append(class_)

    return widget_types
