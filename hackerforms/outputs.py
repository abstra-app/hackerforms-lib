from .page import *


def display(message: str, **kwargs):
    '''Display a message to the user

    Positional Arg:
        message (str): The message to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display(message, **kwargs).run(button_text)


def display_markdown(text: str, **kwargs):
    '''Display a formatted text to the user

    Positional Arg:
        text (str): The formatted text to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_markdown(text, **kwargs).run(button_text)


def display_image(image_str: str, **kwargs):
    '''Display an image to the user

    Positional Arg:
        image_str (str): The url or base64 encoding of the image to display to the user

    Keyword Arg:
        subtitle (str): The subtitle of the image
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_image(image_str, **kwargs).run(button_text)


def display_link(link_url: str, **kwargs):
    '''Display a link to the user

    Positional Arg:
        link_url (str): The url of the link to display to the user

    Keyword Arg:
        link_text (str): The text to display on the link
        button_text (str): The text to display on the button that will continue the form
        same_tab (bool): Whether to open the link in the same tab or not
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_link(link_url, **kwargs).run(button_text)


def display_file(file, **kwargs):
    '''Display a button for the user to download a file

    Positional Arg:
        file (File): The file to download

    Keyword Arg:
        download_text (str): The text to display on the button that will download the file
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_file(file, **kwargs).run(button_text)


def display_html(html: str, **kwargs):
    '''Display a html snippet to the user

    Positional Arg:
        html (str): The html snippet to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_html(html, **kwargs).run(button_text)


def display_pandas(df, **kwargs):
    '''Display a pandas dataframe to the user

    Positional Arg:
        df (pandas.DataFrame): The dataframe to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_pandas(df, **kwargs).run(button_text)


def display_plotly(fig, **kwargs):
    '''Display a plotly figure to the user

    Positional Arg:
        fig (plotly.Figure): The figure to display to the user

    Keyword Arg:
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_plotly(fig, **kwargs).run(button_text)


def display_iframe(url_or_html: str, **kwargs):
    '''Display an inline iframe to the user

    Positional Arg:
        url_or_html (str): The link to the document or the own document to display to the user

    Keyword Arg:
        width (int): The width of the iframe
        height (int): The height of the iframe
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')

    return Page().display_iframe(url_or_html, **kwargs).run(button_text)
