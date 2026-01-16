import allure
import pytest

from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page import LoginPage
from tests.ui_tests.test_sause_demo.conftest import UiSauceDemoBase


@pytest.fixture  # scope=function, запускаеться перед КОЖННИМ тестом в якій вона викликаетсья
def brand_new_page(pw_page) -> HomePage:
    """
    Створює новий контекст і сторінку на один тест.
    Тест повинен явно викликати new_page.
    """
    browser = pw_page.context.browser  # використовуємо той самий browse
    context = browser.new_context()
    page = context.new_page()

    home_page = LoginPage(page).open_page().do_login()

    yield home_page

    context.close()

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('Basket Page')
class TestBasketPage(UiSauceDemoBase):

    @allure.story('empty basket')
    @allure.title('test empty basket')
    def test_basket_is_empty(self, brand_new_page):
        """The test is checking that basket is empty when user is logged in first time"""

        assert brand_new_page.basket.get_number_of_items_in_basket() == 0, 'Initial basket must be empty'

    @allure.story('basket with products')
    def test_basket_has_2_products(self, brand_new_page):

        with allure.step('Add first product to the basket'):
            product_page = brand_new_page.click_on_a_random_product()
            product_page.add_to_card()

        brand_new_page.open_page()

        with allure.step('Add second product to the basket'):
            brand_new_page.add_1_product()

        actual_result = brand_new_page.basket.get_number_of_items_in_basket()
        brand_new_page.page.wait_for_timeout(1000)

        assert actual_result == 2, f'Must be 2 product in basket but we have {actual_result}'

    @allure.story('basket with products')
    def test_basket_has_1_products(self, brand_new_page):

        product_page = brand_new_page.click_on_a_random_product()
        product_page.add_to_card()

        actual_result = brand_new_page.basket.get_number_of_items_in_basket()
        brand_new_page.page.wait_for_timeout(1000)

        assert actual_result == 1, f'Must be 1 product in basket but we have {actual_result}'


