# Author: Satvik Jayalwal

# Importing required libraries
import requests
from behave import *  # BDD step implementation
import os
import sys

# Ensuring the project root path is added to sys.path to resolve module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importing custom payloads and utility functions
from payLoad import *  # Function to prepare request payload
from utilities.resources import *  # API endpoint resources
from utilities.configurations import *  # Config reader (e.g., endpoint, credentials)


@given('the Book details which needs to be added to Library')
def step_impl(context):
    # Constructing the complete API URL using endpoint and resource
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}  # Setting headers
    # Creating request payload with hardcoded ISBN and aisle
    context.payLoad = addBookPayload("manfdfppt", "4373")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    # Sending a POST request with the book payload
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    # Parsing the response and checking the message
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']  # Storing book ID for future use
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"  # Validation


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    # Creating payload dynamically from feature file params
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    # Setting up a session with GitHub credentials
    context.se = requests.session()
    # Use your own GitHub username and token in getPassword()
    context.se.auth = ('satvikjayalwal', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    # Hitting the GET endpoint to fetch repositories
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    # Verifying if the returned HTTP status code is as expected
    print(context.response.status_code)
    assert context.response.status_code == statusCode
