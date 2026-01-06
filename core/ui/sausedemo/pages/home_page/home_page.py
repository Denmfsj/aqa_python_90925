from core.ui.sausedemo.pages.base_page import BasePage
from utils.settings import d_settings
from playwright.sync_api import expect

class HomePage(BasePage):


    page_title_locator = '//span[@data-test="title"]'
    first_product_link_locator = '#item_4_title_link'
    products_links_locator = '.inventory_item_label a'


    def __init__(self, page):
        super().__init__(page)
        self.url = f'{self.base_url}inventory.html'

    def is_page_opened(self):
        check_1 = self.page.url == self.url
        try:
            expect(self.page.locator(self.page_title_locator)
                   ).to_have_text('Products', timeout=2000)

            if check_1 is True:
                return True
            else:
                return False

        except Exception:
            return False

    def click_on_first_product(self):
        products = self.page.locator(self.first_product_link_locator)  # список зпосилань на  6 продуктів
        products.first.click()

    def click_on_a_product(self, number):
        products = self.page.locator(self.products_links_locator)  # список зпосилань на  6 продуктів
        products.nth(number - 1).click()  # індекс = порядковий номер мінус один
        # дргуий продукт на UI має індекс 1
        # третій продукт на UI має індекс 2