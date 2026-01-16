from pathlib import Path

import pytest
import allure

from playwright.sync_api import sync_playwright, expect, Page

from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page import LoginPage
from core.ui.sausedemo.pages.product_page.product_page import ProductPage
from definitions import BASE_PATH


@pytest.mark.ui
@allure.epic('UI SauceDemo tests')
class UiSauceDemoBase:
    pass

@pytest.fixture(scope='session')  # 1 сторінка для всіх тестів
def pw_page() -> Page:

    # pre-condition - перед yield  в yield page поверне сторінку
    # після yield post-condition
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # чи НЕ бачити вікно браузера

        page = browser.new_page()
        yield page
    print('test are done and browser was closed')


@pytest.fixture(scope="function", autouse=True)
def trace_per_test(request, pw_page):

    context = pw_page.context

    trace_path = BASE_PATH / 'pw_traces'
    trace_path.mkdir(exist_ok=True)

    # старт трасування
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield  # тест виконується тут

    # stop tracing і збереження після тесту
    test_name = request.node.name
    context.tracing.stop(path=str(trace_path / f"{test_name}.zip"))

    pw_page.screenshot(path=str(trace_path / f"{test_name}.png"), type='png')

    allure.attach.file(str(trace_path / f"{test_name}.zip"),
                       name='pw_trace', attachment_type=allure.attachment_type.ZIP)

    allure.attach.file(str(trace_path / f"{test_name}.png"),
                       name='screenshot', attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope='session')
def home_page(pw_page) -> HomePage:
    """Логіниться в систему, логіниться в систему перший раз. Повертає HomePage"""
    home_page = HomePage(pw_page)
    home_page.open_page()

    if not home_page.is_page_opened():
        return LoginPage(page=pw_page).do_login()

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