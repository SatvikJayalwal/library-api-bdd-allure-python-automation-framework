# BackEndAutomation

This project demonstrates API automation testing using Python, PyTest, Behave (BDD), and Allure Reports.  
It covers real-world use cases like POST, GET, PUT, and DELETE requests, and includes:

- Custom test reporting
- BDD-style test support
- Data-driven testing
- Modular framework structure

---

## Screenshot

![Allure Report Screenshot](Project%20Demo/Allure_Project_Report.png)

---

## Demo Video

Watch the demo video here:  
📹 `Project_demo_with_allure_reports.mp4` located inside the `Project Demo/` folder.

---

## Features

- Modular framework using `pytest` and `behave`
- Allure reporting integration for both unit and BDD tests
- `conftest.py` for common setup/teardown
- Organized test structure
- Configuration-driven test data

---

## Tech Stack

- Python
- PyTest
- Behave (BDD)
- Requests Library
- Allure Reports
- Git & GitHub

---

## How to Run the BDD Test Suite and Generate Allure Report

1. Execute BDD tests using Behave and generate raw Allure results:
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features/
Generate the Allure HTML report from the results directory:

bash
Copy
Edit
allure generate allure-results/ -o allure-project-report/ --clean
Open the generated Allure report in your default web browser:

bash
Copy
Edit
allure open allure-project-report/
Note:

Ensure Allure is installed and added to your system PATH.

The report will be stored in the allure-project-report/ directory.

Getting Started
Clone the repository
bash
Copy
Edit
git clone https://github.com/SatvikJayalwal/BackEndAutomation.git
cd BackEndAutomation
Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run PyTest tests
bash
Copy
Edit
pytest --alluredir=reports/
Generate Allure Report
bash
Copy
Edit
allure serve reports/
Project Structure
kotlin
Copy
Edit
BackEndAutomation/
├── data/
├── reports/
├── tests/
├── features/
│   ├── *.feature
│   └── steps/
├── utils/
├── conftest.py
├── requirements.txt
├── Project Demo/
│   ├── Allure_Project_Report.png
│   └── Project_demo_with_allure_reports.mp4
└── README.md
License
This project is licensed under the MIT License.

Author
Satvik Jayalwal
