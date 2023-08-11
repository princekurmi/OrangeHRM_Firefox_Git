from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By


class Test_Login:

    def test_login_001(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username = driver.find_element(By.XPATH, "//p[normalize-space()='Username : Admin']").text
        username = username[-5:]
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
        password = driver.find_element(By.XPATH, "//p[normalize-space()='Password : admin123']").text
        password = password[-8:]
        driver.find_element(By.CSS_SELECTOR, "*[name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").is_displayed()
            print("test_login_001 is Passed")
            driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            assert True
        except Ec:
            print("test_login_001 is Failed")
            assert False
        print("test_login_001 is Completed")
        driver.close()

    def test_AddEmp_001(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username = driver.find_element(By.XPATH, "//p[normalize-space()='Username : Admin']").text
        username = username[-5:]
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
        password = driver.find_element(By.XPATH, "//p[normalize-space()='Password : admin123']").text
        password = password[-8:]
        driver.find_element(By.CSS_SELECTOR, "*[name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Prince")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Kurmi")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # print(driver.find_element(By.XPATH,"//div[@class='oxd-toast oxd-toast--success
        # oxd-toast-container--toast']").text)
        try:
            driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
            print("test_AddEmp_001 is Passed")
            driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            addemp = True
        except Ec:
            print("test_AddEmp_001 is Failed")
            addemp = False
        if addemp:
            assert True
        else:
            assert False
        print("test_AddEmp_001 is Completed")
        driver.close()
