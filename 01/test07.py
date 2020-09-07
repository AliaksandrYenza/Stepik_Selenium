from selenium import webdriver
import time
import math


link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_value = browser.find_element_by_css_selector(".nowrap#input_value")
    x_value = int(x_value.text)
    x_value = calc(x_value)
    
    input1 = browser.find_element_by_css_selector(".form-control#answer")
    input1.send_keys(x_value)
    
    chckbx = browser.find_element_by_css_selector(".form-check-input#robotCheckbox")
    chckbx.click()

    rdbtn = browser.find_element_by_css_selector("[for = 'robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rdbtn) 

    chrd = rdbtn.get_attribute("checked")

    if chrd != True:
        rdbtn.click()

    btn = browser.find_element_by_tag_name('button')

    browser.execute_script("return arguments[0].scrollIntoView(true);", btn) 
    # <-- scroll untill obj visiable
    
    btn.click()


finally:
    time.sleep(10)
    browser.quit()

"""browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #scroll untill obj visiable
button.click()
assert True"""