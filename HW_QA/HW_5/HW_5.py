
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_text_in_iframe(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    iframe = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe)
    expected_text = "semper posuere integer et senectus justo curabitur."
    text_element = browser.find_element(
        By.XPATH, f'//*[contains(text(), {"expected_text"})]'
    )

    assert text_element.is_displayed()


def test_drag_and_drop_photo(browser):
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(browser, 10)
    iframe = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "demo-frame")))
    browser.switch_to.frame(iframe)

    photos = browser.find_elements(By.CSS_SELECTOR, "#gallery li")
    first_photo = photos[0]

    trash_area = browser.find_element(By.ID, "trash")
    actions = ActionChains(browser)
    actions.drag_and_drop(first_photo, trash_area).perform()

    trash_photos = browser.find_elements(By.CSS_SELECTOR, "#trash li")
    remaining_photos = browser.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(trash_photos) == 1
    assert len(remaining_photos) == 3


