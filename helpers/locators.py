from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESET_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, '/forgot-password')]")
    LOGOUT_BUTTON = (By.XPATH,
                     "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']")


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text' and @name='name']")
    RESET_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']")

class ResetPasswordPageLocators:
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")
