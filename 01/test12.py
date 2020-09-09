from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    #Дождаться, когда цена дома уменьшится до $100 
    # (ожидание нужно установить не меньше 12 секунд)
    # Нажать на кнопку "Book"
    #Решить уже известную нам математическую задачу 
    #(используйте ранее написанный код) и отправить решение
    
    btn = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.ID, 'book')))


    
    price_value = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    btn.click()

    x_value = browser.find_element(By.CSS_SELECTOR, value = '.nowrap#input_value')
    
    x_value = calc(x_value.text)

    input1 = browser.find_element(By.CSS_SELECTOR, value = '.form-control#answer')
    input1.send_keys(str(x_value))

    btn = browser.find_element(By.CSS_SELECTOR, value = '#solve.btn.btn-primary')
    btn.click()


finally:
    time.sleep(10)
    browser.close()
