🚀 Cnarios Test Automation Framework

This repository contains an end-to-end UI Test Automation Framework built using Python, Selenium, and PyTest, following industry best practices like Page Object Model (POM) and data-driven testing.

📌 Project Overview

The framework is designed to automate web application testing with:
```
Clean and maintainable structure
Reusable components
Scalable test design
Data-driven approach using Excel
🛠️ Tech Stack
Language: Python
Automation Tool: Selenium WebDriver
Test Framework: PyTest
Design Pattern: Page Object Model (POM)
Data Handling: Excel (pandas / openpyxl)
Version Control: Git & GitHub
```
```
📁 Project Structure
Cnarios-Test_Automation/
│
├── tests/                 # Test cases
├── pages/                 # Page Object classes
├── utilities/             # Utility functions (Excel, config, etc.)
├── test_data/             # Excel files for data-driven testing
├── conftest.py            # PyTest fixtures
├── requirements.txt       # Dependencies
└── README.md
```
```
✅ Features
✔ Page Object Model (POM) implementation
✔ Data-driven testing using Excel
✔ Reusable utilities and helpers
✔ Cross-browser support (extendable)
✔ Implicit & Explicit waits handling
✔ File upload automation
✔ Frame handling and keyboard actions
✔ Clean and modular test structure
```
▶️ Setup Instructions
1. Clone the Repository
git clone https://github.com/avinashu199/Cnarios-Test_Automation.git
cd Cnarios-Test_Automation
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run Tests
pytest -v
📊 Test Data

Test data is maintained in Excel files:

URL data
File upload paths
Payment details

This enables data-driven testing for better coverage and flexibility.
```
🧪 Sample Test Scenarios
✅ File Upload functionality
✅ Payment form validation
✅ Checkbox interactions
✅ Frame switching
✅ Keyboard actions (Ctrl, Enter, etc.)
```
```
🔥 Best Practices Followed
Separation of concerns (Test vs Page vs Utility)
Reusable locators and methods
Explicit waits over hard waits
Clean coding standards
Scalable framework design
📈 Future Enhancements
Allure / Extent Reports integration
CI/CD integration (GitHub Actions / Jenkins)
API testing integration
```
👨‍💻 Author

Avinash Uppalapati

GitHub: https://github.com/avinashu199
⭐ Contribution

Feel free to fork, improve, and raise PRs 🚀

📄 License

This project is for learning and demonstration purposes.
