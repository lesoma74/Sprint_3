import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers.urls import HOME_URL
from helpers.locators import ConstructorPageLocators  # Импорт класса с локаторами

@pytest.mark.parametrize("section_title, tab_locator", [
    ("Соусы", ConstructorPageLocators.SAUCES_TAB),
    ("Начинки", ConstructorPageLocators.FILLINGS_TAB)
])
def test_tabs_display(browser, section_title, tab_locator):
    # Открываем страницу конструктора бургеров
    browser.get(HOME_URL)
    print("Открыта страница конструктора бургеров")

    # Проверяем, что изначально активна вкладка "Булки"
    active_tab = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
    )
    initial_active_tab_text = active_tab.text
    assert "Булки" in initial_active_tab_text, "Ожидаемая вкладка 'Булки' не активна при открытии страницы"
    print(f"Текущая активная вкладка: {initial_active_tab_text}")

    # Нажимаем на вкладку "Соусы" или "Начинки"
    print(f"Нажимаем на вкладку '{section_title}'")
    tab = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(tab_locator)
    )
    tab.click()

    # Добавим небольшую задержку для визуализации действия
    import time
    time.sleep(1)  # Задержка в одну секунду

    # Проверяем, что вкладка активна
    active_tab = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
    )
    clicked_tab_text = active_tab.text
    assert section_title in clicked_tab_text, f"Ожидаемая вкладка '{section_title}' не активна после переключения"
    print(f"Активная вкладка после клика: {clicked_tab_text}")

    # Проверяем, что раздел (таб) отображается
    section_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//h2[text()='{section_title}']"))
    )
    assert section_element.is_displayed(), f"Таб '{section_title}' не отображается на странице"
    print(f"Раздел '{section_title}' отображается на странице")















































