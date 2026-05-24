from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)

   def get_items(self):
       return self.wait.until(EC.presence_of_all_elements_located(
           (By.CLASS_NAME, "inventory_item_name")))

   def get_items_amount(self):
       """Returns the total number of items on the inventory page"""
       return len(self.get_items())

   def get_item_price(self, item_name):
       price_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"
       return self.wait.until(EC.presence_of_element_located((By.XPATH, price_xpath))).text


   def add_item_to_cart(self, item_name):
       button_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
       self.wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()

   def go_to_cart(self):

       self.wait.until(EC.element_to_be_clickable(
           (By.CLASS_NAME, "shopping_cart_link"))).click()