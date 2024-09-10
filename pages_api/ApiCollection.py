import requests
import allure

from constants import API_URL, API_KEY


class ApiCollection:
    def __init__(self, url=API_URL):
        self.url = url

    @allure.step("Get list of the books with params: {my_params} and check the status code")
    def get_book(self, my_params: str) -> list:
       resp = requests.get(self.url + "v1/recommend/semantic", headers=API_KEY, params=my_params)
       status = resp.status_code
       return [resp.json(), status]

    @allure.step("Get list of the books with params: {my_params}, by filtering them and check the status code")
    def get_books_by_filter(self, my_params: str) -> list:
        resp = requests.get(self.url + "v2/products",  headers=API_KEY, params=my_params)
        status = resp.status_code
        return [resp.json()["data"][0]["attributes"]["category"]["title"], status]

    @allure.step("Get list of the books with params: {my_params}, by the category and check the status code")
    def books_by_categories(self, my_params: dict) -> list:
        resp = requests.get(self.url + "v1/categories/tree",  headers=API_KEY, params=my_params)
        status = resp.status_code
        return [resp.json()["data"]["info"]["title"], status]

    @allure.step("Get list of the books with params: {my_params}, without API_KEY and check the status code")
    def get_book_no_token(self, my_params: str) -> int:
        resp = requests.get(self.url + "v1/categories/tree", params=my_params)
        return resp.status_code

    @allure.step("Add book to the cart with json: {book} and check the status code")
    def add_to_cart(self, book: dict) -> int:
        resp = requests.post(self.url + 'v1/cart/product', headers=API_KEY, json=book)
        return resp.status_code

    @allure.step("Get added book id from the cart")
    def get_cart(self) -> int:
        resp = requests.get(self.url + 'v1/cart', headers=API_KEY)
        return resp.json()['products'][0]['id']

    @allure.step("Delete book by {book_id} from the cart and check the satus code")
    def delete_from_cart(self, book_id: int) -> int:
        resp = requests.delete(self.url + 'v1/cart/product/' + str(book_id), headers=API_KEY)
        return resp.status_code