import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser_start = webdriver.Chrome()
    browser_start.get(url)
    button = browser_start.find_element(By.ID,'submit_butto')
    button.click()
    time.sleep(5)

finally:
    browser_start.quit()