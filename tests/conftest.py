import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Edge()  # Использовать нужный драйвер
    yield driver
    driver.quit()