from playwright.sync_api import Page


class ProductPage:
    ADD_TO_CART_BUTTON = "//a[@id='atcBtn_btn_1' and .//span[normalize-space()='Add to cart']]"
    PROCEED_BUTTON = "//button[normalize-space()='Proceed']"

    def __init__(self, page: Page):
        self.page = page

    def add_item_to_cart(self, url: str, item_index: int) -> bool:
        try:
            self.page.goto(url)
        except Exception:
            return False

        add_to_cart_button = self.page.locator(self.ADD_TO_CART_BUTTON)

        if add_to_cart_button.count() == 0:
            return False

        add_to_cart_button.click()

        proceed_button = self.page.locator(self.PROCEED_BUTTON)

        if proceed_button.count() > 0:
            proceed_button.click()

        self.page.screenshot(path=f"screenshots/added_item_{item_index}.png")

        return True