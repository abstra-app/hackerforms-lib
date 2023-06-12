import os

from .auth import *

from .actions import execute_js, redirect  # exported
from .version import check_version as _check_version
from .socket import initialize as _initialize_socket, url_params  # exported
from .overloads import _overload_to_widgets, _overload_stdio
from .list_item_schema import ListItemSchema  # exported
from .page import Page  # exported
from .step import run_steps  # exported
from .generated.inputs import *
from .generated.outputs import *

is_nested = os.getenv("RUNNER") in ["dash", "hook", "job"]
is_hosted_form = os.getenv("RUNNER") == "form"  # bool(os.getenv("SESSION_ID"))
is_server = (
    os.getenv("ABSTRA_SERVER") == "true" or os.getenv("ABSTRA_FORM_SERVER") == "true"
)

# Karnaugh map
if is_server:
    _overload_to_widgets()
elif is_nested:
    pass
elif is_hosted_form:
    _initialize_socket()
    _overload_stdio()
    _overload_to_widgets()
else:  # is local
    _check_version()
    _initialize_socket()
    _overload_stdio()
    _overload_to_widgets()


del _check_version
del _initialize_socket
del _overload_stdio
del _overload_to_widgets
del is_nested
del is_server
del is_hosted_form
