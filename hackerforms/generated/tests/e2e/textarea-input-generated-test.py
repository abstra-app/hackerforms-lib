###############################################################################
##             This file is generated by hackerforms-protocol.               ##
##        Do not change this file. Any changes will be overwritten.          ##
###############################################################################
from hackerforms import *


output = read_textarea("text to be displayed", full_width=True)
assert output == "text to be returned"

output = read_textarea("text to be displayed", full_width=False)
assert output == "text to be returned"

output = read_textarea("text to be displayed", hint="custom hint")
assert output == "text to be returned"

output = read_textarea("text to be displayed", required=True)
assert output == "text to be returned"

output = read_textarea("text to be displayed", placeholder="custom placeholder")
assert output == "text to be returned"