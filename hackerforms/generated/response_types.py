from tempfile import NamedTemporaryFile
import requests
from dataclasses import dataclass


class FileResponse:
    """A file response from the user

    Attributes:
        file (file): The file object
        url (str): The url of the file
        content (bytes): The content of the file
    """

    def __init__(self, url):
        res = requests.get(url)
        self.content = res.content
        self.url = url
        self.name = url.split("/")[-1]

        self.file = NamedTemporaryFile()
        self.file.write(self.content)
        self.file.seek(0)


@dataclass
class PhoneResponse:
    """A phone response from the user

    Attributes:
        masked (str): The masked phone number, eg: +55 (21) 99999-9999
        raw (str): The raw phone number, eg: 5521999999999
        country_code (str): The phone number country code, eg: 55
        national_number (str): The phone number national number, eg: 21999999999
    """

    masked: str
    raw: str
    country_code: str
    national_number: str
