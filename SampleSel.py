from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Milena/PycharmProjects/SampleSelPython/proba/driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.implicitly_wait(20)
driver.set_page_load_timeout(50)
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title

username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')
username_input.send_keys('standard_user')
password_input.send_keys('secret_sauce')
login_btn.click()
cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
cart_icon.is_displayed()

time.sleep(3)
