from base.basepage import BasePage
from locators.registration_page_locators import RegistrationPageLocators, RegistrationPagePopUpLocators


class RegistrationPage(BasePage):

    def fill_first_name_field(self, value):
        return self.is_visible(RegistrationPageLocators.FIRST_NAME).send_keys(value)

    def fill_last_name_field(self, value):
        return self.is_visible(RegistrationPageLocators.LAST_NAME).send_keys(value)

    def fill_email_field(self, value):
        return self.is_visible(RegistrationPageLocators.EMAIL).send_keys(value)

    def click_random_gender_radio_button(self):
        return self.click_btn(RegistrationPageLocators.RANDOM_GENDER_RADIO_BTN)

    def get_random_gender_text(self):
        locator = RegistrationPageLocators.RANDOM_GENDER_RADIO_BTN
        self.click_btn(locator)
        gender_text = self.get_text(locator)
        return gender_text

    def fill_mobile_phone_field(self, value):
        return self.is_visible(RegistrationPageLocators.MOBILE_PHONE).send_keys(value)

    def click_date_of_birth_field(self):
        return self.click_btn(RegistrationPageLocators.DATE_OF_BIRTH)

    def choose_calendar_data(self):
        return self.click_btn(RegistrationPageLocators.CALENDAR_DATA)

    def fill_subject_info_field(self, value):
        return self.is_visible(RegistrationPageLocators.SUBJECTS_INFO).send_keys(value)

    def click_random_hobby_checkbox(self):
        return self.click_btn(RegistrationPageLocators.SPORTS_CHECKBOX)

    def get_random_hobby_checkbox_text(self):
        locator = RegistrationPageLocators.SPORTS_CHECKBOX
        self.click_btn(locator)
        checkbox_text = self.get_text(locator)
        return checkbox_text

    def upload_picture(self, value):
        return self.is_clickable(RegistrationPageLocators.UPLOAD_PICTURE_BTN).send_keys(value)

    def fill_current_address_field(self, value):
        return self.is_visible(RegistrationPageLocators.CURRENT_ADDRESS).send_keys(value)

    def click_state_drop_down_menu(self):
        return self.click_btn(RegistrationPageLocators.SELECT_STATE)

    def select_state(self):
        return self.is_clickable(RegistrationPageLocators.STATE)

    def click_city_drop_down_menu(self):
        return self.click_btn(RegistrationPageLocators.SELECT_CITY)

    def select_city(self):
        return self.is_clickable(RegistrationPageLocators.CITY)

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")

    def click_submit_button(self):
        return self.click_btn(RegistrationPageLocators.SUBMIT_BTN)

    def get_pop_up_title(self):
        return self.get_text(RegistrationPagePopUpLocators.POP_UP_TITLE)

    def get_pop_up_table_values(self):
        text_value = []
        elements = self.elements_are_visible(RegistrationPagePopUpLocators.POP_UP_TABLE)
        for element in elements:
            text_value.append(element.text.strip(','))
        return text_value
