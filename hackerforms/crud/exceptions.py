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


class ColumnTypeNotFound(Exception):
    """Raised when the column type is not found in mapper.

    Attributes:
      column type -- column type which caused the error
      message --  explanation of the error
    """

    def __init__(self, column_type: str, message: str = None):
        self.message = (
            message if message else f"ColumnTypeNotFound: {column_type} type not found."
        )
        super().__init__(self.message)


class TableColumnsUndefined(Exception):
    """Raised when the table does not have defined columns.

    Attributes:
      table -- input table which caused the error
      message --  explanation of the error
    """

    def __init__(self, table: str, message: str = None):
        self.message = (
            message
            if message
            else f"TableColumnsUndefined: {table} table has no column defined."
        )
        super().__init__(self.message)


class ColumnNotFound(Exception):
    """Raised when the user sets a column name not found in the related table.

    Attributes:
      table -- table in which the column was looked for.
      column -- mismatching column name which caused the error
      message --  explanation of the error
    """

    def __init__(self, table: str, column: str, message: str = None):
        self.message = (
            message
            if message
            else f"ColumnNotFound: column `{column}` not found in table {table}."
        )
        super().__init__(self.message)


class WrongContextColumnType(Exception):
    """Raised when the user sets a wrong column type value.

    Attributes:
      table -- table in which the column was looked for.
      column -- mismatching column name which caused the error
      message --  explanation of the error
    """

    def __init__(
        self,
        table: str,
        column: str,
        value: any,
        expected_type: any,
        message: str = None,
    ):
        self.message = (
            message
            if message
            else f"WrongContextColumnType: {column} column expects {expected_type} type but ({value, type(value)}) was passed in table {table}."
        )
        super().__init__(self.message)


class ColumnIsNotUniqueContrained(Exception):
    """Raised when the column table is not unique contrained.

    Attributes:
      table -- input table which caused the error
      column -- mismatching column name which caused the error
      message --  explanation of the error
    """

    def __init__(self, table: str, column: str, message: str = None):
        self.message = (
            message
            if message
            else f"ColumnIsNotUniqueContrained: column {column} in table {table} is not unique constrained."
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
