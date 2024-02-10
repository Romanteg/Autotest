import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/simple_form_find_task.html"

browser_start = webdriver.Chrome()
browser_start.get(url)
button = browser_start.find_element(By.ID,'submit_button')
button.click()
time.sleep(5)

browser_start.quit()