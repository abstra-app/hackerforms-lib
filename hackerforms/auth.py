from .socket import send, receive

def authenticate():
  """Get the users email and verify it

  This method will request users to fill in their email addresses and 
  verify them. It will then return the email address and wether the user
  is authenticated or not.

  Returns:
    { 'valid': Boolean, 'info': { 'email': str } }
  """
  send({"type": "auth:initialize"})
  while True:
    auth = receive()
    if auth["type"] == "auth:validation-ended":
      return auth