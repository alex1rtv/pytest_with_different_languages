# https://stepik.org/lesson/237240/step/9?next=&unit=209628
# 3.6.9

import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket_at_page(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button_basket is not None, "Button 'Add To Basket' is not found at the page"
    
