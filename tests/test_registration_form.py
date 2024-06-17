import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция для генерации случайного email
def generate_random_email(length=10, domain="example.com"):
    letters = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    email = f"{username}@{domain}"
    return email

# Функция для генерации случайного пароля
def generate_random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

@pytest.mark.parametrize("name, email, password", [
    ("John Doe", generate_random_email(), generate_random_password()),  # позитивная проверка
    ("", generate_random_email(), generate_random_password()),  # негативная проверка: пустое имя
    ("John Doe", "john.doe.example.com", generate_random_password()),  # негативная проверка: некорректный email
    ("John Doe", generate_random_email(), "12345"),  # негативная проверка: короткий пароль
    ("John Doe", "existing_user@example.com", generate_random_password())  # негативная проверка: пользователь уже существует
])
def test_registration_form(browser, name, email, password):
    browser.get("https://stellarburgers.nomoreparties.site/register")

    # Поле ввода имени
    name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
    )
    name_input.clear()
    name_input.send_keys(name)
    assert name_input.get_attribute("value") == name

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

    # Кнопка регистрации
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
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

