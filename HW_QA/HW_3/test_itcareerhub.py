import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


def test_itcareerhub_contacts_callback(driver):
    driver.get("https://itcareerhub.de/ru")
    time.sleep(5)

    # Проверка логотипа
    logo = driver.find_element(By.CSS_SELECTOR, "#rec1921710463")
    assert logo.is_displayed()

    # Проверка ссылок меню
    assert driver.find_element(By.LINK_TEXT, "Программы").is_displayed()
    assert driver.find_element(By.LINK_TEXT, "Способы оплаты").is_displayed()
    assert driver.find_element(By.LINK_TEXT, "О нас").is_displayed()
    contacts = driver.find_element(By.XPATH, "//a[contains(text(),'Контакт')]")
    driver.execute_script("arguments[0].click();", contacts)
    assert driver.find_element(By.LINK_TEXT, "Отзывы").is_displayed()
    assert driver.find_element(By.LINK_TEXT, "Блог").is_displayed()

    # Проверка кнопок языка
    assert driver.find_element(By.LINK_TEXT, "ru").is_displayed()
    assert driver.find_element(By.LINK_TEXT, "de").is_displayed()

    # Клик Контакты
    contacts = driver.find_element(By.XPATH, "//a[contains(text(),'Контакт')]")
    driver.execute_script("arguments[0].click();", contacts)
    time.sleep(5)

    # Клик по кнопке "Обратный звонок"
    button = driver.find_element(By.CSS_SELECTOR, ".tn-elem__11949867411754046238620 a")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)

    # Проверка текста во всплывающем окне
    text_appeared = driver.find_element(By.XPATH,
                     "//*[contains(.,'Запишитесь на бесплатную карьерную консультацию')]")

    assert text_appeared.is_displayed()

