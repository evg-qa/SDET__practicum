import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker


@pytest.fixture
def options():
    options = Options()
    # options.add_argument("--window-size=1920,1200")
    # options.add_argument('--headless')
    return options

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=5)
    return wait

@pytest.fixture
@allure.title("Открыть браузер")
def driver(options):
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def random_first_name():
    return Faker().first_name()

@pytest.fixture
def random_last_name():
    return Faker().last_name()

@pytest.fixture
def random_mobile_number():
    faker = Faker()
    phone_number = ''
    for _ in range(10):
        phone_number += str(faker.random_digit())
    return phone_number

