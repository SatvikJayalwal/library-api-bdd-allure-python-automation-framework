import requests  # For making HTTP requests
import json      # For handling JSON data

# Send a GET request to fetch books by author name "Satvik Jayalwal"
response = requests.get(
    'http://216.10.245.166/Library/GetBook.php',
    params={'AuthorName': 'Satvik Jayalwal'}
)

# Convert the JSON response to a Python dictionary
json_response = response.json()

# Print the data type (should be a list of dictionaries)
print(type(json_response))

# Print the ISBN of the first book in the response
print(json_response[0]['isbn'])

# Assert the HTTP response code is 200 (OK)
assert response.status_code == 200

# Print response headers for debugging
print(response.headers)

# Assert the content type is JSON as expected
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Loop through the books and find the one with the specified ISBN
for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)  # Print the matching book details
        break

# Define the expected book details (change as needed)
expectedBook = {
    "book_name": "Learn API Automation with RestAssured",
    "isbn": "RGHCC",
    "aisle": "12239"
}

# Verify the actual book matches the expected one
assert actualBook == expectedBook

"""
How to Run the BDD Test Suite and Generate Allure Report:

1. Execute BDD tests using Behave and generate raw Allure results:
   > behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features/

2. Generate the Allure HTML report from the results directory:
   > allure generate allure-results/ -o allure-project-report/ --clean

3. Open the generated Allure report in your default web browser:
   > allure open allure-project-report/

Note:
- Ensure Allure is installed and added to your system PATH.
- The report will be stored in the 'allure-project-report/' directory.
"""

