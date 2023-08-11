import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
username = driver.find_element(By.XPATH,"//p[normalize-space()='Username : Admin']").text
username = username[-5:]
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
password = driver.find_element(By.XPATH,"//p[normalize-space()='Password : admin123']").text
password = password[-8:]
driver.find_element(By.CSS_SELECTOR,"*[name='password']").send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
time.sleep(5)