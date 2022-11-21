from hackerforms import *


output = read_email("text to be displayed", full_width=True)
assert output == "dev@abstra.app"

output = read_email("text to be displayed", full_width=False)
assert output == "dev@abstra.app"

output = read_email("text to be displayed", hint="custom hint")
assert output == "dev@abstra.app"

output = read_email("text to be displayed", required=True)
assert output == "dev@abstra.app"

output = read_email("text to be displayed", placeholder="custom placeholder")
assert output == "dev@abstra.app"
