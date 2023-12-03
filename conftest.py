import pytest
from selenium import webdriver

@pytest.fixture(scope='session') # session = 1 раз за тестовую сессию
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
