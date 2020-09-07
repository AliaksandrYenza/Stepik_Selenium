from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time



link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname = browser.find_element(By.CSS_SELECTOR, value=".form-control[name = 'firstname']")
    input_firstname.send_keys("First")
    input_lastname = browser.find_element(By.CSS_SELECTOR, value=".form-control[name = 'lastname']")
    input_lastname.send_keys("Last")
    input_email = browser.find_element(By.CSS_SELECTOR, value=".form-control[name = 'email']")
    input_email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # <-- получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file_for_test08.txt')           
    # <-- добавляем к этому пути имя файла 
    element= browser.find_element(By.CSS_SELECTOR,value="#file[name='file']")
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, value=".btn.btn-primary")
    time.sleep(0.5)
    submit.click()

finally:
    time.sleep(10)
    browser.quit()