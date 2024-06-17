import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Использовать нужный драйвер
    yield driver
    driver.quit()