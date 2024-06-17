import pytest
import random
import string
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def test_register_and_login(browser):
    random_string = generate_random_string()
    name = f"TestUser{random_string}"
    email = f"test{random_string}@example.com"
    password = "password123"

    browser.get("https://stellarburgers.nomoreparties.site/register")

    try:
        # Ввод имени
        name_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
        )
        name_input.clear()
        name_input.send_keys(name)
        assert name_input.get_attribute("value") == name

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

        # Нажать на кнопку "Зарегистрироваться"
        register_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
        )
        register_button.click()

        # Ожидание перехода на страницу входа
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/login")
        )
        assert "https://stellarburgers.nomoreparties.site/login" in browser.current_url

        # Вход с тестовыми данными
        # Поле ввода email
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute("value") == email

        # Поле ввода пароля
        password_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Пароль']/following-sibling::input"))
        )
        password_input.clear()
        password_input.send_keys(password)
        assert password_input.get_attribute("value") == password

        # Кнопка входа
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Проверка URL после успешного входа
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/")
        )
        assert "https://stellarburgers.nomoreparties.site/" in browser.current_url

    except TimeoutException:
        pytest.fail("Failed to navigate to the registration page or login page.")






