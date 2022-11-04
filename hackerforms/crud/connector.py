"""
hackerforms.crud.connector
~~~~~~~~~~~~~~~~~~~~~~~

This module provides an abstract class as interface for data sources wrapper implementations.

"""

from abc import ABC
from typing import Dict


class Connector(ABC):
    """Abstract class that all data source wrappers derive from.

        It's constructor received a connection, which can be a database driver or api service.
    
    """
    def __init__(self, connection):
        self.connection = connection

    def select(self, query: str):
        pass

    def insert(self, table: str, data: Dict):
        pass
