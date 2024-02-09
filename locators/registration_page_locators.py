from selenium.webdriver.common.by import By
import random

class RegistrationPageLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    RANDOM_GENDER_RADIO_BTN = (By.XPATH, f"//label[@for='gender-radio-{random.randint(1, 3)}']")
    MALE_RADIO_BTN = (By.XPATH, "//label[@for='gender-radio-1']")
    FEMALE_RADIO_BTN = (By.CSS_SELECTOR, "input#gender-radio-2")
    OTHER_RADIO_BTN = (By.CSS_SELECTOR, "input#gender-radio-3")
    MOBILE_PHONE = (By.CSS_SELECTOR, 'input#userNumber')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input#dateOfBirthInput")
    CALENDAR_DATA = (By.XPATH, "//div[@aria-label='Choose Sunday, January 28th, 2024']")
    SUBJECTS_INFO = (By.XPATH, "//input[@id='subjectsInput']")
    RANDOM_HOBBIES_CHECKBOX = (By.ID, f"hobbies-checkbox-{random.randint(1, 3)}")
    SPORTS_CHECKBOX = (By.ID, "hobbies-checkbox-1")
    READING_CHECKBOX = (By.ID, "hobbies-checkbox-2")
    MUSIC_CHECKBOX = (By.ID, "hobbies-checkbox-3")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    UPLOAD_PICTURE_BTN = (By.CSS_SELECTOR, "input[type='file']")
    SELECT_STATE = (By.ID, 'state')
    STATE = (By.ID, 'react-select-3-option-2')
    SELECT_CITY = (By.ID, 'city')
    CITY = (By.ID, 'react-select-4-option-0')
    SUBMIT_BTN = (By.ID, 'submit')


class RegistrationPagePopUpLocators:
    POP_UP_TITLE = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    POP_UP_TABLE = (By.CSS_SELECTOR, "div.modal-body > div > table > tbody > tr > td:nth-child(2)")


