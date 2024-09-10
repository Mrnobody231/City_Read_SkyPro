from selenium import webdriver
import pytest
import allure

from pages_api.ApiCollection import ApiCollection
from pages_ui.MainPage import MainPage


@allure.step("Fixture to set Chrome driver")
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.step("Fixture to create an object of the MainPage class. UI")
@pytest.fixture
def main_page(browser):
    main_page = MainPage(browser)
    return main_page

@allure.step("Fixture to create an object of the ApiCollection class. API")
@pytest.fixture
def api():
    api = ApiCollection()
    return api