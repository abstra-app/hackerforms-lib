from hackerforms.common import Input
from hackerforms.response_types import FileResponse
from typing import Optional


class FileInput(Input):
    type = "file-input"

    def __init__(self, key: str, label: str, **kwargs):
        """Read a file value from the user

        Positional Args:
            label (str): The label to display to the user

        Keyword Args:
            initial_value (str): The initial value to display to the user. Defaults to "".
            required (bool or str): Whether the input is required or not eg. "this field is required". Defaults to True.
            hint (str): A tooltip displayed to the user. Defaults to None.
            full_width (bool): Whether the input should use full screen width. Defaults to False.
            multiple (bool): Whether the user will be allowed to upload multiple files. Defaults to False.
            max_file_size (float): Maximum size allowed to be transfered in total in MB.

        """
        super().__init__(key)
        self.label = label
        self.initial_value = kwargs.get("initial_value", "")
        self.required = kwargs.get("required", True)
        self.hint = kwargs.get("hint", None)
        self.columns = kwargs.get("columns", 1)
        self.multiple = kwargs.get("multiple", False)
        self.full_width = kwargs.get("full_width", False)
        self.disabled = kwargs.get("disabled", False)
        self.max_file_size = kwargs.get("max_file_size", None)

    def json(self, **kwargs):
        return {
            "type": self.type,
            "key": self.key,
            "hint": self.hint,
            "label": self.label,
            "initialValue": self.initial_value,
            "required": self.required,
            "columns": self.columns,
            "multiple": self.multiple,
            "fullWidth": self.full_width,
            "disabled": self.disabled,
            "maxFileSize": self.max_file_size,
        }

    def convert_answer(self, answer) -> Optional[FileResponse]:
        """
        Returns:
            FileResponse or FileResponse[]: A dict containing the file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of files in case of multiple flag set as True
        """
        if not answer:
            return None
        if not self.multiple:
            return FileResponse(answer)
        return [FileResponse(item) for item in answer]
