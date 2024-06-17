Описание локаторов

    # Локатор для поля ввода имени на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Локатор для поля ввода email на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Локатор для поля ввода пароля на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Локатор для кнопки "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")


    # Локатор для поля ввода email на странице входа
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Локатор для поля ввода пароля на странице входа
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Локатор для кнопки "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Локатор для ссылки "Восстановить пароль" на странице входа
    RESET_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, '/forgot-password')]")


    # Локатор для поля ввода email на странице восстановления пароля
    EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text' and @name='name']")
    # Локатор для кнопки "Восстановить" на странице восстановления пароля
    RESET_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']")

    # Локатор для кнопки "Личный кабинет" на главной странице
    PROFILE_LINK = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
    # Локатор для кнопки "Выход" на странице профиля
    LOGOUT_BUTTON = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']")


    # Локатор для кнопки "Конструктор" на главной странице
    CONSTRUCTOR_LINK = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    # Локатор для кнопки "Stellar Burgers"
    STELLAR_BURGERS_LINK = (By.CSS_SELECTOR, 'svg[viewBox="0 0 290 50"]')


    # Локаторы для разделов конструктора бургеров
    SECTIONS = {
        "Булки": (By.XPATH, "//h2[text()='Булки']"),
        "Соусы": (By.XPATH, "//h2[text()='Соусы']"),
        "Начинки": (By.XPATH, "//h2[text()='Начинки']")
    }


