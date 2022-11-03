from abc import ABC
from typing import Dict


class Connector(ABC):
    def __init__(self, connection):
        self.connection = connection

    def select(self, query: str):
        pass

    def insert(self, table: str, data: Dict):
        pass
