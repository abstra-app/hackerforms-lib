display_functions_template = """
import typing
import io
from hackerforms.page import Page

{%- for widget in widgets %}
{% if widgets[widget]['func_name'] == 'display_text' %}
def display({{widgets[widget]['signature_params']}}):
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
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().display({{widgets[widget]['page_input']}}).run(button_text)
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
  '''
  button_text = kwargs.get('button_text', 'Next')
  return Page().{{widgets[widget]["func_name"]}}({{widgets[widget]['page_input']}}).run(button_text)
{%- endif -%} 
{% endfor %}

"""
