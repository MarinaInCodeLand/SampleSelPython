from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Test_global:
    driver = None

def test_Sample1():
    s = Service("C:/Users/Milena/PycharmProjects/SampleSelPython/proba/driver/chromedriver.exe")
    Test_global.driver = webdriver.Chrome(service=s)

    Test_global.driver.maximize_window()
    Test_global.driver.implicitly_wait(20)
    Test_global.driver.set_page_load_timeout(50)
    Test_global.driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in Test_global.driver.title


def test_navReg():
    username_input = Test_global.driver.find_element(By.ID, 'user-name')
    password_input = Test_global.driver.find_element(By.ID, 'password')
    login_btn = Test_global.driver.find_element(By.ID, 'login-button')
    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')
    login_btn.click()
    cart_icon = Test_global.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.is_displayed()
    time.sleep(3)

def test_addToCart():
    add_cart_btn = Test_global.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_cart_btn.click()
    cart_icon = Test_global.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()
    remove_cart_btn = Test_global.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_cart_btn.is_displayed()


def test_logout():
    hamburger = Test_global.driver.find_element(By.ID, 'react-burger-menu-btn')
    hamburger.click()
    logout_btn = Test_global.driver.find_element(By.ID, 'logout_sidebar_link')
    logout_btn.click()
    new_login_btn = Test_global.driver.find_element(By.XPATH, "//input[@id='login-button']")
    new_login_btn.is_displayed()

def test_twoNavReg():
    username_input = Test_global.driver.find_element(By.ID, 'user-name')
    password_input = Test_global.driver.find_element(By.ID, 'password')
    login_btn = Test_global.driver.find_element(By.ID, 'login-button')
    username_input.send_keys('performance_glitch_user')
    password_input.send_keys('secret_sauce')
    login_btn.click()
    cart_icon = Test_global.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.is_displayed()
    time.sleep(3)

def test_remove_product():
    add_cart_btn = Test_global.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_cart_btn.click()
    cart_icon = Test_global.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()
    remove_cart_btn = Test_global.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_cart_btn.click()
    removed_item = Test_global.driver.find_element(By.CLASS_NAME, 'removed_cart_item')
    removed_item.is_displayed()


def test_sort_by_price():
    product_filter = Test_global.driver.find_element(By.CLASS_NAME, 'product_sort_container')
    product_filter.click()
    product_filter.send_keys('Price (high to low)')
    product_filter.is_displayed()