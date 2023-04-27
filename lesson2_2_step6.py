from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return math.log(abs(12*math.sin(x)))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x_value)))
    browser.find_element(By.ID, 'robotCheckbox').click()
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, "button").click()


finally:
    time.sleep(3)
    browser.quit()
