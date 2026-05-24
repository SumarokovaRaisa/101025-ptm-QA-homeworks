"""
Задание 1: Проверка наличия текста в iframe
Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице.
Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
Открыть страницу Drag & Drop Demo.
Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
Выполнить следующие шаги:
Захватить первую фотографию (верхний левый элемент).
Перетащить её в область корзины (Trash).
Проверить, что после перемещения:
В корзине появилась одна фотография.
В основной области осталось 3 фотографии.
Ожидаемый результат:
Фотография успешно перемещается в корзину.
Вне корзины остаются 3 фотографии.
"""


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
    # Задание 1: Проверка наличия текста в iframe
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    # Находим фрейм и переключаемся в него
    iframe = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe)

    expected_text = "semper posuere integer et senectus justo curabitur."
    text_element = browser.find_element(
        By.XPATH, f'//*[contains(text(), {"expected_text"})]'
    )
    assert text_element.is_displayed()


def test_drag_and_drop_photo(browser):
    # Задание 2: Тестирование Drag & Drop
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(browser, 10)

    # Ожидаем фрейм и переключаемся в него
    iframe = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "demo-frame")))
    browser.switch_to.frame(iframe)

    # Ожидаем появления картинок в галерее
    photos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    first_photo = photos[0]

    trash_area = browser.find_element(By.ID, "trash")

    # Используем пошаговый drag and drop (click_and_hold -> move_to_element -> release),
    actions = ActionChains(browser)
    actions.click_and_hold(first_photo).move_to_element(trash_area).release().perform()

    # Ожидаем, пока картинка физически появится внутри корзины (в DOM-дереве #trash)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    # Считаем количество фото в корзине и в галерее
    trash_photos = browser.find_elements(By.CSS_SELECTOR, "#trash li")
    remaining_photos = browser.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(trash_photos) == 1
    assert len(remaining_photos) == 3