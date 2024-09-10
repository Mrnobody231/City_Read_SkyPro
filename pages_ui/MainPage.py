from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from constants import BASE_URL


class MainPage:
    def __init__(self, browser: WebDriver):
        self.driver = browser
        self.driver.get(BASE_URL)
        self.actions = ActionChains(self.driver)

    @allure.step("Get website's current url")
    def get_url(self) -> str:
        return self.driver.current_url

    @allure.step("Click on whatever button: {locator}")
    def click(self, locator: str):
        self.driver.find_element(By.XPATH, locator).click()

    @allure.step("Get text from the element: {text}")
    def get_location_text(self, time_out: int, locator: str, text: str) -> str:
        WebDriverWait(self.driver, time_out).until(EC.text_to_be_present_in_element(
            (By.XPATH, locator), text))
        text = self.driver.find_element(By.XPATH, locator).text
        return text

    @allure.step("Insert {text} in the field")
    def write_text(self, locator: str, text: str):
        self.driver.find_element(By.XPATH, locator).send_keys(text)

    @allure.step("Get list of the books on the first page")
    def list_of_books_per_page(self, time_out: int, locator: str) -> str:
        all_books = WebDriverWait(self.driver, time_out).until(EC.visibility_of_all_elements_located(
            (By.XPATH, locator)))
        return str(len(all_books))

    @allure.step("Click on the element with Actions")
    def move_to_element_with_actions(self, time_out: int, locator: str):
        WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable((By.XPATH, locator)))
        element = self.driver.find_element(By.XPATH, locator)
        self.actions.move_to_element(element).click().perform()