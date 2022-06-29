from ..input_types import *
from ..output_types import *
import pandas as pd
import plotly.graph_objs as go

example_instances = [
    TextInput('text', 'What is your name?'),
    TagInput('tags', 'What are your interests?',
             initial_value = ['python', 'javascript', 'c++']),
    DateInput('date', 'When is your birthday?'),
    FileInput('file', 'Upload a file'),
    ImageInput('file', 'Upload a image file'),
    MultipleChoiceInput(
        'multiple-choice', 'What is your favorite color?', options=['Red', 'Blue', 'Green']),
    DropdownInput('dropdown', 'What is your favorite color?',
                  options=['Red', 'Blue', 'Green']),
    TextareaInput('textarea', 'What is your favorite color?'),
    NumberInput('number', 'What is your favorite number?'),
    EmailInput('email', 'What is your email address?'),
    PhoneInput('phone', 'What is your phone number?'),
    CardsInput('card', 'What is your favorite color?', options=[{'title': 'red', 'image': 'redImage', 'description': 'red'}, {
               'title': 'blue', 'image': 'blueImage', 'description': 'blue'}, {'title': 'green', 'image': 'greenImage', 'description': 'green'}]),
    TextOutput('Hello, world!'),
    MarkdownOutput('## This is a h2 tag'),
    ImageOutput('https://i.imgur.com/XyqQZ.jpg', subtitle = 'A cute cat'),
    LinkOutput('https://www.google.com', link_text='Google'),
    FileOutput('https://www.google.com', download_text='Google'),
    HTMLOutput('<h1>Hello, world!</h1>'),
    PandasOutput(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})),
    PlotlyOutput(go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 1, 2])])),
    IFrameOutput('<h1>Hello, world!</h1>', width='100%', height='100%', column=1),
    ExecuteJs("A key", "console.log('Hello World')", context={}),
    PandasRowSelectionInput( 'dataframe', pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}))
]
