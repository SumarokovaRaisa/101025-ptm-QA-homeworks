from HW_6.pages.login_page import LoginPage
from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.cart_page import CartPage
from HW_6.pages.checkout_page import CheckoutPage


def test_checkout_total(driver):

    # login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.success_login(
        "standard_user",
        "secret_sauce"
    )

    # inventory
    inventory_page = InventoryPage(driver)

    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    # cart
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # checkout
    checkout_page = CheckoutPage(driver)

    checkout_page.fill_checkout_form(
        "Raisa",
        "Sumarokova",
        "12345"
    )

    total_price = checkout_page.get_total_price()

    assert total_price == "Total: $58.29"