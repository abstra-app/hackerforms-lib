import os
from collections import UserDict
from .connection import Connection


WS_HOST = os.environ.get("WS_HOST", "wss://hackerforms-broker.abstra.cloud")
FRONTEND_HOST = os.environ.get("FRONTEND_HOST", "https://console.abstracloud.com")
DEBUG_ENABLED = os.environ.get("ABSTRA_DEBUG")
SESSION_ID = os.environ.get("SESSION_ID")
ABSTRA_FORM_SERVER = os.environ.get("ABSTRA_FORM_SERVER")


def initialize():
    global __connection, initialized
    if ABSTRA_FORM_SERVER:
        return
    initialized = True
    __connection = Connection(SESSION_ID, DEBUG_ENABLED)


def get_connection():
    if not initialized or not __connection:
        raise Exception('No connection available')
    return __connection


def send(data, debug_data=None):
    return get_connection().send(data, debug_data)


def receive(path: str = ""):
    return get_connection().receive(path)


def close():
    return get_connection().close()


# this is a class to wrap all read methods of dicts to call get_url_params instead
class UrlParams(UserDict):
    @property
    def params(self):
        conn = get_connection()
        return conn.url_params if conn else {}

    def __getitem__(self, key):
        return self.params.__getitem__(key)

    def __iter__(self):
        return self.params.__iter__()

    def __len__(self) -> int:
        return self.params.__len__()

    def __contains__(self, key):
        return self.params.__contains__(key)

    def __str__(self) -> str:
        return self.params.__str__()

    def __repr__(self) -> str:
        return self.params.__repr__()

    def keys(self):
        return self.params.keys()

    def values(self):
        return self.params.values()

    def items(self):
        return self.params.items()

    def has_key(self, key):
        return key in self.params


url_params = UrlParams()
initialized = False
__connection = None
