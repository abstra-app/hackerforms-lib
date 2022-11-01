class TableNotFound(Exception):
    """Raised when the postgres table is not found.

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
    """Raised when the postgres column type is not found in mapper.

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
    """Raised when the postgres table does not have defined columns.

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


class ContextColumnNotFound(Exception):
    """Raised when the user sets a context column name not found in the related table.

    Attributes:
      table -- table in which the column was looked for.
      column -- mismatching column name which caused the error
      message --  explanation of the error
    """

    def __init__(self, table: str, column: str, message: str = None):
        self.message = (
            message
            if message
            else f"ContextColumnNotFound: column `{column}` not found in table {table}."
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
    """Raised when the postgres column table is not unique contrained.

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
    """Raised when the postgres table does not have a primary key defined.

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
