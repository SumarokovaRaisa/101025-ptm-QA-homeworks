
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


def test_text_input_button_changes(driver):
    driver.get("http://uitestingplayground.com/textinput")
    text = "ITCH"
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys(text)
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    assert button.text == text


def test_check_image_presents(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 10)
    third_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                             "img:nth-of-type(3)")))
    alt_value = third_image.get_attribute("alt")
    assert alt_value == "award"
