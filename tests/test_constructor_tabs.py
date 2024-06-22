from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import HOME_URL
from locators import ConstructorPageLocators  # Импорт класса с локаторами


def test_buns_tab_display(browser):
    # Открываем страницу конструктора бургеров
    browser.get(HOME_URL)

    # Проверяем, что изначально активна вкладка "Булки"
    active_tab = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
    )
    initial_active_tab_text = active_tab.text
    assert "Булки" in initial_active_tab_text, "Ожидаемая вкладка 'Булки' не активна при открытии страницы"

    # Проверяем, что раздел (таб) отображается
    section_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB)
    )
    assert section_element.is_displayed(), "Таб 'Булки' не отображается на странице"


def test_sauces_tab_display(browser):
    # Открываем страницу конструктора бургеров
    browser.get(HOME_URL)

    # Нажимаем на вкладку "Соусы"
    tab = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
    )
    tab.click()

    # Ожидаем, что вкладка станет активной
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Соусы")
    )

    # Проверяем, что вкладка активна
    active_tab = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
    )
    clicked_tab_text = active_tab.text
    assert "Соусы" in clicked_tab_text, "Ожидаемая вкладка 'Соусы' не активна после переключения"

    # Проверяем, что раздел (таб) отображается
    section_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_TAB)
    )
    assert section_element.is_displayed(), "Таб 'Соусы' не отображается на странице"


def test_fillings_tab_display(browser):
    # Открываем страницу конструктора бургеров
    browser.get(HOME_URL)

    # Нажимаем на вкладку "Начинки"
    tab = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB)
    )
    tab.click()

    # Ожидаем, что вкладка станет активной
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Начинки")
    )

    # Проверяем, что вкладка активна
    active_tab = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
    )
    clicked_tab_text = active_tab.text
    assert "Начинки" in clicked_tab_text, "Ожидаемая вкладка 'Начинки' не активна после переключения"

    # Проверяем, что раздел (таб) отображается
    section_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.FILLINGS_TAB)
    )
    assert section_element.is_displayed(), "Таб 'Начинки' не отображается на странице"















































