from hackerforms.common import Output
from hackerforms.file_utils import convert_file
from typing import Union
import io


class ImageOutput(Output):
    type = "image-output"

    def __init__(self, image: Union[str, io.IOBase], **kwargs):
        """Display an image to the user

        Positional Args:
            image (file-like or str (path, url, base64)): The image to display to the user

        Keyword Args:
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            subtitle (str): The subtitle of the image. Defaults to "".

        """
        self.image = image
        self.subtitle = kwargs.get("subtitle", "")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "imageUrl": convert_file(self.image),
            "subtitle": self.subtitle,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
