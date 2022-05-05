from .socket import send, receive

def authenticate():
  """Get the users email and verify it

  This method will ask the user to enter their email address and will
  verify it. It will then return the email address and wether the user
  is authenticated or not.

  Returns:
    { 'valid': Boolean, 'info': { 'email': str } }
  """
  send({"type": "auth:initialize"})
  while True:
    auth = receive()
    if auth["type"] == "auth:validation-ended":
      return auth