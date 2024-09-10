from allure_commons.types import Severity
import allure

from pages_ui import MainPage


@allure.severity(Severity.CRITICAL)
@allure.title("Get website's url")
@allure.description("Ckeck if the current url is the same as BASE_URL")
@allure.feature("Get")
def test_get_url(browser, main_page: MainPage):
    url = main_page.get_url()
    with allure.step("Check if BASE_URL is the same as we get"):
        assert "https://www.chitai-gorod.ru/" in url

@allure.severity(Severity.CRITICAL)
@allure.title("Change location")
@allure.description("Select your desirable location from the list")
@allure.feature("Select")
def test_change_location(browser, main_page: MainPage):
    main_page.click("//div[@class='button change-city__button change-city__button--cancel light-blue']")
    main_page.click("//div[@class='app-select city-modal__select']")
    main_page.click("(//div[@class='app-select__dropdown']/*/*)[2]")
    main_page.click("(//ul[@class='city-modal__popular']/*)[2]")
    with allure.step("Get selected location's text"):
        location_text = main_page.get_location_text(4,
                                "//span[@class='header-city__title']",
                                "Казахстан, Астана")
    with allure.step("Check if the locaton's text is the same as was selected"):
        assert location_text == "Казахстан, Астана"

@allure.severity(Severity.BLOCKER)
@allure.title("Unsuccessfully authorization")
@allure.description("Write incorrect 5 digits code in the message stage")
@allure.feature("Write")
def test_authorization_with_incorrect_code(browser, main_page: MainPage):
    main_page.click("//span[text()='Войти']")
    main_page.write_text("//label[@class='phone-input']", "+7 966 666-66-66")
    main_page.click("//span[text()='получить код']")
    main_page.write_text("//div[@class='app-input']/*", "12345")
    with allure.step("Get error text by writing incorrect message code"):
        sms_error = main_page.get_location_text(4,
                                "//span[@class='sms-form__error']",
                                "Пожалуйста, проверьте код из СМС")
    with allure.step("Check if error text is the same as 'Пожалуйста, проверьте код из СМС'"):
        assert sms_error == "Пожалуйста, проверьте код из СМС"

@allure.severity(Severity.NORMAL)
@allure.title("List of the books per page")
@allure.description("Get the length of the books displayed per page")
@allure.feature("Get")
def test_books_per_page(browser, main_page: MainPage):
    main_page.write_text("//input[@class='header-search__input']", "1984")
    main_page.click("//button[@type='submit']")
    with allure.step("Get the list of the books displayed on the first page"):
        total_books = main_page.list_of_books_per_page(5,"(//div[@class='product-title__head' and ""contains(text(),"
                                                         " '1984')])[position() <='48']")
    with allure.step("Check if the books length is equal 48"):
        assert total_books == "48"

@allure.severity(Severity.CRITICAL)
@allure.title("Incorrect data in the search box")
@allure.description("Write incorrect data in the search box to get error message")
@allure.feature("Get")
def test_search_result_with_incorrect_input(browser, main_page: MainPage):
    main_page.write_text("//input[@class='header-search__input']", "asdfgweqwdw")
    main_page.click("//button[@type='submit']")
    with allure.step("Get error message's text after writing wrong data in the search box"):
        inform_message =  main_page.get_location_text(4,
                                                  "//div[@class='catalog-empty-result__description']/*",
                                                  "Похоже, у нас такого нет")
    with allure.step("Check if error message is the same as 'Похоже, у нас такого нет'"):
        assert inform_message == "Похоже, у нас такого нет"

@allure.severity(Severity.NORMAL)
@allure.title("Filtering books")
@allure.description("The option to select a desired filter for finding books")
@allure.feature("Get")
def test_sort_with_filter(browser, main_page: MainPage):
    main_page.click("//div[@class='button change-city__button change-city__button--accept blue']")
    main_page.click("//button[@class='catalog__button']")
    main_page.click("//span[@class='categories-menu__item-title' and contains(text(), 'Манга')]")
    with allure.step("Get the list of the books displayed on the first page"):
        total_books = main_page.list_of_books_per_page(8, "//div[@class='product-title__head']")
    with allure.step("Check if the books length is equal 48"):
        assert total_books == "48"
    with allure.step("Retrieve the name of the first book"):
        book_title = main_page.get_location_text(8,
                                             "//div[@class='product-title__head']",
                                             "Смерть - единственный конец для злодейки."
                                             " Том 5 (Villains Are Destined to Die / Единственный конец"
                                             " злодейки - смерть). Новелла")
    with allure.step("Check if the first book name title is 'Смерть - единственный конец для злодейки. "
                     "Том 5 (Villains Are Destined to Die / Единственный конец злодейки - смерть). Новелла'"):
        assert book_title == ("Смерть - единственный конец для злодейки. Том 5 (Villains Are Destined to Die"
                          " / Единственный конец злодейки - смерть). Новелла")