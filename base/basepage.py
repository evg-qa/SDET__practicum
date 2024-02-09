import datetime
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_visible(self, locator, timeout=10):
        self.go_to_element(self.is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_btn(self, locator):
        self.is_clickable(locator).click()

    def get_text(self, locator):
        return self.element_is_visible(locator, 10).text

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")
        screenshot_name = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\evg\\Desktop\\Projects\\sdet_practicum\\screenshots\\' + screenshot_name)
        print("Screenshot: " + screenshot_name)







