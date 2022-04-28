from .page import *


def display(msg: str, button_text: str = 'Next'):
    '''Display a message to the user

    Args:
        msg (str): The message to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display(msg).run(button_text)


def display_image(image_str: str, subtitle: str = "", button_text: str = 'Next'):
    '''Display an image to the user

    Args:
        image_str (str): The url or base64 encoding of the image to display to the user
        subtitle (str): The subtitle of the image
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display_image(image_str, subtitle).run(button_text)


def display_link(link_url: str, link_text: str = "Click here", button_text: str = 'Next'):
    '''Display a link to the user
    
    Args:
        link_url (str): The url of the link to display to the user
        link_text (str): The text to display on the link
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display_link(link_url, link_text).run(button_text)


def display_file(file, download_text: str = "Download here", button_text: str = 'Next'):
    '''Display a button for the user to download a file

    Args:
        file (File): The file to download
        download_text (str): The text to display on the button that will download the file
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display_file(file, download_text).run(button_text)


def display_html(html: str, button_text: str = 'Next'):
    '''Display a html snippet to the user

    Args:
        html (str): The html snippet to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display_html(html).run(button_text)


def display_pandas(df, button_text: str = 'Next'):
    '''Display a pandas dataframe to the user

    Args:
        df (pandas.DataFrame): The dataframe to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display_pandas(df).run(button_text)


def display_plotly(fig, button_text: str = 'Next'):
    '''Display a plotly figure to the user

    Args:
        fig (plotly.Figure): The figure to display to the user
        button_text (str): The text to display on the button that will continue the form
    '''
    return Page().display_plotly(fig).run(button_text)
