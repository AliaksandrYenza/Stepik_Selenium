from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element(By.CSS_SELECTOR, value=".form-group #input_value")
    x = value_x.text
    answer = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR, value=".form-group #answer")
    input_field.send_keys(answer)
    chckbx = browser.find_element(By.CSS_SELECTOR, value=".form-check.form-check-custom .form-check-input")
    chckbx.click()
    rdbttn = browser.find_element(By.CSS_SELECTOR,value="[for='robotsRule']")
    rdbttn.click()
    buttno = browser.find_element(By.CSS_SELECTOR, value=".btn.btn-default")
    buttno.click()

finally:
    time.sleep(10)
    browser.quit()
