import io
from typing import Union
from PIL.Image import Image
from .apis import upload_file


def convert_file(file: Union[str, io.IOBase, Image]) -> str:
    if not file:
        return ""

    if isinstance(file, str):
        # URL or base64 encoded string
        if file.startswith("http") or file.startswith("data:"):
            return file

        # path to file
        file = open(file, "rb")

    if isinstance(file, Image):
        file_path = "/tmp/img.png"
        file.save(file_path)
        file = open(file_path, "rb")

    return upload_file(file)
