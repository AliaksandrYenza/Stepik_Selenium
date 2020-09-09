from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_css_selector('.trollface.btn.btn-primary')
    btn.click()

    win_tabs = browser.window_handles[1]    #open and save new tab
    browser.switch_to.window(win_tabs)      #change handles to new tabs

    time.sleep(1)

    x_value = browser.find_element_by_css_selector('.nowrap#input_value')
    x_value = x_value.text
    x_value = calc(x_value)

    input1 = browser.find_element_by_css_selector('.form-control#answer')
    input1.send_keys(str(x_value))

    btn = browser.find_element_by_tag_name('button')
    btn.click()

finally:

    time.sleep(11)
    browser.quit()