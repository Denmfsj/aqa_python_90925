from playwright.sync_api import Page
import logging


class BucketForm:

    choping_card_list = '.shopping_cart_link'

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger('BucketForm')


    def open_bucket_page(self):
        self.page.locator(self.choping_card_list).click()

    def get_number_of_items_in_bucket(self):
        try:
            return int(self.page.locator(self.choping_card_list).text_content())
        except Exception as e:
            self.logger.warning(f'Potential problem with converting to int: {e}')
            return 0