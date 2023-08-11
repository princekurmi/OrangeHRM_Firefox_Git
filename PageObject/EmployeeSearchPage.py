from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.readproperties import ReadConfig


class EmployeeSearch:
    search = ReadConfig.searchItem()
    XPATH_EmpName = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div["
                               "1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    XPATH_Search_Button = (By.XPATH, "//button[@type='submit']")
    XPATH_Search_Result = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div')

    # Class_name_SearchResult = (By.CLASS_NAME, "oxd-autocomplete-text-input oxd-autocomplete-text-input--focus")

    # "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > "
    # "div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) "
    # "> div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")

    def __init__(self, driver):
        self.driver = driver

    def enter_EmpName(self, empname):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(EmployeeSearch.XPATH_EmpName)
        )
        element.send_keys(empname)

    def click_Search_Button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(EmployeeSearch.XPATH_Search_Button))
        element.click()

    def search_Result(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(EmployeeSearch.XPATH_Search_Result))
            self.driver.find_elements(EmployeeSearch.XPATH_Search_Result)
            return True
        except:
            return True

    # def search_Result(self):
    #     serch = self.driver.find_element(*EmployeeSearch.CSS_Search_Result).text
    #     if serch == self.search:
    #         return True
    #     elif serch != self.search :
    #         print(self.driver.find_element(*EmployeeSearch.CSS_Search_Result).text)
    #         return False
