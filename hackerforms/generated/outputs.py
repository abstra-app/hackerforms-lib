
###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################

import typing
import io
from .page import Page

def display_file(file: typing.Union[str, io.IOBase], **kwargs):
  '''Display a button for the user to download a file

      Positional Args:
        file (file-like or str (path, url, base64)): The file to download
      
      Keyword Args:
        download_text (str): The text to display on the button that will download the file
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_file(file, **kwargs).run(button_text)

def display_html(html: str, **kwargs):
  '''Display a html snippet to the user

      Positional Args:
        html (str): The html snippet to display to the userfull_width (bool): Whether the input should use full screen width
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_html(html, **kwargs).run(button_text)

def display_iframe(url_or_html: str, **kwargs):
  '''Display an inline iframe to the user

      Positional Args:
        url_or_html (str): The link to the document or the own document to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        width (int): The width of the iframe
        height (int): The height of the iframe
        full_width (bool): Whether the input should use full screen width
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_iframe(url_or_html, **kwargs).run(button_text)

def display_image(image: typing.Union[str, io.IOBase], **kwargs):
  '''Display an image to the user

      Positional Args:
        image (file-like or str (path, url, base64)): The image to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        subtitle (str): The subtitle of the image
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_image(image, **kwargs).run(button_text)

def display_link(link_url: str, **kwargs):
  '''Display a link to the user

      Positional Args:
        link_url (str): The url of the link to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        link_text (str): The text to display on the link
        same_tab (bool): Whether to open the link in the same tab or not
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_link(link_url, **kwargs).run(button_text)

def display_markdown(text: str, **kwargs):
  '''Display a formatted text to the user

      Positional Args:
        text (str): The formatted text to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_markdown(text, **kwargs).run(button_text)

def display_pandas(df: typing.Any, **kwargs):
  '''Display a pandas dataframe to the user

      Positional Args:
        df (pandas.DataFrame): The dataframe to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        display_index (bool): Whether to show a index column
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_pandas(df, **kwargs).run(button_text)

def display_plotly(fig: typing.Any, **kwargs):
  '''Display a plotly figure to the user

      Positional Args:
        fig (plotly.Figure): The figure to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display_plotly(fig, **kwargs).run(button_text)

def display(message: str, **kwargs):
  '''Display a message to the user

      Positional Args:
        message (str): The message to display to the user
      
      Keyword Args:
        button_text (str): The text to display on the button that will continue the form
        full_width (bool): Whether the input should use full screen width
        
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display(message, **kwargs).run(button_text)
