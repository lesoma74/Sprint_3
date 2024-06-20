import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.urls import HOME_URL
from helpers.locators import ConstructorPageLocators  # Предположим, что локаторы хранятся в отдельном файле

@pytest.mark.parametrize("section_title", ["Булки", "Соусы", "Начинки"])
def test_tabs_display(browser, section_title):
    try:
        # Открываем страницу конструктора бургеров
        browser.get(HOME_URL)

        # Ожидаем загрузки всех табов и проверяем их наличие
        section_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, ConstructorPageLocators.get_section_title_xpath(section_title)))
        )

        # Проверяем, что раздел (таб) отображается
        assert section_element.is_displayed(), f"Таб '{section_title}' не отображается на странице"

    except TimeoutException as e:
        pytest.fail(f"TimeoutException occurred: {e}")



































