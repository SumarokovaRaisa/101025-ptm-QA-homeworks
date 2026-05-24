from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

@pytest.fixture
def driver():
    options = Options()
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)

    yield driver

    driver.quit()

def test_payment_section(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(3)

    payment_section = driver.find_element(By.LINK_TEXT, value="Способы оплаты")
    sleep(3)
    payment_section.click()
    sleep(3)
    driver.save_screenshot("./itc.png")


