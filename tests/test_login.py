import pytest
import random
import string
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_random_email(length=10, domain="example.com"):
    letters = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    email = f"{username}@{domain}"
    return email

def generate_random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def test_positive_login(browser):
    email = "Antonov18@ya.ru"  # зарегистрированный email
    password = "password123"  # зарегистрированный пароль

    browser.get("https://stellarburgers.nomoreparties.site/login")

    try:
        # Ввод email
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute("value") == email

        # Ввод пароля
        password_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Пароль']/following-sibling::input"))
        )
        password_input.clear()
        password_input.send_keys(password)
        assert password_input.get_attribute("value") == password

        # Нажать кнопку "Войти"
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Проверка успешного входа
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/")
        )
        assert "https://stellarburgers.nomoreparties.site/" in browser.current_url

    except TimeoutException:
        pytest.fail("Login was expected to succeed, but it did not.")

def test_negative_login(browser):
    email = generate_random_email()
    password = generate_random_password()

    browser.get("https://stellarburgers.nomoreparties.site/login")

    try:
        # Ввод email
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute("value") == email

        # Ввод пароля
        password_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Пароль']/following-sibling::input"))
        )
        password_input.clear()
        password_input.send_keys(password)
        assert password_input.get_attribute("value") == password

        # Нажать кнопку "Войти"
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Проверка неуспешного входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    except TimeoutException:
        pytest.fail("Login was expected to fail, but it did not.")





