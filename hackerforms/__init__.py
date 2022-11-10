import os

from .auth import *
from .generated.page import *
from .generated.inputs import *
from .generated.outputs import *
from .generated.actions import *
from .parameters import url_params
from .version import __version__, check_version as _check_version
from .socket import initialize as _initialize_socket
from .overloads import initialize as _initialize_overloads

if os.getenv("ENV") != "test":
    _check_version()
    _initialize_socket()
    _initialize_overloads()

del _check_version
del _initialize_socket
del _initialize_overloads
