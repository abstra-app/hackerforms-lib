from hackerforms.socket import send, receive
from hackerforms.generated.widget_schema import WidgetSchema
from hackerforms.page_response import PageResponse
from hackerforms.validation import validate_widget_props

from typing import Callable, Dict


class Page(WidgetSchema):
    """A form page that can be displayed to the user

    This is a page that can be displayed to the user. It can be used to
    show data as well as collect informations. After configuring the
    inputs and outputs, use the run method to display the form to the
    user and collect the answers.
    """

    def __init__(self):
        super().__init__()

    def run(
        self, actions="Next", columns: float = 1, validate: Callable = None
    ) -> Dict:
        """Run the form

        Args:
            button_text: The text of the button that is used to submit the form
            columns: The number of columns of the form

        Returns:
            The form result as a dict with the keys being the key of the input and the value being the value of the input
        """

        widgets_json = self.__get_validated_page_widgets_json(self.convert_answer({}))

        if self.__is_progress_screen():
            self.__send_form_message(widgets=widgets_json, columns=columns, actions=[])
            return

        self.__send_form_message(
            widgets=widgets_json,
            columns=columns,
            actions=self.__actions_property(actions),
        )
        response: Dict = self.__user_event_messages(validate=validate)

        return PageResponse(
            self.convert_answer(response["payload"]),
            response.get("action"),
        )

    def __user_event_messages(self, **kwargs):
        response: Dict = receive()

        while response["type"] == "user-event":
            converted_payload = self.convert_answer(response["payload"])
            widgets_json = self.__get_validated_page_widgets_json(converted_payload)
            self.__send_user_event_message(
                widgets=widgets_json,
                validation=self.__build_validation_object(
                    validation=kwargs.get("validate"), payload=converted_payload
                ),
            )

            response = receive()

        return response

    def __get_validated_page_widgets_json(self, converted_payload):
        widgets_json = self.json(converted_payload)
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

        return {"status": validation_status, "message": validation_message}

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
