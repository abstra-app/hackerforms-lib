# hackerforms-lib
Documentation for Hackerforms Library

# Outputs

These functions display something on the screen and 
returns when the user clicks the button (with text defined by `button_text`)

## simple text
``` python
def display(msg: str, button_text: str = "Next") -> None
```

## image

``` python
def display_image(image_str: str, button_text: str = "Next", subtitle: str = "") -> None
```
the `image_str` param should be an url or the encoded base64 of the image

## link

``` python
def display_link(link_url: str, button_text: str = "Next", link_text: str = "Click here") -> None
```

## file

``` python
def display_file(file, button_text: str = "Next", download_text: str = "Download here") -> None
```
the `file` param should be the file url of a [file-like](https://docs.python.org/3/glossary.html#term-file-like-object) object

# Inputs

These functions ask for some input from the user.

## simple text

``` python
def read(msg: str, button_text: str = "Next") -> str
```
## email

``` python
def read_email(msg: str, button_text: str = "Next") -> str
```
## phone

``` python
def read_phone(msg: str, button_text: str = "Next") -> str
```
## date

``` python
def read_date(msg: str, button_text: str = "Next") -> str
```
the response will be in the `YYYY-MM-DD` format

## file

``` python
def read_file(msg: str, button_text: str = "Next") -> FileResponse
```
the response type `FileResponse` has attributes `url` (string), `content` (bytes) and `file` (TemporaryFile)

## multiple choice

``` python
def read_multiple_choice(msg: str,
                         options: Union[List[str], List[Dict]],
                         button_text: str = "Next",
                         multiple: bool = False) -> str
```
options example:
```python
['Option 1', 'Option 2', 'Option 3']
[{'label': 'First option', 'value': 1}, {'label': 'Second option', 'value': 2}]
```

## dropdown

``` python
def read_dropdown(name: str, 
                  options: Union[List[str], List[Dict]], 
                  button_text: str = "Next") -> str
```
options example:
```python
['Option 1', 'Option 2', 'Option 3']
[{'label': 'First option', 'value': 1}, {'label': 'Second option', 'value': 2}]
```
