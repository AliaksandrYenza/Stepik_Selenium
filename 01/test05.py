from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    hidden_value = browser.find_element(By.CSS_SELECTOR, value=".form-group #treasure")
    x = hidden_value.get_attribute('valuex')

    input1 = browser.find_element(By.CSS_SELECTOR, value=".form-group #answer")
    x = calc(x)
    input1.send_keys(x)

    chckbx = browser.find_element(By.CSS_SELECTOR, value=".check-input#robotCheckbox")
    chckbx.click()

    radio_people = browser.find_element(By.CSS_SELECTOR, value=".check-input#peopleRule")
    radio_robots = browser.find_element(By.CSS_SELECTOR, value=".check-input#robotsRule")

    chck_radio = radio_robots.get_attribute("checked")

    print("!!!!!!!!!!!!!!!!!!!!value of people radio: ", chck_radio)

    if radio_robots != True:
        radio_robots.click()

    button = browser.find_element(By.CSS_SELECTOR, value=".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
