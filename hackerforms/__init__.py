from .page import *
from .inputs import *
from .outputs import *
from .stdio import initialize as _initialize_stdio
from .auth import *
from .parameters import url_params
from .socket import initialize as _initialize_socket
import os


if os.environ.get("ENV") != "test":
  _initialize_socket()
  _initialize_stdio()
