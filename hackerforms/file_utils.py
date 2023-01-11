import io
from typing import Union
from .apis import upload_file
from .types import PILImage


def convert_file(file: Union[str, io.IOBase, PILImage]) -> str:
    if not file:
        return ""

    if isinstance(file, str):
        # URL or base64 encoded string
        if file.startswith("http") or file.startswith("data:"):
            return file

        # path to file
        file = open(file, "rb")

    if callable(getattr(file, "save", None)):
        file_path = "/tmp/img.png"
        file.save(file_path)
        file = open(file_path, "rb")

    return upload_file(file)
