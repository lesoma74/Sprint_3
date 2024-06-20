import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.utils import generate_test_data, generate_random_email, generate_random_password
from helpers.data import EXISTING_USER_EMAIL
from helpers.urls import REGISTER_URL
from helpers.locators import RegisterPageLocators



@pytest.mark.parametrize("name, email, password", [
    generate_test_data(),  # позитивная проверка
    ("", generate_random_email(), generate_random_password()),  # негативная проверка: пустое имя
    ("John Doe", "john.doe.example.com", generate_random_password()),  # негативная проверка: некорректный email
    ("John Doe", generate_random_email(), "12345"),  # негативная проверка: короткий пароль
    ("John Doe", EXISTING_USER_EMAIL, generate_random_password())  # негативная проверка: пользователь уже существует
])
def test_registration_form(browser, name, email, password):
    browser.get(REGISTER_URL)

    # Поле ввода имени
    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(name)

    # Поле ввода email
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    # Поле ввода пароля
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    # Кнопка регистрации
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

    # Проверка, что сообщение об ошибке отображается только при некорректном пароле
    if len(password) < 6:
        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']"))
        )
        assert "Некорректный пароль" in error_message.text
    else:
        # Проверка, что сообщение об ошибке отсутствует, если пароль корректный
        error_messages = browser.find_elements(By.XPATH,
                                               "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")
        assert len(error_messages) == 0

    # Проверка, что сообщение об ошибке отображается при уже существующем пользователе
    if email == "existing_user@example.com":
        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(@class, 'input__error') and text()='Такой пользователь уже существует']"))
        )
        assert "Такой пользователь уже существует" in error_message.text
    else:
        # Проверка, что сообщение об ошибке отсутствует, если email не существует
        error_messages = browser.find_elements(By.XPATH,
                                               "//p[contains(@class, 'input__error') and text()='Такой пользователь уже существует']")
        assert len(error_messages) == 0

