import io
from typing import Union

from .apis import upload_file


def convert_file(file: Union[str, io.IOBase]) -> str:
    if not file:
        return ""

    if isinstance(file, str):
        # URL or base64 encoded string
        if file.startswith("http") or file.startswith("data:"):
            return file

        # path to file
        file = open(file, "rb")

    return upload_file(file)
