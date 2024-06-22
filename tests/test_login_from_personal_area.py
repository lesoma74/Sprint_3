from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.data import TestData
from urls import LOGIN_URL, HOME_URL
from locators import LoginPageLocators, ProfilePageLocators

def test_redirect_to_login_and_login(browser):
    # Открыть главную страницу
    browser.get(HOME_URL)

    # Нажать на кнопку "Личный кабинет"
    profile_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(ProfilePageLocators.PROFILE_LINK)
     )
    profile_link.click()

    # Проверка URL после перехода на страницу входа
    WebDriverWait(browser, 20).until(
        EC.url_contains(LOGIN_URL)
    )
    assert LOGIN_URL in browser.current_url

    # Ввод email для входа
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(TestData.REGISTERED_EMAIL)

    # Ввод пароля для входа
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(TestData.REGISTERED_PASSWORD)

    # Нажать на кнопку "Войти"
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    login_button.click()

    # Проверка URL после успешного входа (на главной странице)
    WebDriverWait(browser, 20).until(
        EC.url_contains(HOME_URL)
    )
    assert HOME_URL in browser.current_url





