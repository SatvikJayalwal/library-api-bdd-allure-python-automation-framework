Backend Automation Framework using Python (SDET Project)
This project demonstrates end-to-end backend automation using Python. It covers API testing, BDD automation framework (using behave), database validation, SSH interaction with Linux servers, file handling (JSON, CSV), and web scraping.

Note: This project does not use PyTest. All test cases are implemented using behave (a BDD framework).

Screenshot

![Allure Report Screenshot](Project%20Demo/Allure_Project_Report.png)

Demo Video

Watch the demo video here:  
📹 `Project_demo_with_allure_reports.mp4` located inside the `Project Demo/` folder.

Key Features

- JSON file parsing and creation
- CSV read/write automation
- API Testing with Python requests library
- CRUD operations: GET, POST, PUT, DELETE
- Database interaction using mysql.connector
- Full BDD framework setup using behave
- Dynamic payload creation using DB data
- SSH connectivity using paramiko
- Executing remote batch jobs via SSH
- Uploading/downloading files to/from Linux servers
- Web scraping using BeautifulSoup

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

BackEndAutomation :

1.  features/                       
│   1.1 AddBook.feature
│
2.  steps/               # Step implementations
│   2.1 steps_addBook.py
│
3.  utilities/                     # Utilities for DB, SSH, File IO, etc.
│   3.1 __init__.py
│   3.2 configurations.py
│   3.3 properties.ini
│   3.4 resources.py
│
├── allure-results/                # Output folder for raw Allure results
├── allure-project-report/         # Allure HTML report (after generation)
├── Project Demo/                  # Demo files (screenshot + video)
│   └── Allure_Project_Report.png
│   └── Project_demo_with_allure_reports.mp4
├── Library_API_Endpoint_Documentation.pdf
└── README.md
