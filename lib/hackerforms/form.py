from typing import List, Dict
from .socket import send, receive
from .input_types import *
from .output_types import *


class Form:
    def __init__(self, button_text: str = 'Next'):
        self.button_text = button_text
        self.fields: List[Union[Input, Output]] = []

    def read(self, message: str, key: str = ''):
        self.fields.append(TextInput(key or message, message))
        return self

    def read_textarea(self, message: str, key: str = ''):
        self.fields.append(TextareaInput(key or message, message))
        return self

    def read_number(self, message: str, key: str = ''):
        self.fields.append(NumberInput(key or message, message))
        return self

    def read_email(self, message: str, key: str = ''):
        self.fields.append(EmailInput(key or message, message))
        return self

    def read_phone(self, message: str, key: str = ''):
        self.fields.append(PhoneInput(key or message, message))
        return self

    def read_date(self, message: str, key: str = ''):
        self.fields.append(DateInput(key or message, message))
        return self

    def read_file(self, message: str, key: str = ''):
        self.fields.append(FileInput(key or message, message))
        return self

    def read_dropdown(self, name: str, options: Union[List[str], List[Dict]], key: str = ''):
        self.fields.append(DropdownInput(key or name, name, options))
        return self

    def read_multiple_choice(self, message: str, options: Union[List[str], List[Dict]], multiple: bool = False, key: str = ''):
        self.fields.append(MultipleChoiceInput(
            key or message, message, options, multiple))
        return self

    def display(self, msg: str):
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

    def display_html(self, html: str):
        self.fields.append(HTMLOutput(html))
        return self

    def display_pandas(self, df):
        self.fields.append(PandasOutput(df))
        return self

    def display_plotly(self, fig):
        self.fields.append(PlotlyOutput(fig))
        return self

    def run(self):
        send({
            'type': 'form',
            'fields': [field.json() for field in self.fields],
            'buttonText': self.button_text
        })
        form_answers: Dict = receive('payload')
        answer: Dict = {}

        inputs = list(
            filter(lambda field: isinstance(field, Input), self.fields))

        if len(inputs) == 1:
            input = inputs[0]
            return input.convertAnswer(form_answers[input.key])

        for input in inputs:
            answer[input.key] = input.convertAnswer(form_answers[input.key])
        return answer
