from typing import List, Dict
from .socket import send, receive
from .outputs import *
from .inputs import *

class Form:
    def __init__(self, title: str = '', button_text: str = 'Next'):
        self.title = title
        self.button_text = button_text
        self.fields: List[Union[Input, Output]] = []

    def read_text(self, key: str, message: str):
        self.fields.append(TextInput(key, message))
        return self

    def read_textarea(self, key: str, message: str):
        self.fields.append(TextareaInput(key, message))
        return self
        
    def read_number(self, key: str, message: str):
        self.fields.append(NumberInput(key, message))
        return self

    def read_email(self, key: str, message: str):
        self.fields.append(EmailInput(key, message))
        return self

    def read_phone(self, key: str, message: str):
        self.fields.append(PhoneInput(key, message))
        return self

    def read_date(self, key: str, message: str):
        self.fields.append(DateInput(key, message))
        return self

    def read_file(self, key: str, message: str):
        self.fields.append(FileInput(key, message))
        return self

    def read_dropdown(self, key: str, name: str, options: Union[List[str], List[Dict]]):
        self.fields.append(DropdownInput(key, name, options))
        return self

    def read_multiple_choice(self, key: str, message: str, options: Union[List[str], List[Dict]], multiple: bool = False):
        self.fields.append(MultipleChoiceInput(key, message, options, multiple))
        return self

    def display_text(self, msg: str):
        self.fields.append(TextOutput(msg))
        return self

    def display_image(self, image_str: str, subtitle: str = ""):
        self.fields.append(ImageOutput(image_str, subtitle))
        return self

    def display_link(self, link_url: str, link_text: str = "Click here"):
        self.fields.append(LinkOutput(link_url, link_text))
        return self

    def display_file(self, file, download_text: str = "Download here"):
        self.fields.append(FileOutput(file, download_text))
        return self

    def display_html(self, html: str, download_text: str = "Download here"):
        self.fields.append(HTMLOutput(html, download_text))
        return self

    def run(self):
        send({
            'type': 'form',
            'fields': [field.json() for field in self.fields],
            'buttonText': self.button_text
        })
        form_answers: Dict = receive('payload')
        answer: Dict = {}
        for field in self.fields:
            if isinstance(field, Input):
                answer[field.key] = field.convertAnswer(form_answers[field.key])
        return answer
