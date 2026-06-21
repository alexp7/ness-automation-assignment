from playwright.sync_api import Page
from utils.price_parser import parse_price


class CartPage:
    CART_ICON = "//span[contains(@class,'gh-cart__icon')]"
    CART_SUBTOTAL = "//div[@data-test-id='SUBTOTAL']//span[contains(text(),'$')]"

    def __init__(self, page: Page):
        self.page = page

    def open_cart(self):
        self.page.locator(self.CART_ICON).click()

    def get_cart_total(self) -> float:
        subtotal_text = self.page.locator(self.CART_SUBTOTAL).inner_text()
        return parse_price(subtotal_text)

    def assert_cart_total_not_exceeds(self, budget_per_item: int, items_count: int):
        cart_total = self.get_cart_total()
        max_allowed_total = budget_per_item * items_count

        assert cart_total <= max_allowed_total