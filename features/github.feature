# Created by Satvik Jayalwal on 31/07/2025
# Feature: GitHub API validation
# This feature validates GitHub repository access using authenticated API calls.

Feature: GitHub API validation

  # Scenario: Check if the GitHub session and authentication work correctly
  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200
