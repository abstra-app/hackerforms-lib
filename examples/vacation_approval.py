from hackerforms import *
import requests
import json
import os
from datetime import datetime
from urllib.parse import urlencode, quote_plus

api_key = os.environ['API_KEY']

display("Hi there! You have a new vacation request.",
        button_text="Let's see")

# Retrieve request from your database
endpoint = "https://INSERT_API_URL_HERE"
head = {"Authorization": "Bearer " + api_key}
data = requests.get(url = endpoint, headers = head)
data = data.json()

data_fields = data['fields']
name = data_fields['Name']
email = data_fields['Email address']
team = data_fields['Team']
start_date_requested = data_fields['Start date']
end_date_requested = data_fields['End date']
last_vacation = data_fields['Days of vacation in the last 12 months']

# Convert string into date to make calculations
start_date_requested = datetime.strptime(start_date_requested, '%Y-%m-%d')
end_date_requested = datetime.strptime(end_date_requested, '%Y-%m-%d')
days_requested = end_date_requested - start_date_requested

# Company's vacation policy
companys_vacation_policy = 30
time_remaining = companys_vacation_policy - last_vacation

display(name +" from the " + team + " team has requested " + str(days_requested.days) + " days of vacation, from " + start_date_requested.strftime("%x") + " to " + end_date_requested.strftime("%x") +".")

display("They’ve taken " + str(last_vacation) + " days off in the last 12 months and have " + str(time_remaining) + " remaining days to request, according to company policy.")

approve = read_multiple_choice("Do you approve this request for " + str(days_requested.days) + " days starting " + start_date_requested.strftime("%x") + "?", [
 {"label": "Yes", "value": True},
 {"label":"No", "value": False}, 
])

# Send response to database and create calendar link
if approve == True:
  calendar_start_date = start_date_requested.strftime("%Y%m%d")
  calendar_end_date = end_date_requested.strftime("%Y%m%d")
  calendar_properties = {'dates': calendar_start_date + '/' + calendar_end_date, 'details':'Enjoy!', 'text': f"{name}'s Vacation"}
  calendar_url = "https://calendar.google.com/calendar/render?action=TEMPLATE&" + urlencode(calendar_properties, quote_via=quote_plus)
  
  endpoint = "https://INSERT_API_URL_HERE"
  head = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}
  info = {"fields": {
          "Request Status": "Approved", 
          "Comment": calendar_url 
      }}        
  approval = requests.patch(url = endpoint, json = info, headers = head)
  
  display("We've registered your approval successfully!")
  display_link(calendar_url, f"Click here to add {name}'s vacation to your calendar")
elif approve == False:
  comment = read_textarea("Please tell us why the request was denied:")
  
  endpoint = "https://INSERT_API_URL_HERE"
  head = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}
  info = {"fields": {
          "Request Status": "Denied", 
          "Comment": comment 
      }}      
  approval = requests.patch(url = endpoint, json = info, headers = head)
  display("We've registered your response successfully. Thanks!")