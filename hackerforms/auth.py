from .socket import send, receive

def authenticate():
  send({"type": "auth:initialize"})
  while True:
    auth = receive()
    if auth["type"] == "auth:validation-ended":
      return auth