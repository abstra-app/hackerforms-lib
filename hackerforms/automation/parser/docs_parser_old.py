from typing import Dict, List, Optional

POSITIONAL_ARGS_SECTION = "Positional Args:"
KEYWORD_ARGS_SECTION = "Keyword Args:"


def group_docs_by_section(docs: str) -> Dict[str, str]:
    description, positional_arguments, keyword_arguments = get_docs_sections(
        parse_docs(docs)
    )

    return {
        "description": description,
        "positional_arguments": positional_arguments,
        "keyword_arguments": keyword_arguments,
    }


def parse_docs(docs: str) -> List[str]:
    try:
        return remove_empty_lines(strip_docs(docs.splitlines()))
    except:
        raise Exception(
            "Add widget documentation on widget class constructor __init__."
        )


def strip_docs(doc_lines: List[str]) -> List[str]:
    return list(map(lambda line: line.strip(), doc_lines))


def remove_empty_lines(doc_lines: List[str]) -> List[str]:
    return list(filter(lambda line: len(line) > 0, doc_lines))


def get_docs_sections(docs: List[str]):
    return (
        get_description_from_docs(docs),
        get_position_args_from_docs(docs),
        get_keyword_args_from_docs(docs),
    )


def get_description_from_docs(docs: List[str]) -> List[str]:
    description = []
    current = 0

    while current < len(docs):
        if not docs[current].startswith(POSITIONAL_ARGS_SECTION):
            description.append(docs[current])
            current += 1
            continue
        break

    if current == 0:
        raise Exception(
            "Description not found. Please, write docs with description, positional args and keyword args."
        )

    if current == len(docs):
        raise Exception(
            "Positional arguments not found. Please, write docs with description, positional args and keyword args."
        )

    return description


def get_position_args_from_docs(docs: List[str]) -> List[str]:
    positional_args = []
    current = 0
    positional_not_found = True

    while current < len(docs):
        if positional_not_found and not docs[current].startswith(
            POSITIONAL_ARGS_SECTION
        ):
            current += 1
            continue

        if docs[current].startswith(POSITIONAL_ARGS_SECTION):
            positional_not_found = False
            current += 1
            continue

        if docs[current].startswith(KEYWORD_ARGS_SECTION):
            break

        positional_args.append(docs[current])
        current += 1

    return positional_args


def get_keyword_args_from_docs(docs: List[str]) -> List[str]:
    keyword_args = []
    current = 0
    keyword_not_found = True

    while current < len(docs):
        if keyword_not_found and not docs[current].startswith(KEYWORD_ARGS_SECTION):
            current += 1
            continue

        if docs[current].startswith(KEYWORD_ARGS_SECTION):
            keyword_not_found = False
            current += 1
            continue

        keyword_args.append(docs[current])
        current += 1

    if len(keyword_args) == 0:
        raise Exception(
            "Keyword args not found. Please, describe the possible keyword arguments in widget type method."
        )

    return keyword_args


def generate_page_method_docs(
    docs: Dict, key_default: Optional[str] = None, widget_type: str = "input"
) -> Dict:

    keyword_arguments = process_keywords(
        docs["keyword_arguments"],
        key_default,
        widget_type,
    )
    return_message = "The form object"

    return {
        "description": docs["description"],
        "positional_arguments": docs["positional_arguments"],
        "keyword_arguments": keyword_arguments,
        "return_message": return_message,
    }


def process_keywords(
    keyword_arguments: List[str],
    key_default: Optional[str] = None,
    widget_type: str = "input",
) -> List[str]:
    processed_keywords = add_columns_keyword(remove_button_text(keyword_arguments))

    if widget_type == "input":
        processed_keywords = add_key_keyword(processed_keywords, key_default)

    return processed_keywords


def remove_button_text(keyword_arguments: List[str]) -> List[str]:
    return list(
        filter(
            lambda argument: not argument.startswith("button_text"), keyword_arguments
        )
    )


def add_columns_keyword(keyword_arguments: List[str]) -> List[str]:
    keyword = "columns: The number of columns of the input"
    return keyword_arguments + [keyword]


def add_key_keyword(keyword_arguments: List[str], key_default: Optional[str]):
    if key_default:
        keyword = f"key: The key of the input's value on the form result. Defaults to the {key_default} arg"
    else:
        keyword = f"key: The key of the input's value on the form result. Defaults to empty string"

    return keyword_arguments + [keyword]
