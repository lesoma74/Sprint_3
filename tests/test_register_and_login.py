import pytest
import random
import string
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.utils import generate_test_data
from helpers.locators import RegisterPageLocators, LoginPageLocators
from helpers.urls import LOGIN_URL, HOME_URL, REGISTER_URL

def test_register_and_login(browser):
    name, email, password = generate_test_data()

    browser.get(REGISTER_URL)

    # Ввод имени
    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(name)

    # Ввод email
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    # Ввод пароля
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    # Нажать на кнопку "Зарегистрироваться"
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

    # Ожидание перехода на страницу входа
    WebDriverWait(browser, 20).until(
        EC.url_contains(LOGIN_URL)
    )

    # Вход с тестовыми данными
    browser.get(LOGIN_URL)

    # Поле ввода email
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    # Поле ввода пароля
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    # Кнопка входа
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    login_button.click()

    # Проверка URL после успешного входа
    WebDriverWait(browser, 20).until(
        EC.url_contains(HOME_URL)
    )
    assert HOME_URL in browser.current_url










