import pytest
import allure
from allure_commons.types import LinkType
from playwright.sync_api import sync_playwright, expect

from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page import LoginPage
from core.ui.sausedemo.pages.product_page.product_page import ProductPage
from tests.ui_tests.test_sause_demo.conftest import UiSauceDemoBase
from utils.settings import d_settings

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

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Smoke')
@pytest.mark.smoke
class TestSmoke(UiSauceDemoBase):


    @allure.link('hira.com/bug-123', link_type=LinkType.ISSUE)
    @allure.link('hira.com/feature-345', link_type=LinkType.TEST_CASE)
    @allure.title('Smoke: login to home page')
    @allure.description('Just base check for login on main page')
    def test_smoke_home_page(self, brand_new_page):

        login_page = LoginPage(brand_new_page)

        login_page.open_page()
        login_page.do_login()

        brand_new_page.wait_for_timeout(1000)

        # елемент тільки на головній сторінці
        home_page = HomePage(brand_new_page)
        assert home_page.is_page_opened() is True, 'Home page wasn\'t opened'
        brand_new_page.wait_for_timeout(1000)
