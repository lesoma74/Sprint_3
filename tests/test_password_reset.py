import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_password_reset(browser):
    # Открыть страницу входа
    browser.get("https://stellarburgers.nomoreparties.site/login")

    try:
        # Нажать на ссылку "Восстановить пароль"
        reset_password_link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/forgot-password')]"))
        )
        reset_password_link.click()

        # Проверка URL после перехода на страницу восстановления пароля
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/forgot-password")
        )
        assert "https://stellarburgers.nomoreparties.site/forgot-password" in browser.current_url

        # Ввод email для восстановления пароля
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text' and @name='name']"))
        )
        email = "lesoma18@yandex.ru"  # заменить на актуальный email для тестирования восстановления пароля
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute("value") == email

        # Нажать на кнопку "Восстановить"
        reset_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']"))
        )
        reset_button.click()

        # Проверка URL после перехода на страницу ввода нового пароля
        WebDriverWait(browser, 20).until(
            EC.url_contains("https://stellarburgers.nomoreparties.site/reset-password")
        )
        assert "https://stellarburgers.nomoreparties.site/reset-password" in browser.current_url

        # Тестирование завершено на шаге, когда запрашивается ввод кода из письма
        # Добавить код для ввода пароля и кода из письма здесь, если есть валидный код

        # Ввод кода из письма
        #code_input = WebDriverWait(browser, 10).until(
            #EC.presence_of_element_located((By.XPATH,
                                            #"//input[@class='text input__textfield text_type_main-default' and @type='text' and @name='token']"))
        #)
        #code = "123456"  # заменить на реальный код из письма
        # code_input.clear()
        # code_input.send_keys(code)
        # assert code_input.get_attribute("value") == code
        #
        # # Ввод нового пароля
        # new_password_input = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='password']"))
        # )
        # new_password = "new_secure_password"  # заменить на желаемый новый пароль
        # new_password_input.clear()
        # new_password_input.send_keys(new_password)
        # assert new_password_input.get_attribute("value") == new_password
        #
        # # Нажать на кнопку "Сохранить"
        # save_button = WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Сохранить']"))
        # )
        # save_button.click()
        #
        # # Проверка URL после успешного восстановления пароля
        # WebDriverWait(browser, 20).until(
        #     EC.url_contains("https://stellarburgers.nomoreparties.site/login")
        # )
        # assert "https://stellarburgers.nomoreparties.site/login" in browser.current_url

    except TimeoutException:
        pytest.fail("Failed to navigate through password reset process.")







