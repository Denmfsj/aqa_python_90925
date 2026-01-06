from core.ui.sausedemo.pages.base_page import BasePage
from core.ui.sausedemo.pages.login_page.login_page_locators import LoginPageLocators
from utils.settings import d_settings

import logging


class LoginPage(BasePage):
    # css selectors
    user_name  = '#user-name'
    user_pwd ='#password'
    login_button = '#login-button'

    def __init__(self, page):
        super().__init__(page)
        self.url = self.base_url
        self.page_locators = LoginPageLocators()
        self.logger = logging.getLogger('LoginPage')


    def open_page(self):
        self.page.goto(self.url, timeout=1000)

    def do_login(self, user_name=d_settings.SAUSEDEMO_USERNAME,
                 user_pwd=d_settings.SAUSEDEMO_PASSWORD):

        self.fill_user_name(name=user_name)
        self.fill_user_pwd(pwd=user_pwd)
        self.click_login_button()


    def click_login_button(self):
        self.page.locator(self.page_locators.login_button).click()

    def fill_user_pwd(self, pwd=d_settings.SAUSEDEMO_PASSWORD):
        self.fill_field(
            locator=self.page.locator(self.page_locators.user_pwd),
            value=pwd
        )

    def fill_user_name(self, name=d_settings.SAUSEDEMO_USERNAME):
        self.logger.info(f'Filling user name with name = {name}')
        self.page.locator(self.page_locators.user_name).fill(name)

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


