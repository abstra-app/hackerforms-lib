from tempfile import TemporaryFile
import requests
from dataclasses import dataclass


class FileResponse:
    def __init__(self, url):
        res = requests.get(url)
        self.content = res.content
        self.url = url

        self.file = TemporaryFile()
        self.file.write(self.content)
        self.file.seek(0)

@dataclass
class PhoneResponse:
    masked: str
    raw: str
