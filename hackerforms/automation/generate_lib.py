from parser.generate_functions import (
    generate_input,
    generate_metadata_dict,
    generate_output,
    generate_page,
)


def generate_lib():
    generate_input()
    print("Read functions generated")
    generate_output()
    print("Display functions generated")
    generate_page()
    print("Page generated")
    generate_metadata_dict()
    print("Metadata generated")


if __name__ == "__main__":
    generate_lib()
