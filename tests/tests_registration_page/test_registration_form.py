import allure
from pages.pages_registration_page import RegistrationPage
from data.registration_page_urls import REGISTRATION_PAGE_URL
from data.registration_page_data import EMAIL, DATE_OF_BIRTH, SUBJECTS, HOBBIES, FILE_PATH, CURRENT_ADDRESS,\
    PICTURE, STATE, CITY, SUCCESS_POP_UP_TITLE


@allure.title("Кейс. Заполнение формы регистрации")
@allure.description("Заполнение данными регистрационной формы - проверка заголовка, полученных значений в поп ап окне")
def test_filling_registration_form(driver, random_first_name, random_last_name, random_mobile_number):

    with allure.step("Перейти на страницу входа: https://demoqa.com/automation-practice-form"):
        page = RegistrationPage(driver, url=REGISTRATION_PAGE_URL)
        page.open()

    with allure.step("1. Заполнить поле First Name произвольной строкой"):
        page.fill_first_name_field(random_first_name)

    with allure.step("2. Заполнить поле Last Name произвольной строкой"):
        page.fill_last_name_field(random_last_name)

    with allure.step("3. Заполнить поле Email строкой формата name@example.com"):
        page.fill_email_field(EMAIL)

    with allure.step("4. Выбрать любое значение в Gender с помощью переключателя"):
        random_gender = page.get_random_gender_text()

    with allure.step("5. Заполнить поле Mobile произвольными 10 цифрами"):
        page.fill_mobile_phone_field(random_mobile_number)

    with allure.step("6. Заполнить поле Date of birth произвольной датой с помощью всплывающего календаря"):
        page.click_date_of_birth_field()
        page.choose_calendar_data()

    with allure.step("7. Заполнить поле Subjects произвольной строкой"):
        page.fill_subject_info_field(SUBJECTS)

    with allure.step("8. Загрузить любое изображение в поле Picture"):
        page.upload_picture(FILE_PATH)

    with allure.step("9. Заполнить поле Current Address произвольной строкой"):
        page.fill_current_address_field(CURRENT_ADDRESS)

    with allure.step("10.Выбрать любое значение в Select State с помощью выпадающего списка"):
        page.click_state_drop_down_menu()
        page.select_state().click()

    with allure.step("11.Выбрать любое значение в Select City с помощью выпадающего списка"):
        page.click_city_drop_down_menu()
        page.select_city().click()

    with allure.step("12.Нажать кнопку Submit"):
        page.remove_footer()
        page.click_submit_button()

    expected_values = [
        f'{random_first_name} {random_last_name}', EMAIL, random_gender, random_mobile_number, DATE_OF_BIRTH,
        SUBJECTS, HOBBIES, PICTURE, CURRENT_ADDRESS, f'{STATE} {CITY}']

    with allure.step("1.Проверка отображения всплывающего окна с заголовком Thanks for submitting the form"):
        pop_up_title_text = page.get_pop_up_title()
        assert pop_up_title_text == SUCCESS_POP_UP_TITLE, \
            "Pop up title is not displayed correctly or contains unexpected text"

    with allure.step("2.Проверка отображения ранее введенных данных на их актуальность"):
        actual_values = page.get_pop_up_table_values()
        assert actual_values == expected_values, \
            "The values in the pop up table aren`t the same as those filled in the registration form"


