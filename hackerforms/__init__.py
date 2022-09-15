import os

from .auth import *
from .generated.page import *
from .generated.inputs import *
from .generated.outputs import *
from .generated.actions import *
from .parameters import url_params

from .socket import initialize as _initialize_socket
from .overloads import initialize as _initialize_overloads


if os.getenv("ENV") != "test":
    _initialize_socket()
    _initialize_overloads()
