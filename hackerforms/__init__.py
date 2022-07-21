from .generated.page import *
from .generated.inputs import *
from .generated.outputs import *
from .generated.actions import *
from .stdio import initialize as _initialize_stdio
from .auth import *
from .parameters import url_params
from .socket import initialize as _initialize_socket
from .input import overload_input as _overload_input
import os


if os.environ.get("ENV") != "test":
    _initialize_socket()
    _initialize_stdio()
    _overload_input()
