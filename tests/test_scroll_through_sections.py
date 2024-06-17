import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scroll_through_sections(browser):
    try:
        # Открываем страницу конструктора бургеров
        browser.get("https://stellarburgers.nomoreparties.site/")

        # Определяем разделы по тексту заголовков
        sections = ["Булки", "Соусы", "Начинки"]

        # Проходим по каждому разделу и скроллируем до него
        for section in sections:
            section_element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//h2[text()='{section}']"))
            )
            browser.execute_script("arguments[0].scrollIntoView();", section_element)
            assert section_element.is_displayed()

    except TimeoutException as e:
        pytest.fail(f"Не удалось выполнить скроллинг или проверить наличие разделов. Ошибка TimeoutException: {e}")












