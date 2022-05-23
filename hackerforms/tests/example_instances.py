from ..page import Page
from ..input_types import *
from ..output_types import *
import pandas as pd
import plotly.graph_objs as go


example_instances = [
    TextInput('text', 'What is your name?'),
    DateInput('date', 'When is your birthday?'),
    FileInput('file', 'Upload a file'),
    MultipleChoiceInput('multiple-choice', 'What is your favorite color?', options=['Red', 'Blue', 'Green']),
    DropdownInput('dropdown', 'What is your favorite color?', options=['Red', 'Blue', 'Green']),
    TextareaInput('textarea', 'What is your favorite color?'),
    NumberInput('number', 'What is your favorite number?'),
    EmailInput('email', 'What is your email address?'),
    PhoneInput('phone', 'What is your phone number?'),
    ListInput('list', Page().read("Name")),
    TextOutput('Hello, world!'),
    ImageOutput('https://i.imgur.com/XyqQZ.jpg', 'A cute cat'),
    LinkOutput('https://www.google.com', 'Google'),
    FileOutput('https://www.google.com', 'Google'),
    HTMLOutput('<h1>Hello, world!</h1>'),
    PandasOutput(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})),
    PlotlyOutput(go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 1, 2])])),
    IFrameOutput('<h1>Hello, world!</h1>', '100%', '100%'),
]