import pytest
from playwright.sync_api import sync_playwright, expect

from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page import LoginPage
from core.ui.sausedemo.pages.product_page.product_page import ProductPage
from utils.settings import d_settings


def test_smoke_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # чи НЕ бачити вікно браузера

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.open_page()
        login_page.do_login()

        page.wait_for_timeout(1000)

        # елемент тільки на головній сторінці
        home_page = HomePage(page)
        assert home_page.is_page_opened() is True, 'Home page wasn\'t opened'
        page.wait_for_timeout(1000)


@pytest.mark.parametrize('product_number', [2,3,4])
def test_smoke_product_page(home_page, pw_page, product_number):

    home_page.open_page()
    assert home_page.is_page_opened() is True, 'Home page wasn\'t opened'

    home_page.page.wait_for_timeout(1000)
    home_page.click_on_a_product(number=product_number)

    product_page = ProductPage(page=pw_page)
    assert product_page.is_page_opened() is True, 'Product page wasn\'t opened'


        # якщо дивитись ан іншу сторінку
        # find_product.click()
        # expect(page.locator('//span[@data-test="title"]')).to_have_text('Products', timeout=2000)

        # browser = p.chromium.launch(headless=False)
        #
        # page = browser.new_page()
        # page.goto(d_settings.SAUSEDEMO_URL)
        # page.wait_for_timeout(1000)
        #
        # page.locator('#user-name').fill(d_settings.SAUSEDEMO_USERNAME, timeout=1000)  # login
        # page.locator('#password').fill(d_settings.SAUSEDEMO_PASSWORD, timeout=1000)  # password
        #
        # page.get_by_role('button').click(timeout=500)  # login button
        # page.wait_for_timeout(1000)
        #
        # # елемент тільки на головній сторінці
        # expect(page.locator('//span[@data-test="title"]')).to_have_text('Products', timeout=2000)
        # page.wait_for_timeout(1000)

        # якщо дивитись ан іншу сторінку
        # find_product.click()
        # expect(page.locator('//span[@data-test="title"]')).to_have_text('Products', timeout=2000)