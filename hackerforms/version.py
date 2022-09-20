import pkg_resources
import requests

__version__ = pkg_resources.get_distribution("hackerforms").version


def check_version():
    try:
        libs = requests.get(
            "https://hackerforms-api.abstra.cloud/public/abstra-pypi-packages"
        ).json()
        hackerforms = list(filter(lambda lib: lib["name"] == "hackerforms", libs))[0]

        if hackerforms["version"] != __version__ and __version__ != "0.0.0":
            print("You are using an outdated version of hackerforms.")
            print(
                "Please update your library using the following command: pip install hackerforms=="
                + hackerforms["version"]
            )
    except Exception as e:
        pass
