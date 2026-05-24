import pytest
from selenium import webdriver
from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.login_page import LoginPage
from HW_6.pages.cart_page import CartPage


# @pytest.mark.usefixtures("setup")
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        # Инициализация Page Objects
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.cart_page = CartPage(self.driver)

        yield
        driver.quit()
