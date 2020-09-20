import time, math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestPazamTask():


    @pytest.mark.parametrize('link', [ "236895","236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_ch(self, browser, link):

        browser.get(f'https://stepik.org/lesson/{link}/step/1')
        browser.implicitly_wait(10)

        input_field = browser.find_element(By.CSS_SELECTOR,
                                           value='.textarea.string-quiz__textarea.ember-text-area.ember-view')
        answer = math.log(int(time.time()))
        input_field.send_keys(str(answer))
        btn = browser.find_element(By.CSS_SELECTOR,
                                   value='.submit-submission')
        btn.click()
        exp_res_field = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text


        assert exp_res_field == 'Correct!', print(exp_res_field)

