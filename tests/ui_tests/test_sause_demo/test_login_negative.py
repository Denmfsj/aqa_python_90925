import pytest
import allure

from core.ui.sausedemo.pages.login_page.login_page import LoginPage
from tests.ui_tests.test_sause_demo.conftest import UiSauceDemoBase


@pytest.fixture
def brand_new_page(pw_page):
    """
    Створює новий контекст і сторінку на один тест.
    Тест повинен явно викликати new_page.
    """
    browser = pw_page.context.browser  # використовуємо той самий browse
    context = browser.new_context()
    page = context.new_page()

    yield page  # повертаємо контекст, щоб трасування могло працювати

    context.close()

@allure.severity(allure.severity_level.MINOR)
@allure.feature('Negative')
@pytest.mark.negative
@pytest.mark.product_page
class TestLoginPageNegative(UiSauceDemoBase):

    def test_smoke_login_page_incorrect_user_data(self, brand_new_page):

        login_page = LoginPage(brand_new_page)

        login_page.open_page()

        # incorrect user name
        login_page.fill_user_name('INCORRECT_AQA_USER_NAME').fill_user_pwd().click_login_button()
        login_page.find_and_close_login_error()

        # incorrect user pwd
        login_page.fill_user_name().fill_user_pwd('INCORRECT_AQA_USER_PASSWORD').click_login_button()
        login_page.find_and_close_login_error()

        # incorrect user name and user pwd
        login_page.fill_user_name('INCORRECT_AQA_USER_NAME').fill_user_pwd('INCORRECT_AQA_USER_PASSWORD').click_login_button()
        login_page.find_and_close_login_error()
