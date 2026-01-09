from playwright.sync_api import Page

from utils.settings import d_settings
import logging


class BasePage:

    def __init__(self, page: Page):
        self.base_url = d_settings.SAUSEDEMO_URL
        self.page = page
        self.logger = logging.getLogger()


    def open_page(self):
        self.page.goto(self.url, timeout=1000)


    def is_page_opened(self):
        raise NotImplemented

    def fill_field(self, locator, value):
        print(f'Filling {locator} with pwd = {value}...')
        locator.fill(value)