class TableNotFound(Exception):
    """Raised when the table is not found.

    Attributes:
      table -- input table which caused the error
      message --  explanation of the error
    """

    def __init__(self, table: str, message: str = None):
        self.message = (
            message if message else f"TableNotFound: {table} table not found."
        )
        super().__init__(self.message)


class PrimaryKeyNotDefined(Exception):
    """Raised when the table does not have a primary key defined.

    Attributes:
      table -- input table which caused the error
      message --  explanation of the error
    """

    def __init__(self, table: str, message: str = None):
        self.message = (
            message
            if message
            else f"PrimaryKeyNotDefined: table {table} does not have a primary key defined."
        )
        super().__init__(self.message)


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
