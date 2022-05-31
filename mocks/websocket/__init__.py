import js

class WS:
    def recv(self):
        return js.__recv()

    def send(self, msg):
        return js.__send(msg)

    def close(self):
        return js.__close()

def create_connection(name):
    return WS()
