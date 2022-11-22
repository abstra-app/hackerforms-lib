from hackerforms import *

read_text = read


output = read_text("text to be displayed", full_width=True)
assert output == "text to be returned"

output = read_text("text to be displayed", full_width=False)
assert output == "text to be returned"

output = read_text("text to be displayed", hint="custom hint")
assert output == "text to be returned"

output = read_text("text to be displayed", required=True)
assert output == "text to be returned"

output = read_text("text to be displayed", placeholder="custom placeholder")
assert output == "text to be returned"
