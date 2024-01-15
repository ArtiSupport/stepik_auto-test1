import time
import pytest

def test_add_to_cart_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # Добавим sleep для визуальной проверки корректности отображения
    time.sleep(10)
    add_to_cart_button = browser.find_element("css selector", ".btn-add-to-basket")
    assert add_to_cart_button, "Add to cart button is not present on the page"
