# SDET__practicum

## Test Task - for admission to the sdet practicum

1. Choose a programming language - Java (version 11 or 17 recommended) or Python (version 3.10 recommended) to create a project of UI tests based on the described test cases below.
2. Use the following in the project:
   - Selenium WebDriver (preferably using Chrome browser).
   - When searching for elements on the page, use at least one selector from the following: css, xpath, id.
   - Choose one of the testing frameworks: Java - TestNG, JUnit 4/5, Python - pytest.
   - Choose one of the build systems (for Java): Maven, Gradle.
3. Format the results as a project on GitHub.
4. It is advisable to use the Page Object Model design pattern in the project.
5. Implementation of reporting on passed tests through Allure is welcomed but not mandatory.

## Test Case: Registration Form Submission

### Preconditions:
1. Open the browser.
2. Go to the login page: https://demoqa.com/automation-practice-form.

### Steps:
1. Fill in the "First Name" field with an arbitrary string.
2. Fill in the "Last Name" field with an arbitrary string.
3. Fill in the "Email" field with a string in the format name@example.com.
4. Select any value in the "Gender" field using the toggle switch.
5. Fill in the "Mobile" field with any 10 digits.
6. Fill in the "Date of Birth" field with an arbitrary date using the pop-up calendar.
7. Fill in the "Subjects" field with an arbitrary string.
8. Upload any image to the "Picture" field.
9. Fill in the "Current Address" field with an arbitrary string.
10. Select any value in the "Select State" field using the dropdown list.
11. Select any value in the "Select City" field using the dropdown list.
12. Click the "Submit" button.

### Expected Result:
1. A pop-up window with the title "Thanks for submitting the form" will appear.
2. The previously entered values will be displayed in the table on the window.

--- 

# Project setup

#### Configuration:
- Clone the repository to your computer.
- Navigate to the root folder of the project.
- Create a virtual environment:
```
python -m venv venv
```
- Activate the virtual environment:
```
source venv/Scripts/activate
```

#### Dependencies:

- Install dependencies:
```
pip install -r requirements.txt
```

#### Running automated tests

- Execute the following command to run the tests:
```
pytest -s -v
```

#### Generating and running allure reports

- Execute the following command to run the tests:
```
pytest -s -v --alluredir allure-results
```

- Execute the following command to view the report:
```
allure serve allure-results
```
