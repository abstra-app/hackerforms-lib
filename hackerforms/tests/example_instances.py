from hackerforms.widgets.input_types import *
from hackerforms.widgets.output_types import *
import pandas as pd
import plotly.graph_objs as go

example_instances = [
    TextInput("text", "What is your name?"),
    TagInput(
        "tags",
        "What are your interests?",
        initial_value=["python", "javascript", "c++"],
    ),
    DateInput("date", "When is your birthday?"),
    FileInput("file", "Upload a file"),
    ImageInput("file", "Upload a image file"),
    VideoInput("file", "Upload a video file"),
    MultipleChoiceInput(
        "multiple-choice",
        "What is your favorite color?",
        options=["Red", "Blue", "Green"],
    ),
    DropdownInput(
        "dropdown", "What is your favorite color?", options=["Red", "Blue", "Green"]
    ),
    TextareaInput("textarea", "What is your favorite color?"),
    NumberInput("number", "What is your favorite number?"),
    EmailInput("email", "What is your email address?"),
    PhoneInput("phone", "What is your phone number?"),
    CardsInput(
        "card",
        "What is your favorite color?",
        options=[
            {
                "title": "red",
                "image": "https://via.placeholder.com/150/FF0000/808080",
                "description": "red",
            },
            {
                "title": "blue",
                "image": "https://via.placeholder.com/150/0000FF/808080",
                "description": "blue",
            },
            {
                "title": "green",
                "image": "https://via.placeholder.com/150/00FF00/808080",
                "description": "green",
            },
        ],
    ),
    TextOutput("Hello, world!"),
    MarkdownOutput("## This is a h2 tag"),
    ImageOutput("https://i.imgur.com/XyqQZ.jpg", subtitle="A cute cat"),
    LinkOutput("https://www.google.com", link_text="Google"),
    FileOutput("https://www.google.com", download_text="Google"),
    HtmlOutput("<h1>Hello, world!</h1>"),
    PandasOutput(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})),
    PlotlyOutput(go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 1, 2])])),
    IframeOutput("<h1>Hello, world!</h1>", width="100%", height="100%", column=1),
    PandasRowSelectionInput(
        "dataframe", pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    ),
    TimeInput("time", "What's the meeting time?"),
    PasswordInput("password", "Insert your password"),
    CodeInput("code", "Type your code", language="python"),
    NpsInput(
        "nps", "How likely?", min=1, max=100, min_hint="No way!", max_hint="Hell yeah!"
    ),
    CurrencyInput("currency", "How much?", currency="BRL"),
    ProgressOutput(50, 100),
]
