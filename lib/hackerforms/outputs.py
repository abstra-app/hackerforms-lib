from .form import *

def display(msg: str, button_text: str = 'Next'):
    return Form(button_text).display(msg).run()

def display_image(image_str: str, subtitle: str = "", button_text: str = 'Next'):
    return Form(button_text).display_image(image_str, subtitle).run()

def display_link(link_url: str, link_text: str = "Click here", button_text: str = 'Next'):
    return Form(button_text).display_link(link_url, link_text).run()

def display_file(file, download_text: str = "Download here", button_text: str = 'Next'):
    return Form(button_text).display_file(file, download_text).run()

def display_html(html: str, button_text: str = 'Next'):
    return Form(button_text).display_html(html).run()

def display_pandas(df: pd.DataFrame, button_text: str = 'Next'):
    return Form(button_text).display_pandas(df).run()

def display_plotly(fig, button_text: str = 'Next'):
    return Form(button_text).display_plotly(fig).run()