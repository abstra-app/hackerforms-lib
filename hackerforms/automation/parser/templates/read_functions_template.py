read_functions_template = """
import typing
from hackerforms.page import Page

{%- for widget in widgets %}
{% if widgets[widget]['func_name'] == 'read_text' %}
def read({{widgets[widget]['signature_params']}}):
  '''{%- for description in widgets[widget]['docs']['description'] -%}
      {{description}}
      {%- endfor %}

      Positional Args:
        {% for positional_args in widgets[widget]['docs']['positional_arguments'] -%}
        {{positional_args}}
        {%- endfor %}
      
      Keyword Args:
        {% for keyword_args in widgets[widget]['docs']['keyword_arguments'] -%}
        {{keyword_args}}
        {% endfor %}
  {{- widgets[widget]['return_docs'] -}}
  '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().read({{widgets[widget]['page_input']}}).run(button_text))
{%- else %}
def {{widgets[widget]["func_name"]}}({{widgets[widget]['signature_params']}}):
  '''{%- for description in widgets[widget]['docs']['description'] -%}
      {{description}}
      {%- endfor %}

      Positional Args:
        {% for positional_args in widgets[widget]['docs']['positional_arguments'] -%}
        {{positional_args}}
        {%- endfor %}
      
      Keyword Args:
        {% for keyword_args in widgets[widget]['docs']['keyword_arguments'] -%}
        {{keyword_args}}
        {% endfor %}
  {{- widgets[widget]['return_docs'] -}}
  '''
  button_text = kwargs.get('button_text', 'Next')
  return get_single_value(Page().{{widgets[widget]["func_name"]}}({{widgets[widget]['page_input']}}).run(button_text))
  
{%- endif -%} 
{% endfor %}

def get_single_value(answer: typing.Dict):
  return list(answer.values())[0]
"""
