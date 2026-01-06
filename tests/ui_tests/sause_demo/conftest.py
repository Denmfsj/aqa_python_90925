import pytest

from playwright.sync_api import sync_playwright, expect

from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page import LoginPage
from core.ui.sausedemo.pages.product_page.product_page import ProductPage


@pytest.fixture(scope='session')  # 1 сторінка для всіх тестів
def pw_page():

    # pre-condition - перед yield  в yield page поверне сторінку
    # після yield post-condition
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # чи НЕ бачити вікно браузера

        page = browser.new_page()
        yield page
    print('test are done and browser was closed')



@pytest.fixture(scope='session')
def home_page(pw_page):
    """Логіниться в систему, логіниться в систему перший раз. Повертає HomePage"""
    home_page = HomePage(pw_page)
    home_page.open_page()

    if not home_page.is_page_opened():
        LoginPage(page=pw_page).do_login()

    return home_page  # все це pre-condition, після return не можу бути post-conditions
    pritn('Never printed')

# @pytest.fixture(scope='session')
# def loggined_page(pw_page):
#     lp = LoginPage(page=pw_page)
#
#     if lp.is_page_opened():
#         lp.do_login()
#     return pw_page
#
# @pytest.fixture(scope='session')
# def checkout_page(loggined_page):
#     """Логіниться в систему, логіниться в систему перший раз. Повертає HomePage"""
#     checkout_page = CheckoutPage(loggined_page)
#     checkout_page.open_page()
#
#     return checkout_page