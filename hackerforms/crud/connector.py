from abc import ABC
from typing import Dict


class Connector(ABC):
    def __init__(self):
        pass

    def select(self, query: str):
        pass

    def insert(self, table: str, data: Dict):
        pass
