from abc import ABC


class Connector(ABC):
    def __init__(self):
        pass

    def select(self, query: str):
        pass

    def insert(self, query: str):
        pass
