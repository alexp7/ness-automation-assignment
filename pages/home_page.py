from playwright.sync_api import Page


class HomePage:
    DIGITAL_CAMERAS_URL = "https://www.ebay.com/b/Digital-Cameras/31388/bn_779"

    PRODUCT_LINKS = "//a[contains(@href,'/itm/') and contains(@class,'brwrvr__item-card__image-link')]"

    def __init__(self, page: Page):
        self.page = page

    def search_items_by_name_under_price(self, query: str, max_price: int, limit: int):
        self.page.goto(f"{self.DIGITAL_CAMERAS_URL}?LH_BIN=1&_udhi={max_price}")

        links = self.page.locator(self.PRODUCT_LINKS).evaluate_all(
            "(elements) => elements.map(element => element.href)"
        )

        return links[:limit]