from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id][contains(text(), '')]"), "$100")
        )
    browser.find_element(By.ID, 'book').click()

    x_value = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(x_value))
    browser.find_element(By.ID, 'solve').click()


finally:
    time.sleep(5)
    browser.quit()
