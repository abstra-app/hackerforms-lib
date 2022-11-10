from .socket import send, receive


def get_user():
    """Get the users email and verify it

    This method will request users to fill in their email addresses and
    verify them. It will then return the email address once it has been validated.

    Returns:
      AuthReponse
    """
    send({"type": "auth:initialize"})
    while True:
        auth = receive()
        if auth["type"] == "auth:validation-ended":
            return AuthResponse(auth["email"])


class AuthResponse:
    """The response from the authentication process

    Attributes:
      email (str): The email address of the user
    """

    def __init__(self, email: str):
        self.email = email
