# Created by Satvik Jayalwal on 31/07/2025
# Feature file to verify AddBook functionality using Library API

Feature: Add and manage books using the Library API

  @library
  Scenario: Verify adding a book using AddBook API
    # Step: Prepare book details
    Given the Book details which needs to be added to Library
    # Step: Call the API endpoint
    When we execute the AddBook PostAPI method
    # Step: Validate the response and capture the book ID
    Then book is successfully added
    # Step: Confirm status code is 200 (Success)
    And  status code of response should be 200

  @library
  Scenario Outline: Add books dynamically with different ISBN and aisle values
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added

    Examples:
      | isbn  | aisle |
      | fdfee | 8948  |
      | powr  | 76333 |
