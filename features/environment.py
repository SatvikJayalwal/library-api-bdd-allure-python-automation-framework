# Created by Satvik Jayalwal on 31/07/2025
# This script contains post-scenario cleanup for Library API tests

import requests  # Used to make HTTP requests to the API

# Hook that runs automatically after each scenario
def after_scenario(context, scenario):
    # Check if the scenario has the tag @library
    if "library" in scenario.tags:

        # Make a POST request to delete the book using its ID
        response_deleteBook = requests.post(
            'http://216.10.245.166/Library/DeleteBook.php',  # API endpoint for deleting a book
            json={
                "ID": context.bookId  # Book ID is retrieved from context set in previous step
            },
            headers={"Content-Type": "application/json"}  # Set content type for JSON data
        )

        # Verify that the status code is 200 (Success)
        assert response_deleteBook.status_code == 200

        # Convert response to JSON format
        res_json = response_deleteBook.json()

        # Print the confirmation message to console
        print(res_json["msg"])

        # Assert that the deletion message matches expected text
        assert res_json["msg"] == "book is successfully deleted"
