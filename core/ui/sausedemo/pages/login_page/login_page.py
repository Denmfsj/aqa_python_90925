from playwright.sync_api import expect

from core.ui.sausedemo.pages.base_page import BasePage
from core.ui.sausedemo.pages.home_page.home_page import HomePage
from core.ui.sausedemo.pages.login_page.login_page_locators import LoginPageLocators
from utils.settings import d_settings

import logging
import allure


class LoginPage(BasePage):
    # css selectors
    user_name  = '#user-name'
    user_pwd ='#password'
    login_button = '#login-button'
    error_button = '.error-button'

    def __init__(self, page):
        super().__init__(page)
        self.url = self.base_url
        self.page_locators = LoginPageLocators()
        self.logger = logging.getLogger('LoginPage')


    @allure.step('opening LoginPage')
    def open_page(self):
        self.page.goto(self.url, timeout=1000)
        return self

    @allure.step('Do login with username = {user_name}')
    def do_login(self, user_name=d_settings.SAUSEDEMO_USERNAME,
                 user_pwd=d_settings.SAUSEDEMO_PASSWORD) -> HomePage:

        self.fill_user_name(name=user_name)
        self.fill_user_pwd(pwd=user_pwd)
        return self.click_login_button()


    @allure.step('click login button')
    def click_login_button(self) -> HomePage:
        self.page.locator(self.page_locators.login_button).click()
        return HomePage(self.page)

    @allure.step('fill user pwd')
    def fill_user_pwd(self, pwd=d_settings.SAUSEDEMO_PASSWORD):
        self.fill_field(
            locator=self.page.locator(self.page_locators.user_pwd),
            value=pwd
        )
        return self

    def find_and_close_login_error(self):
        expect(self.page.locator(self.error_button)).to_be_enabled(timeout=1000)
        self.page.locator(self.error_button).click()
        return self

    @allure.step('fill user name')
    def fill_user_name(self, name=d_settings.SAUSEDEMO_USERNAME):
        self.logger.info(f'Filling user name with name = {name}')
        self.page.locator(self.page_locators.user_name).fill(name)
        return self

        # перший варіант - ми зберігаемо локатор(строку) в цьому методі
        # self.page.locator('#user-name').fill(user_name)
        #
        # перший варіант - ми зберігаемо локатор(строку) в цьому класі
        # self.page.locator(user_name).fill(user_name)
        #
        # перший варіант - ми зберігаемо локатор(строку) в окремому класі
        # user_name_css_locator_string = self.page_locators.user_name
        # pw_locator = self.page.locator(user_name_css_locator_string)
        # pw_locator.fill(user_name)


