import os
import re
import pathlib
from setuptools import setup

regex = "^v(\d+\.\d+\.\d+)$"
TAG = os.getenv("TAG", "v0.0.0")
if not TAG or not re.search(regex, TAG):
    raise ValueError("TAG environment variable must be in the format v1.2.3")
version = re.search(regex, TAG).group(1)

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# The list of requirements
requirements = (HERE / "requirements.txt").read_text().split("\n")

setup(
    name="hackerforms",
    version=version,
    description="Hacker Forms",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abstra-app/hackerforms-lib",
    license="MIT",
    packages=[
        "hackerforms",
        "hackerforms.generated",
        "hackerforms.connection",
    ],
    install_requires=requirements,
)
