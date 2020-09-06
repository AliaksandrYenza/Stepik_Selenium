from selenium import webdriver
import time
from selenium.webdriver.common.by import  By


#link = "http://suninjuly.github.io/simple_form_find_task.html"
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #.container .form-group [text()='First name:*']
    input1 = browser.find_element(By.CSS_SELECTOR, value=".container .form-group .form-control[name='first_name']")
    #input1 = browser.find_element_by_tag_name(".container .form-group")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(name="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(id_="country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH,value='//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()