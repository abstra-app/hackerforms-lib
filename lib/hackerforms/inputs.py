from typing import List, Union, Dict
from .form import *

def read_text(message: str, button_text: str = 'Next'):
    return Form(button_text).read_text(message).run()

def read_textarea(message: str, button_text: str = 'Next'):
    return Form(button_text).read_textarea(message).run()

def read_number(message: str, button_text: str = 'Next'):
    return Form(button_text).read_number(message).run()

def read_email(message: str, button_text: str = 'Next'):
    return Form(button_text).read_email(message).run()

def read_phone(message: str, button_text: str = 'Next'):
    return Form(button_text).read_phone(message).run()

def read_date(message: str, button_text: str = 'Next'):
    return Form(button_text).read_date(message).run()

def read_file(message: str, button_text: str = 'Next'):
    return Form(button_text).read_file(message).run()

def read_dropdown(name: str, options: Union[List[str], List[Dict]], button_text: str = 'Next'):
    return Form(button_text).read_dropdown(name, options).run()

def read_multiple_choice(message: str, options: Union[List[str], List[Dict]], multiple: bool = False, button_text: str = 'Next'):
    return Form(button_text).read_multiple_choice(message, options, multiple).run()
