from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import REGISTER_URL
from locators import RegisterPageLocators  # Импорт класса с локаторами
from helpers.data import TestData  # Импорт класса с тестовыми данными

def test_successful_registration(browser):
    browser.get(REGISTER_URL)
    name, email, password = TestData.generate_test_data()

    # Заполнение формы регистрации
    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(name)

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()


def test_registration_with_empty_name(browser):
    browser.get(REGISTER_URL)
    email = TestData.generate_random_email()
    password = TestData.generate_random_password()

    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys("")

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()


def test_registration_with_invalid_email(browser):
    browser.get(REGISTER_URL)
    name = "John Doe"
    email = "john.doe.example.com"
    password = TestData.generate_random_password()

    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(name)

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

def test_registration_with_short_password(browser):
    browser.get(REGISTER_URL)
    name = "John Doe"
    email = TestData.generate_random_email()
    password = "12345"  # Короткий пароль

    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(name)

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

    # Проверка сообщения об ошибке о некорректном пароле
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR_MESSAGE)
    )
    assert "Некорректный пароль" in error_message.text

def test_registration_with_existing_user(browser):
    browser.get(REGISTER_URL)
    name = "John Doe"
    email = TestData.EXISTING_USER_EMAIL
    password = TestData.generate_random_password()

    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(name)

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

    # Проверка сообщения об ошибке о существующем пользователе
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators.EXISTING_USER_ERROR_MESSAGE)
    )
    assert "Такой пользователь уже существует" in error_message.text

