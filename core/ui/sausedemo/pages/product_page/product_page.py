from core.ui.sausedemo.forms.bucket_form import BucketForm
from core.ui.sausedemo.pages.base_page import BasePage
from utils.settings import d_settings
from playwright.sync_api import expect

class ProductPage(BasePage):


    def __init__(self, page, page_id=None):
        super().__init__(page)
        self.url = f'{self.base_url}inventory-item.html?id='
        self.page_id = page_id
        self.bucket = BucketForm(page)


    def open_page(self):
        if self.page_id is not None:
            self.page.goto(self.url + self.page_id, timeout=1000)
        else:
            raise ValueError('Cant open Product page without page_id')


    def is_page_opened(self):
        try:
            expect(self.page.locator('#back-to-products')).to_be_visible(timeout=1000)
            return True
        except Exception:
            return False


    def add_to_card(self):
        self.page.locator('#add-to-cart').click()
