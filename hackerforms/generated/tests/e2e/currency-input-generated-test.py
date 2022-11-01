###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################
from hackerforms import *


output = read_currency("text to be displayed", currency="BRL", full_width=True)
assert output == 23.3

output = read_currency("text to be displayed", currency="BRL", full_width=False)
assert output == 23.3

output = read_currency("text to be displayed", currency="BRL", hint="custom hint")
assert output == 23.3

output = read_currency("text to be displayed", currency="BRL", required=True)
assert output == 23.3

output = read_currency(
    "text to be displayed", currency="BRL", placeholder="custom placeholder"
)
assert output == 23.3