import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
#pytest --language=es test_items.py

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(5)
    assert button != 0, "Wrong!"
