import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By
import unittest
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#unittest
#for pytest -> in terminal: pytest class_name.py
class TestAbs(unittest.TestCase):


    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver = webdriver.Chrome()
        driver.get(link)

        firstName_input = driver.find_element(By.CSS_SELECTOR,
                                      value=".first_block .form-control.first")
        firstName_input.send_keys('First Name')

        lastName_input = driver.find_element(By.CSS_SELECTOR,
                                      value='.first_block .form-control.second')
        lastName_input.send_keys("Last Name")

        email_input = driver.find_element(By.CSS_SELECTOR,
                                      value=".form-group.third_class .form-control.third")
        email_input.send_keys("email123@mail.com")

        phone_input = driver.find_element(By.CSS_SELECTOR,
                                          value=".form-control.first[placeholder='Input your phone:']")
        phone_input.send_keys('123-12-3122')

        address_input = driver.find_element(By.CSS_SELECTOR,
                                            value=".form-control.second[placeholder='Input your address:']")
        address_input.send_keys('Test str. 9819')


        btn = driver.find_element(By.CSS_SELECTOR,
                                  value=".btn.btn-default")
        btn.click()

        #!!!!!!!!!!!Explicit
        txt = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//h1[contains(text() ,'Congratulations!')]" ))
        ).text

        self.assertEqual(txt, 'Congratulations! You have successfully registered!')
        driver.quit()


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        #!!!!!!!!!!!!!!!! implicitly
        driver.implicitly_wait(10)

        driver.get(link)

        firstName_input = driver.find_element(By.CSS_SELECTOR,
                                              value=".first_block .form-control.first")
        firstName_input.send_keys('First Name')

        lastName_input = driver.find_element(By.CSS_SELECTOR,
                                             value='.first_block .form-control.second')
        lastName_input.send_keys("Last Name")

        email_input = driver.find_element(By.CSS_SELECTOR,
                                          value=".form-group.third_class .form-control.third")
        email_input.send_keys("email123@mail.com")

        phone_input = driver.find_element(By.CSS_SELECTOR,
                                          value=".form-control.first[placeholder='Input your phone:']")
        phone_input.send_keys('123-12-3122')

        address_input = driver.find_element(By.CSS_SELECTOR,
                                            value=".form-control.second[placeholder='Input your address:']")
        address_input.send_keys('Test str. 9819')

        btn = driver.find_element(By.CSS_SELECTOR,
                                  value=".btn.btn-default")
        btn.click()

        # !!!!!!!!!!!Explicit
        txt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text() ,'Congratulations!')]"))
        ).text

        self.assertEqual(txt, 'Congratulations! You have successfully registered!')
        driver.quit()

if __name__ == '__main__':
    unittest.main()

    #link = "http://suninjuly.github.io/registration2.html"
