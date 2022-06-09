import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='hackerforms',
    version='0.3.2',
    description='Hacker Forms',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abstra-app/hackerforms-lib",
    license='MIT',
    packages=['hackerforms'],
    install_requires=['setuptools', 'requests',
                      'websocket-client', 'validators']
)
