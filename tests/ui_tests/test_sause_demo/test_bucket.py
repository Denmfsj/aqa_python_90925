import pytest

from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page import LoginPage


@pytest.fixture  # scope=function, запускаеться перед КОЖННИМ тестом в якій вона викликаетсья
def brand_new_page(pw_page) -> HomePage:
    """
    Створює новий контекст і сторінку на один тест.
    Тест повинен явно викликати new_page.
    """
    browser = pw_page.context.browser  # використовуємо той самий browse
    context = browser.new_context()
    page = context.new_page()

    yield LoginPage(page).open_page().do_login()

    context.close()


def test_bucket_is_empty(brand_new_page):

    assert brand_new_page.bucket.get_number_of_items_in_bucket() == 0, 'Initial bucket must be empty'


def test_bucket_has_2_products(brand_new_page):

    product_page = brand_new_page.click_on_a_random_product()
    product_page.add_to_card()

    brand_new_page.open_page()
    brand_new_page.add_1_product()
    actual_result = brand_new_page.bucket.get_number_of_items_in_bucket()
    brand_new_page.page.wait_for_timeout(1000)

    assert actual_result == 2, f'Must be 2 product in bucket but we have {actual_result}'


def test_bucket_has_1_products(brand_new_page):

    product_page = brand_new_page.click_on_a_random_product()
    product_page.add_to_card()

    actual_result = brand_new_page.bucket.get_number_of_items_in_bucket()
    brand_new_page.page.wait_for_timeout(1000)

    assert actual_result == 1, f'Must be 1 product in bucket but we have {actual_result}'


