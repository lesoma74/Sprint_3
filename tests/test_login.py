import pytest
import random
import string
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.utils import generate_random_email, generate_random_password  # импорт функций из helpers.utils
from helpers.data import REGISTERED_EMAIL, REGISTERED_PASSWORD  # импорт тестовых данных из helpers.data
from helpers.urls import LOGIN_URL, HOME_URL  # импорт URL-адресов из helpers.urls
from helpers.locators import LoginPageLocators



def test_positive_login(browser):
    email = REGISTERED_EMAIL  # зарегистрированный email
    password = REGISTERED_PASSWORD  # зарегистрированный пароль

    browser.get(LOGIN_URL)  # Использование URL из helpers.urls

    # Ввод email
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    # Ввод пароля
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    # Нажать кнопку "Войти"
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    login_button.click()

    # Проверка успешного входа
    WebDriverWait(browser, 20).until(
        EC.url_contains(HOME_URL)
    )
    assert HOME_URL in browser.current_url
def test_negative_login(browser):
    email = generate_random_email()
    password = generate_random_password()

    browser.get(LOGIN_URL)  # Использование URL из helpers.urls

    # Ввод email
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)

    # Ввод пароля
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

    # Нажать кнопку "Войти"
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    login_button.click()

    # Проверка неуспешного входа
    WebDriverWait(browser, 10).until(
        EC.url_to_be(LOGIN_URL)
    )
    assert browser.current_url == LOGIN_URL




