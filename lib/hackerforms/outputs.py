from .form import *

def display_text(msg: str, button_text: str = 'Next'):
    return Form(button_text).display_text(msg).run()

def display_image(image_str: str, subtitle: str = "", button_text: str = 'Next'):
    return Form(button_text).display_image(image_str, subtitle).run()

def display_link(link_url: str, link_text: str = "Click here", button_text: str = 'Next'):
    return Form(button_text).display_link(link_url, link_text).run()

def display_file(file, download_text: str = "Download here", button_text: str = 'Next'):
    return Form(button_text).display_file(file, download_text).run()

def display_html(html: str, download_text: str = "Download here", button_text: str = 'Next'):
    return Form(button_text).display_html(html, download_text).run()
