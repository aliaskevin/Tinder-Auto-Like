from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Use Facebook user name and password
user_name = os.environ.get("user")
password = os.environ.get("pass")

# Opening Tinder using selenium
driver = webdriver.Firefox()
driver.get("https://www.tinder.com")
time.sleep(4)

# Clickinn Login button
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(3)
# Handling hurdles of login though Facebook
try:
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
except NoSuchElementException:
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
time.sleep(5)
# Swithching to Pop-up Facebook window to fill username and password
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
user = driver.switch_to.active_element
user.send_keys(user_name)
user.send_keys(Keys.TAB)
user_pass = driver.switch_to.active_element
user_pass.send_keys(password)
user_pass.send_keys(Keys.ENTER)
time.sleep(7)
# Dismissing popups
driver.switch_to.window(base_window)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()
time.sleep(5)
# Accepting cookies
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]').click()
time.sleep(6)
# Auto liking 100 times
for n in range(100):
    try:
        driver.find_element(By.CSS_SELECTOR, '.Bgi\(\$g-ds-background-like\)\:a').click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
        except NoSuchElementException:
            print("no such element")
    finally:
        time.sleep(3)
