from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return math.log(abs(12*math.sin(x)))


try:
    
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(1) #фиксируем работу с неявным ожиданием
    browser.get(link)
    #Балуемся со скриптом для остановки кнопки
    #browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    time.sleep(3)

    browser.find_element(By.TAG_NAME, 'button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_value = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.TAG_NAME, 'input').send_keys(calc(int(x_value)))
    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(5)
    browser.quit()
