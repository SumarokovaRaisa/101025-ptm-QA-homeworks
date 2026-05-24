from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # локаторы
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        ).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_total_price(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        ).text
