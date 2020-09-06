from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = str(math.ceil(math.pow(math.pi, math.e)*10000))
    cl = browser.find_element(By.PARTIAL_LINK_TEXT,value=a)
    cl.click()
    input1 = browser.find_element(By.CSS_SELECTOR, value='.form-control')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, value='.container .form-group [name="last_name"]')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CSS_SELECTOR, value=".form-control.city")
    input3.send_keys('Smolensk')

    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    




finally:
    time.sleep(30)
    browser.quit()