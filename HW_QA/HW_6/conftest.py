import pytest
from selenium import webdriver
from HW_6.pages.login_page import LoginPage
from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.cart_page import CartPage
from HW_6.pages.checkout_page import CheckoutPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield
    driver.quit()

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.cart_page = CartPage(driver)
    request.cls.checkout_page = CheckoutPage(driver)

    yield
    driver.quit()

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()