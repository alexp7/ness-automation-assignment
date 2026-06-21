from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.data_reader import load_test_data


def test_ebay_cart_total_not_exceeds_budget(page):
    test_data = load_test_data("data/test_data.json")

    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    urls = home_page.search_items_by_name_under_price(
        test_data["query"],
        test_data["max_price"],
        test_data["limit"]
    )

    assert len(urls) > 0, "No product URLs found. eBay may have opened captcha/challenge page."

    for url in urls:
        product_page.add_item_to_cart(url)

    cart_page.open_cart()
    cart_page.assert_cart_total_not_exceeds(
        test_data["max_price"],
        len(urls)
    )