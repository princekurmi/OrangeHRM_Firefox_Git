import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.AddEmpPage import Add_Emp
from PageObject.EmployeeSearchPage import EmployeeSearch
from PageObject.LoginPage import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.readproperties import ReadConfig


class Test_EmpSearch:
    url = ReadConfig.geturl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    search = ReadConfig.searchItem()

    @pytest.mark.sanity
    def test_empsearch_005(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.es = EmployeeSearch(self.driver)
        self.ae = Add_Emp(self.driver)
        self.log = LogGenerator.log_gen()

        self.log.info("test_empsearch_005 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp.enter_Username(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.click_Login()
        self.log.info("Click on Login Button")
        self.ae.click_PIM()
        self.log.info("CLick on PIM Menu")
        self.es.enter_EmpName(self.search)
        self.log.info(f"Search-->{self.search}")
        self.log.info("Entering EmpName to Search")
        self.es.click_Search_Button()
        self.log.info("Click on Search Button")
        time.sleep(5)
        if self.es.search_Result():
            self.log.info("Search Found")
            self.driver.save_screenshot(
                "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_empsearch_005--Passed.png")
            self.lp.click_Menu()
            self.log.info("Click on Menu Button")
            self.lp.click_Logout()
            self.log.info("Click on Logout Button")
            self.log.info("test_empsearch_005 is Passed")
            assert True
        else:
            self.log.info("No Search Found")
            self.driver.save_screenshot(
                "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_empsearch_005--Failed.png")
            self.log.info("test_empsearch_005 is Failed")
            assert False
        self.driver.close()
