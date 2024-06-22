from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.data import TestData
from urls import LOGIN_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from locators import LoginPageLocators, ForgotPasswordPageLocators, ResetPasswordPageLocators


def test_password_reset(browser):
    # Открыть страницу входа
    browser.get(LOGIN_URL)

    # Нажать на ссылку "Восстановить пароль"
    reset_password_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.RESET_PASSWORD_LINK)
    )
    reset_password_link.click()

    # Проверка URL после перехода на страницу восстановления пароля
    WebDriverWait(browser, 20).until(
        EC.url_contains(FORGOT_PASSWORD_URL)
    )
    assert FORGOT_PASSWORD_URL in browser.current_url

    # Ввод email для восстановления пароля
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(ForgotPasswordPageLocators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(TestData.REGISTERED_EMAIL)

    # Нажать на кнопку "Восстановить"
    reset_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(ForgotPasswordPageLocators.RESET_BUTTON)
    )
    reset_button.click()

    # Проверка URL после перехода на страницу ввода нового пароля
    WebDriverWait(browser, 20).until(
        EC.url_contains(RESET_PASSWORD_URL)
    )
    assert RESET_PASSWORD_URL in browser.current_url
    # Ввод нового пароля
    password = TestData.generate_random_password()
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(ResetPasswordPageLocators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)

        # Тестирование завершено на шаге, когда запрашивается ввод кода из письма










