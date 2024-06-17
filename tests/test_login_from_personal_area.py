import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_redirect_to_login_and_login(browser):
    try:
        # Открыть главную страницу
        browser.get("https://stellarburgers.nomoreparties.site/")

        # Нажать на кнопку "Личный кабинет"
        profile_link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"))
        )
        profile_link.click()

        # Проверка URL после перехода на страницу входа
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/login")
        )
        assert "https://stellarburgers.nomoreparties.site/login" in browser.current_url

        # Ввод email для входа
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='name']"))
        )
        email = "Antonov18@ya.ru"  # Заменить на свой email для тестирования
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute("value") == email

        # Ввод пароля для входа
        password_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='Пароль']"))
        )
        password = "123456"  # Заменить на свой пароль для тестирования
        password_input.clear()
        password_input.send_keys(password)
        assert password_input.get_attribute("value") == password

        # Нажать на кнопку "Войти"
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()

        # Проверка URL после успешного входа (на главной странице)
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/")
        )
        assert "https://stellarburgers.nomoreparties.site/" in browser.current_url

    except TimeoutException:
        pytest.fail("Failed to navigate and login to profile page.")



