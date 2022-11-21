page_template = """
import typing
from typing import Any, Union, List, Dict
import io
from hackerforms.socket import send, receive
from hackerforms.input_types import *
from hackerforms.output_types import *
from hackerforms.validation import validate_widget_props
from hackerforms.realtime import Realtime
import copy


class WidgetSchema:
    def __init__(self):
        self.widgets: typing.List[typing.Union[Input, Output]] = []

    def realtime(self, callback):
        self.widgets.append(Realtime(callback))
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
            if isinstance(widget, Realtime):
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

class PageResponse(dict):
  def __init__(self, data, action):
    self.action = action
    self.data = data

  def __getitem__(self, key):
    return self.data[key]

  def __setitem__(self, key, value):
    self.data[key] = value

  def __delitem__(self, key):
    del self.data[key]

  def __iter__(self):
    return iter(self.data)

  def __len__(self):
    return len(self.data)

  def __contains__(self, key):
    return key in self.data

  def __str__(self):
    return str(self.data)
  
  def __repr__(self):
    return repr(self.data)

  def __cmp__(self, cmp_dict):
    return self.__cmp__(self.data, cmp_dict)

  def keys(self):
    return self.data.keys()

  def values(self):
    return self.data.values()

  def items(self):
    return self.data.items()

  def clear(self):
    return self.data.clear()

  def copy(self):
    return PageResponse(self.data.copy(), self.action)

  def has_key(self, key):
    return key in self.data

  def update(self, *args, **kwargs):
    return self.data.update(*args, **kwargs)
  
  def pop(self, *args):
    return self.data.pop(*args)


class Page(WidgetSchema):
    '''A form page that can be displayed to the user

    This is a page that can be displayed to the user. It can be used to
    show data as well as collect informations. After configuring the
    inputs and outputs, use the run method to display the form to the
    user and collect the answers.
    '''

    def __init__(self):
        super().__init__()

    def run(
        self, actions="Next", columns: float = 1, validate: typing.Callable = None
    ) -> typing.Dict:
        '''Run the form

        Args:
            button_text: The text of the button that is used to submit the form
            columns: The number of columns of the form

        Returns:
            The form result as a dict with the keys being the key of the input and the value being the value of the input
        '''

        widgets_json = self.__get_validated_page_widgets_json({})

        if self.__is_progress_screen():
            self.__send_form_message(widgets=widgets_json, columns=columns, actions=[])
            return

        self.__send_form_message(widgets=widgets_json, columns=columns, actions=self.__actions_property(actions))
        response: typing.Dict = self.__user_event_messages(validate=validate)

        return PageResponse(
            self.convert_answer(response["payload"]),
            response.get("action"),
        )

    def __user_event_messages(self, **kwargs):
        response: typing.Dict = receive()

        while response["type"] == "user-event":
            payload = response["payload"]
            widgets_json = self.__get_validated_page_widgets_json(payload)
            self.__send_user_event_message(widgets=widgets_json, validation=self.__build_validation_object(validation=kwargs.get("validate"),payload=payload))

            response = receive()

        return response
      
    def __get_validated_page_widgets_json(self, raw_payload):
        widgets_json = self.json(self.convert_answer(raw_payload))
        for widget in widgets_json:
            validate_widget_props(widget)
        return widgets_json
    
    def __actions_property(self, actions):
      if isinstance(actions, list):
          return actions
      elif actions is None:
          return []
      return [actions]

    def __is_progress_screen(self):
        return len(self.widgets) == 1 and self.widgets[0].type == "progress-output"

    def __build_validation_object(self, validation, payload):
        validation_status = True
        validation_message = ""

        if validation:
            validation_response = validation(payload)
            if type(validation_response) == bool:
                validation_status = validation_response
                validation_message = ""
            elif type(validation_response) == str:
                validation_status = False
                validation_message = validation_response

        return { "status": validation_status, "message": validation_message }

    def __send_form_message(self, widgets, actions, columns):
        send(
            {
                "type": "form",
                "widgets": widgets,
                "columns": columns,
                "actions": actions,
            }
        )
    
    def __send_user_event_message(self, widgets, validation):
        send(
                {
                    "type": "user-event",
                    "widgets": widgets,
                    "validation": validation,
                }
            )

class ListItemSchema(WidgetSchema):
    '''A schema for a list item

    This schema is used to define the schema of a list item.
    '''

    def __init__(self):
        super().__init__()
"""
