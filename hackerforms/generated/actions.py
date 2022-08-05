###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################
from ..socket import send, receive


def execute_action(type, payload):
    send(
        {
            "type": "action",
            "action": {
                "type": type,
                **payload,
            },
        }
    )

    response = receive()

    if "errorMessage" in response:
        raise Exception(response["errorMessage"])

    return response.get("value", None)


def redirect(url):
    return execute_action("redirect", {"url": url})
