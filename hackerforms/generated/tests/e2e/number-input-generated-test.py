###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################
from hackerforms import *


output = read_number("text to be displayed", full_width=True)
assert output == 20.0

output = read_number("text to be displayed", full_width=False)
assert output == 20.0

output = read_number("text to be displayed", hint="custom hint")
assert output == 20.0

output = read_number("text to be displayed", required=True)
assert output == 20.0

output = read_number("text to be displayed", placeholder="custom placeholder")
assert output == 20.0