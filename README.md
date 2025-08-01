Backend Automation Framework using Python (SDET Project)
This project demonstrates end-to-end backend automation using Python. It covers API testing, BDD automation framework (using behave), database validation, SSH interaction with Linux servers, file handling (JSON, CSV), and web scraping.

Note: This project does not use PyTest. All test cases are implemented using behave (a BDD framework).

Project Demo
Screenshot of Allure Report

Demo Video
Watch the Demo

Key Features
JSON file parsing and creation

CSV read/write automation

API Testing with Python requests library

CRUD operations: GET, POST, PUT, DELETE

Database interaction using mysql.connector

Full BDD framework setup using behave

Dynamic payload creation using DB data

SSH connectivity using paramiko

Executing remote batch jobs via SSH

Uploading/downloading files to/from Linux servers

Web scraping using BeautifulSoup

How to Run the BDD Test Suite and Generate Allure Report
bash
Copy
Edit
# 1. Run the BDD tests and generate Allure raw results:
behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features/

# 2. Generate the HTML report:
allure generate allure-results/ -o allure-project-report/ --clean

# 3. Open the Allure report:
allure open allure-project-report/
- Make sure Allure is installed and available in your system PATH
- The report will be available at: allure-project-report/

Course Overview (Covered in this project)
This project is built as part of a Python SDET (Software Development Engineer in Test) course. The course covers:

- API Automation (GET, POST, PUT, DELETE)

- JSON, CSV parsing utilities

- BDD Framework development (behave)

- MySQL database operations using Python

- SSH automation via paramiko

- Remote Linux command execution

- File transfer to/from remote servers

- Web scraping for data extraction

- Folder Structure
graphql
Copy
Edit
BackEndAutomation/
│
├── features/                       # BDD feature files
│   └── AddBook.feature
│
├── stepDefinitions/               # Step implementations
│   └── steps_addBook.py
│
├── utilities/                     # Utilities for DB, SSH, File IO, etc.
│   └── dbUtils.py
│   └── sshUtils.py
│   └── jsonHandler.py
│   └── csvHandler.py
│
├── allure-results/                # Output folder for raw Allure results
├── allure-project-report/         # Allure HTML report (after generation)
├── Project Demo/                  # Demo files (screenshot + video)
│   └── Allure_Project_Report.png
│   └── Project_demo_with_allure_reports.mp4
├── Library_API_Endpoint_Documentation.pdf
└── README.md
