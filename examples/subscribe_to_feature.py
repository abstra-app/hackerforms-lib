from hackerforms import *
import requests
import os

api_key = os.environ['HUBSPOT_API_KEY']

display("Hi there. Thanks for your interest in our upcoming features!")

display("We're almost ready to launch. Let's sign you up to get the news first-hand.")

fname = read("Firstly, what is your first name?")

lname = read('What is your last name?')

email = read("Great! What's your email?")

# Create contact in Hubspot

endpoint = "https://api.hubapi.com/contacts/v1/contact"
head = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}
info = json.dumps({
  "properties": [
    {
      "property": "email",
      "value": email
    },
    {
      "property": "firstname",
      "value": fname
    },
    {
      "property": "lastname",
      "value": lname
    },
  ]
})

r = requests.post(url = endpoint, data = info, headers = head)

# Add contact to list

endpoint = "https://api.hubapi.com/contacts/v1/lists/1/add"
head = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}
emails = json.dumps({
        "emails": [
         email
        ]
        },
      )

r = requests.post(url = endpoint, data = emails, headers = head)

display(f"All set, {fname}! You'll be notified as soon as we launch 😎🚀")
