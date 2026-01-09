import pytest


from core.ui.sausedemo.pages.product_page.product_page import ProductPage


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.product_page
@pytest.mark.parametrize('product_number', [2,3,4])
def test_product_page(home_page, product_number):

    home_page.open_page()
    assert home_page.is_page_opened() is True, 'Home page wasn\'t opened'

    home_page.page.wait_for_timeout(1000)
    product_page = home_page.click_on_a_product(number=product_number)

    assert product_page.is_page_opened() is True, 'Product page wasn\'t opened'

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.product_page
def test_product_page_click_at_random_product(home_page):

    home_page.open_page()
    assert home_page.is_page_opened() is True, 'Home page wasn\'t opened'

    home_page.page.wait_for_timeout(1000)
    product_page = home_page.click_on_a_random_product()

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