from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    first_name_el = browser.find_element_by_css_selector(
        "div.first_block input.first")
    first_name_el.send_keys("1")

    last_name_el = browser.find_element_by_css_selector(
        "div.first_block input.second")
    last_name_el.send_keys("2")

    email_el = browser.find_element_by_css_selector(
        "div.first_block input.third")
    email_el.send_keys("3")

    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    congrats = browser.find_element_by_tag_name("h1")
    congrats_text = congrats.text

    assert "Congratulations! You have successfully registered!" == congrats_text

finally:
    time.sleep(3)
    browser.quit()