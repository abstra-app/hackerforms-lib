widget_schema_template = """
import typing
import io
from hackerforms.input_types import *
from hackerforms.output_types import *
from hackerforms.reactive import Reactive


class WidgetSchema:
  def __init__(self):
    self.widgets: typing.List[typing.Union[Input, Output]] = []

  def reactive(self, callback):
    self.widgets.append(Reactive(callback))
    return self

  def convert_answer(self, form_answers: typing.Dict) -> typing.Dict:
    '''Convert the answer from the form to the expected format
    Args:
        answer: The answer from the form
    Returns:
        The converted answer
    '''
    answer: typing.Dict = {}
    inputs = self.get_input_widgets()
    for input in inputs:
        answer[input.key] = input.convert_answer(form_answers.get(input.key))
    return answer

  def get_input_widgets(self):
    concrete_widgets = []
    for widget in self.widgets:
      if isinstance(widget, Reactive):
        concrete_widgets.extend(widget.get_widgets())
      else:
        concrete_widgets.append(widget)

    inputs = list(
      filter(lambda widget: isinstance(widget, Input), concrete_widgets)
    )
    return inputs


  def json(self, payload):
    output = []
    for widget in self.widgets:
      widget_json = widget.json(payload=payload)
      if isinstance(widget_json, list):
          output.extend(widget_json)
      else:
          output.append(widget_json)
    
    return output

  {% for widget in input_widgets %}
  {% if input_widgets[widget]['func_name'] == 'read_text' %}
  def read(self, {{input_widgets[widget]['signature_params']}}):
    '''{%- for description in input_widgets[widget]['page_docs']['description'] -%}
      {{description}}
      {%- endfor %}

      Positional Args:
        {% for positional_args in input_widgets[widget]['page_docs']['positional_arguments'] -%}
        {{positional_args}}
        {%- endfor %}
      
      Keyword Args:
        {% for keyword_args in input_widgets[widget]['page_docs']['keyword_arguments'] -%}
        {{keyword_args}}
        {% endfor %}

      Returns:
        {{input_widgets[widget]['page_docs']['return_message']}}
    '''

    key = kwargs.pop('key', {{input_widgets[widget]['default_key']}})
    self.widgets.append({{widget}}(key, {{input_widgets[widget]['page_input']}}))
    return self 
  {%- else %}
  def {{input_widgets[widget]['func_name']}}(self, {{input_widgets[widget]['signature_params']}}):
    '''{%- for description in input_widgets[widget]['page_docs']['description'] -%}
      {{description}}
      {%- endfor %}

      Positional Args:
        {% for positional_args in input_widgets[widget]['page_docs']['positional_arguments'] -%}
        {{positional_args}}
        {%- endfor %}
      
      Keyword Args:
        {% for keyword_args in input_widgets[widget]['page_docs']['keyword_arguments'] -%}
        {{keyword_args}}
        {% endfor %}

      Returns:
        {{input_widgets[widget]['page_docs']['return_message']}}
    '''
    key = kwargs.pop('key', {{input_widgets[widget]['default_key']}})
    self.widgets.append({{widget}}(key, {{input_widgets[widget]['page_input']}}))
    return self
  {%- endif -%} 
  {% endfor %}

  {% for widget in output_widgets %}
  {% if output_widgets[widget]['func_name'] == 'display_text' %}
  def display(self, {{output_widgets[widget]['signature_params']}}):
    '''{%- for description in output_widgets[widget]['page_docs']['description'] -%}
      {{description}}
      {% endfor %}

      Positional Args:
        {% for positional_args in output_widgets[widget]['page_docs']['positional_arguments'] -%}
        {{positional_args}}
        {% endfor %}
      
      Keyword Args:
        {% for keyword_args in output_widgets[widget]['page_docs']['keyword_arguments'] -%}
        {{keyword_args}}
        {% endfor %}

      Returns:
        {{output_widgets[widget]['page_docs']['return_message']}}
    '''
    self.widgets.append({{widget}}({{output_widgets[widget]['page_input']}}))
    return self
  {%- else %}
  def {{output_widgets[widget]['func_name']}}(self, {{output_widgets[widget]['signature_params']}}):
    '''{%- for description in output_widgets[widget]['page_docs']['description'] -%}
      {{description}}
      {% endfor %}

      Positional Args:
        {% for positional_args in output_widgets[widget]['page_docs']['positional_arguments'] -%}
        {{positional_args}}
        {% endfor %}
      
      Keyword Args:
        {% for keyword_args in output_widgets[widget]['page_docs']['keyword_arguments'] -%}
        {{keyword_args}}
        {% endfor %}

      Returns:
        {{output_widgets[widget]['page_docs']['return_message']}}
    '''
    self.widgets.append({{widget}}({{output_widgets[widget]['page_input']}}))
    return self
  {%- endif -%} 
  {% endfor %}

  input = read

"""
