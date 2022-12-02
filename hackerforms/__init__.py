import os

from .auth import *

from .actions import execute_js, redirect
from .version import check_version as _check_version
from .socket import initialize as _initialize_socket
from .overloads import initialize as _initialize_overloads
from .list_item_schema import ListItemSchema
from .page import Page
from . import environments as envs
from .parameters import url_params
from .generated.inputs import *
from .generated.outputs import *

environment = os.getenv("ENV")

if environment not in [envs.TEST]:
    _check_version()
    _initialize_socket()
    _initialize_overloads()

del _check_version
del _initialize_socket
del _initialize_overloads
