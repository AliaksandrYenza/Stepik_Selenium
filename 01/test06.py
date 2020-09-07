from selenium import webdriver
from selenium.webdriver.common.by import  By
import time






link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    output1 = browser.find_element(By.CSS_SELECTOR, value=".nowrap#num1")
    output2 = browser.find_element(By.CSS_SELECTOR, value=".nowrap#num2")
    res = int(output1.text) + int(output2.text)

    selected = browser.find_element_by_tag_name('select')
    selected.click()
    res = '"'+ str(res) + '"'
    browser.find_element(By.CSS_SELECTOR, value=f"[value={str(res)}]").click()

    btn = browser.find_element(By.CSS_SELECTOR, value='.btn.btn-default')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()