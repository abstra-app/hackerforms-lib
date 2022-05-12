from hackerforms import *
import requests
import json
from datetime import datetime

display("Hi! Welcome to our Expense Approver.",
        button_text="Let's get started")

title = read("What is the title of this expense?")

value = read_number("How much was this expense?")

recurring = read_multiple_choice(
    "Is this a monthly recurring expense?",
    [{'label': 'yes', 'value': True}, {'label': 'no', 'value': False}]
)

id_department = read_multiple_choice(
    "To which department does this expense belong?",
    [
        {'label': 'Marketing', 'value': 1},
        {'label': 'Sales', 'value': 2},
        {'label': 'Operations', 'value': 3},
        {'label': 'Product', 'value': 4},
        {'label': 'Human Resources', 'value': 5},
        {'label': 'Engineering', 'value': 6}
    ]
)

# get department budget from database
department = requests.post(
    "https://INSERT_API_URL_HERE",
    json={'iddepartment': int(id_department)}
)
department = department.json()[0]
department_name = department['name']
budget = department['budget']

# check if enough budget remains, if not jump to end
if value > budget:
    approved = False
else:
    approved = True

if approved == True:
    description = read("Briefly describe what this expense is for.")
    type = read_multiple_choice(
        "What type of expense is this?",
        [
            'tool',
            'freelancer',
            'reimbursement',
            'misc'
        ]
    )

    due = read_date("When is this expense due?")
    newexpense = requests.post(
        "https://INSERT_API_URL_HERE",
        json={
            "name": title,
            "description": description,
            "type": type,
            "value": value,
            "recurring_monthly": recurring,
            "due": due.strftime('%Y-%m-%d'),
        }
    )
    display("We've registered this expense succesfully. Thanks! See ya next time.")
else:
    display(
        f"Sorry, the budget for the {department_name} department is not sufficient to cover this expense. Please speak to your manager."
    )
