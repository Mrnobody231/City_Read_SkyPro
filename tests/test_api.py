from allure_commons.types import Severity
import allure

from pages_api import ApiCollection


@allure.severity(Severity.CRITICAL)
@allure.title("Get books written in the params")
@allure.description("Retrieve the list of books by the specified name")
@allure.feature("Get")
def test_get_book(api: ApiCollection):
    result = api.get_book("1984")
    with allure.step("Check if the getting list is not empty"):
        assert result[0] is not None
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200

@allure.severity(Severity.NORMAL)
@allure.title("Get books by the filter")
@allure.description("Retrieve the list of books by using the filter")
@allure.feature("Get")
def test_get_book_by_filter(api: ApiCollection):
    result = api.get_books_by_filter("1")
    with allure.step("Check if title is 'Фэнтези'"):
        assert result[0] == 'Фэнтези'
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200

@allure.severity(Severity.NORMAL)
@allure.title("Get books by the category")
@allure.description("Retrieve the list of books by using the category")
@allure.feature("Get")
def test_get_book_by_category(api: ApiCollection):
    result = api.books_by_categories({'slug' : '110685'})
    with allure.step("Check if title is 'Ежедневники'"):
        assert result[0] == "Ежедневники"
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200

@allure.severity(Severity.BLOCKER)
@allure.title("Get books without API_Token")
@allure.description("Get the list of books without inserting a token in the headers")
@allure.feature("Get")
def test_get_book_with_no_token(api: ApiCollection):
    result = api.get_book_no_token("1984")
    with allure.step("Check if the status is equal 401"):
        assert result == 401

@allure.severity(Severity.CRITICAL)
@allure.title("Add book to the cart")
@allure.description("Click button 'Купить' to add the book to the cart")
@allure.feature("Add")
def test_add_to_cart(api: ApiCollection):
    result = api.add_to_cart({"id": 2978800, "adData": {"item_list_name": "search", "product_shelf": ""}})
    with allure.step("Check if the status is equal 200"):
        assert result == 200

@allure.severity(Severity.CRITICAL)
@allure.title("Delete book from the cart")
@allure.description("Click icon with trash to delete the book from the cart")
@allure.feature("Delete")
def test_delete_from_cart(api: ApiCollection):
    api.get_book("1984")
    api.add_to_cart({"id":2942503,"adData":{"item_list_name":"search","product_shelf":""}})
    book_id = api.get_cart()
    empty_cart = api.delete_from_cart(book_id)
    with allure.step("Check if the status is equal 204"):
        assert empty_cart == 204