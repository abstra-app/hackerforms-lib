from hackerforms import *
import requests, json
from ast import literal_eval
import os

api_key = os.environ['AIRTABLE_API_KEY']

fname = read("Welcome to Dr.Pete's! Let's get started. What is your first name?")

lname = read('What is your last name?')

minitial = read('What is your middle initial? If you have no middle initial, leave blank.')

name = fname+' '+minitial+' '+lname

email = read("Ok. What is your email?")

birthdate = read_date(f"What is your date of birth, {fname}?")

#get countries from api and populate dropdown
list = []
hed={}
data = {}
url = 'https://countriesnow.space/api/v0.1/countries'
response = requests.get(url, json=data, headers=hed)
response = response.json()
list = response['data']

countries = []
for item in list:
  if 'country' in item:
    countries.append(item['country'])
country = read_dropdown(
  "In which country do you currently live?",
  options = countries
  )

#get states by country and populate dropdown
cities = []
hed={"Content-Type": "application/json"}
data = {"country": country}
url = 'https://countriesnow.space/api/v0.1/countries/cities'
response = requests.post(url, json=data, headers=hed)
response = response.json()
cities = response['data']

city = read_dropdown(
  "In which city do you currently live?",
  options = cities
  )

address_street = read(f"Ok! Please add your street address in {country}.")

address_number = read_number("And what's the number?")

address_apt = read("Apartment or unit:")

address_zip = read_number("Zip code:")

address = address_street+' '+str(address_number)+' '+address_apt+' ZIP '+str(address_zip)

phone = read_phone("What is your primary phone number?")

id_type = read_multiple_choice("What type of identification can you provide?",
  ["passport","driver's license","student ID"])

id_number = read("What is the identification number?")

id_expiration = read_date("What is the identification expiration date?")

display("We're done with personal info! Let's move on to your medical history.", 
        button_text = "Let's go!")

weight = read_number("What is your last known weight, in kilograms?")

height = read_number("What is your height, in centimeters?")

under_care = read_multiple_choice(
  "Are you under a physician's care now?",
  [{"label":"yes", "value": True},
   {"label":"no", "value": False}]
  )

if under_care == True:
  reason_under_care = read_textarea("Please state the main reason you are under medical care at the moment.")
else:
  reason_under_care = ""

hospitalized = read_multiple_choice(
  "Have you ever been hospitalized or had a major injury?",
  [{"label":"yes", "value": True},
   {"label":"no", "value": False}]
  )

if hospitalized == True:
  reason_hospitalized = read_textarea("Please provide details.")
else:
  reason_hospitalized = ""

medicated = read_multiple_choice(
  "Are you taking any medication?",
  [{"label":"yes", "value": True},
   {"label":"no", "value": False}]
  )

if medicated == "yes":
  reason_medicated = read_textarea("Please provide reasons, names and dosages of all medication.")
else:
  reason_medicated = ""

diet = read_multiple_choice(
  "Are you on a special diet?",
  [{"label":"yes", "value": True},
   {"label":"no", "value": False}]
  )

if diet == True:
  reason_diet = read_textarea("Please provide details regarding your diet.")
else:
  reason_diet = ""

smoker = read_multiple_choice(
  "Do you smoke?",
    [{"label":"yes", "value": True},
     {"label":"no", "value": False}]
  )

drinker = read_multiple_choice(
  "Do you consume alcohol regularly?",
  [{"label":"yes", "value": True},
   {"label":"no", "value": False}]
  )

pregnant_trying = read_multiple_choice(
  "Are you pregnant or trying to get pregnant?",
  [{"label":"yes", "value": True},
   {"label":"no", "value": False}]
  )

allergies = read_multiple_choice(
  "Please select from the list below any allergies you have.",
  ["aspirin","penicillin","codein","local anesthetics","other"],
  multiple = True
  )

if "other" in allergies:
  allergies_other = read("What other allergies do you have?"
  )
else:
  allergies_other = ""

concerns = read_textarea("If you have any specific concerns that brought you to medical care today, please explain them in detail here.")

display("Alright! We're nearly finished. Just one last thing...")

#check terms accepted if not type again
terms_accepted = False
while terms_accepted == False:
  name_confirm = read(f"Please confirm that you've answered this form with the truth to the best of your knowledge by typing your full name EXACTLY as follows: {name}")
  if name_confirm == name:
   terms_accepted = True,
  else:
   terms_accepted = False

# Send response to Airtable
head = {'Authorization': 'Bearer ' + api_key, "Content-Type": "application/json"}
data = {"records": [
    {
      "fields": {
        "Name": name, 
        "Email": email, 
        "Birthdate": str(birthdate), 
        "Address": address, 
        "Phone": str(phone.masked), 
        "ID_type": str(id_type), 
        "ID_number": str(id_number), 
        "ID_expiration": str(id_expiration), 
        "Weight": str(weight), 
        "Height": str(height), 
        "Under_care": str(under_care),
        "Reason_under_care": str(reason_under_care),
        "Hospitalized": str(hospitalized),
        "Reason_hospitalized": str(reason_hospitalized),
        "Medicated": str(medicated),
        "Reason_medicated": str(reason_medicated),
        "Diet": str(diet),
        "Reason_diet": str(reason_diet),
        "Smoker": str(smoker),
        "Drinker": str(drinker),
        "Pregnant_trying": str(pregnant_trying),
        "Allergies": str(allergies),
        "Allergies_other": str(allergies_other),
        "Concerns": str(concerns),
        "Country": str(country),
        "City": str(city)
    }}
  ]}
url = 'https://api.airtable.com/v0/appuAflHPcfsiCItG/Check-ins'
response = requests.post(url, json=data, headers=head)

display(f"Thanks, {name}! You're checked in and ready to go.")