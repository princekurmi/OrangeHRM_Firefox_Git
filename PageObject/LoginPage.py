from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    XPATH_UserName = (By.XPATH, "//input[@placeholder='Username']")
    CSS_Password = (By.CSS_SELECTOR, "*[name='password']")
    XPATH_Login_Button = (By.XPATH, "//button[@type='submit']")
    XPATH_Menu_Button = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    XPATH_Logout = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def enter_Username(self,username):
        self.driver.find_element(*LoginPage.XPATH_UserName).send_keys(username)

    def enter_Password(self, password):
        self.driver.find_element(*LoginPage.CSS_Password).send_keys(password)

    def click_Login(self):
        self.driver.find_element(*LoginPage.XPATH_Login_Button).click()

    def click_Menu(self):
        self.driver.find_element(*LoginPage.XPATH_Menu_Button).click()

    def click_Logout(self):
        self.driver.find_element(*LoginPage.XPATH_Logout).click()

    def login_Status(self):
        try:
            self.driver.find_element(*LoginPage.XPATH_Menu_Button)
            return True
        except NoSuchElementException:
            return False
