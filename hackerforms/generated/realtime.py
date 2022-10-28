import typing


class Realtime():
    type = "realtime"

    def __init__(self, callback: typing.Callable):
        self.callback = callback
        self.page = None

    def json(self, payload):
        self.page = self.callback(payload)
        return self.page.json(payload) if self.page else []

    def get_widgets(self):
        return self.page.widgets if self.page else []