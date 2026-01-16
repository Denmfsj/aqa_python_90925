from core.ui.sausedemo.forms.basket_form import BasketForm
from core.ui.sausedemo.pages.base_page import BasePage
from core.ui.sausedemo.pages.product_page.product_page import ProductPage
from utils.settings import d_settings
from playwright.sync_api import expect, Page
import random
import allure

class HomePage(BasePage):


    page_title_locator = '//span[@data-test="title"]'
    first_product_link_locator = '#item_4_title_link'
    products_links_locator = '.inventory_item_label a'
    add_product_buttons = '#add-to-cart-sauce-labs-backpack'

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f'{self.base_url}inventory.html'
        self.basket = BasketForm(page)

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

    @allure.step('adding 1 product')
    def add_1_product(self):
        self.page.locator(self.add_product_buttons).click()

    def click_on_first_product(self):
        products = self.page.locator(self.first_product_link_locator)  # список зпосилань на  6 продуктів
        products.first.click()
        return ProductPage(self.page)


    def click_on_a_product(self, number):
        with allure.step('searching products on the page'):
            products = self.page.locator(self.products_links_locator)  # 1 локатора з усіма продектами

        with allure.step(f'clicking at {number - 1} products'):
            products.nth(number - 1).click()  # індекс = порядковий номер мінус один
        # дргуий продукт на UI має індекс 1
        # третій продукт на UI має індекс 2
        return ProductPage(self.page)

    def click_on_a_random_product(self) -> ProductPage:
        all_products = self.page.locator(self.products_links_locator).all() # список локаторів на всі продукти

        assert all_products is not None and len(all_products) > 0, 'Cant find products on Home page'
        selected_product = random.choice(all_products)
        self.logger.info(f'Home page. Select product is {selected_product.text_content()}')
        self.logger.info(f'Custom log just to present')

        with allure.step(f'clicking at {selected_product.text_content()} products'):
            selected_product.click()  # click на рандомний продукт

        return ProductPage(self.page)
