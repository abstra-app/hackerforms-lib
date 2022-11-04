"""
hackerforms.crud.exceptions
~~~~~~~~~~~~~~~~~~~~~~~

This module provides possible exceptions raised in the crud subpackage

"""


class MissingParameter(Exception):
    """Raised when the user does not pass a required parameter.

    Attributes:
      parameter -- missing which caused the error
      message --  explanation of the error
    """

    def __init__(self, parameter: str, message: str = None):
        self.message = (
            message
            if message
            else f"MissingParameter: parameter {parameter} is required."
        )
        super().__init__(self.message)
