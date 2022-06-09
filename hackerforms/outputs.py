from .page import *


def display(**kwargs):
    '''Display a message to the user

    Keyword Arg:
        message (str): The message to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display(**kwargs).run(button_text)


def display_markdown(**kwargs):
    '''Display a formatted text to the user

    Keyword Arg:
        text (str): The formatted text to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_markdown(**kwargs).run(button_text)


def display_image(**kwargs):
    '''Display an image to the user

    Keyword Arg:
        image_str (str): The url or base64 encoding of the image to display to the user
        subtitle (str): The subtitle of the image
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_image(**kwargs).run(button_text)


def display_link(**kwargs):
    '''Display a link to the user

    Keyword Arg:
        link_url (str): The url of the link to display to the user
        link_text (str): The text to display on the link
        button_text (str): The text to display on the button that will continue the form
        same_tab (bool): Whether to open the link in the same tab or not
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_link(**kwargs).run(button_text)


def display_file(**kwargs):
    '''Display a button for the user to download a file

    Keyword Arg:
        file (File): The file to download
        download_text (str): The text to display on the button that will download the file
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_file(**kwargs).run(button_text)


def display_html(**kwargs):
    '''Display a html snippet to the user

    Keyword Arg:
        html (str): The html snippet to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_html(**kwargs).run(button_text)


def display_pandas(**kwargs):
    '''Display a pandas dataframe to the user

    Keyword Arg:
        df (pandas.DataFrame): The dataframe to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_pandas(**kwargs).run(button_text)


def display_plotly(**kwargs):
    '''Display a plotly figure to the user

    Keyword Arg:
        fig (plotly.Figure): The figure to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')
    return Page().display_plotly(**kwargs).run(button_text)


def display_iframe(**kwargs):
    '''Display an inline iframe to the user

    Keyword Arg:
        url_or_html (str): The link to the document or the own document to display to the user
        width (int): The width of the iframe
        height (int): The height of the iframe
        button_text (str): The text to display on the button that will continue the form
    '''
    button_text = kwargs.get('button_text', 'Next')

    return Page().display_iframe(**kwargs).run(button_text)
