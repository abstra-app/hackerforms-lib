from hackerforms.common import Output
from typing import Union
from hackerforms.file_utils import convert_file
import io


class FileOutput(Output):
    type = "file-output"

    def __init__(self, file: Union[str, io.IOBase], **kwargs):
        """Display a button for the user to download a file

        Positional Args:
            file (file-like or str (path, url, base64)): The file to download

        Keyword Args:
            download_text (str): The text to display on the button that will download the file. Defaults to "Download here".
            full_width (bool): Whether the input should use full screen width. Defaults to False.

        """
        self.file = file
        self.download_text = kwargs.get("download_text", "Download here")
        self.columns = kwargs.get("columns", 1)
        self.full_width = kwargs.get("full_width", False)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "fileUrl": convert_file(self.file),
            "downloadText": self.download_text,
            "columns": self.columns,
            "fullWidth": self.full_width,
        }
