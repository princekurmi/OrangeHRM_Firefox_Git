from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Add_Emp:
    XPATH_PIM = (By.XPATH, "//span[normalize-space()='PIM']")
    XPATH_Add_Emp = (By.XPATH, "//button[normalize-space()='Add']")
    XPATH_First_Name = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div['
                                  '1]/div/div/div[2]/div[1]/div[2]/input')
    XPATH_Last_Name = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div['
                                 '1]/div/div/div[2]/div[3]/div[2]/input')
    XPATH_Submit = (By.XPATH, "//button[@type='submit']")
    XPATH_Add_Success = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    XPATH_Menu = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    XPATH_Add_Emp_Again = (By.XPATH, "//a[normalize-space()='Add Employee']")

    def __init__(self, driver):
        self.driver = driver

    def click_PIM(self):
        self.driver.find_element(*Add_Emp.XPATH_PIM).click()

    def click_Add_Emp(self):
        self.driver.find_element(*Add_Emp.XPATH_Add_Emp).click()

    def enter_First_Name(self, firstname):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Add_Emp.XPATH_First_Name)
        )
        element.send_keys(firstname)

    def enter_Last_Name(self, lastname):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Add_Emp.XPATH_Last_Name)
        )
        element.send_keys(lastname)

    def click_Submit_Button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Add_Emp.XPATH_Submit)
        )
        element.click()

    def click_Add_Emp_Again(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Add_Emp.XPATH_Add_Emp_Again)
        )
        element.click()

    def success_Add_Emp(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(Add_Emp.XPATH_Add_Success)
            )
            return True
        except TimeoutException:
            return False

    # def click_PIM(self):
    #     self.driver.find_element(*Add_Emp.XPATH_PIM).click()
    #
    # def click_Add_Emp(self):
    #     self.driver.find_element(*Add_Emp.XPATH_Add_Emp).click()
    #
    # def enter_First_Name(self, firstname):
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Add_Emp.XPATH_First_Name)
    #     )
    #     element.send_keys(firstname)
    #
    # def enter_Last_Name(self, lastname):
    #     self.driver.find_element(*Add_Emp.XPATH_Last_Name).send_keys(lastname)
    #
    # def click_Submit_Button(self):
    #     self.driver.find_element(*Add_Emp.XPATH_Submit).click()
    #
    # def click_Add_Emp_Again(self):
    #     self.driver.find_element(*Add_Emp.XPATH_Add_Emp_Again).click()
    #
    # def success_Add_Emp(self):
    #     try:
    #         self.driver.find_element(*Add_Emp.XPATH_Add_Success)
    #         return True
    #     except NoSuchElementException:
    #         return False
