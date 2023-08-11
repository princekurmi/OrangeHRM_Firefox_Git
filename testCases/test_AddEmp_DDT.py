import time

import pytest

from PageObject.AddEmpPage import Add_Emp
from PageObject.LoginPage import LoginPage
from Utilities import XLutils
from Utilities.Logger import LogGenerator
from Utilities.readproperties import ReadConfig


class Test_AddEmp_DDT:
    url = ReadConfig.geturl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.log_gen()
    path = "D:\\Software Testing\\TK OrangeHRM\\testCases\\TestData\\EmployeeList.xlsx"

    @pytest.mark.sanity
    def test_AddEmp_DDT_009(self, setup):
        self.log.info("test_DDT_009 has Started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Going to URL-->" + self.url)
        self.lp = LoginPage(self.driver)
        self.lp.enter_Username(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.click_Login()
        self.log.info("Clicking on Login Button")
        self.ae = Add_Emp(self.driver)
        self.ae.click_PIM()
        self.ae.click_Add_Emp()
        self.rows = XLutils.getRowCount(self.path, "Sheet1")
        print("Number of rows are-->", self.rows)
        self.log.info(f"Number of rows are-->{self.rows}")

        # self.firstname = XLutils.readData(self.path,"Sheet1",2,2)
        # print(self.firstname)
        self.status_list = []
        for r in range(2, self.rows + 1):
            self.firstName = XLutils.readData(self.path, "Sheet1", r, 2)
            self.lastName = XLutils.readData(self.path, "Sheet1", r, 3)
            self.ae.enter_First_Name(self.firstName)
            self.log.info("Entering FirstName-->" + self.firstName)
            self.ae.enter_Last_Name(self.lastName)
            self.log.info("Entering LastName-->" + self.lastName)
            self.ae.click_Submit_Button()
            self.log.info("Clicking on Submit Button")
            if self.ae.success_Add_Emp():
                self.ae.click_Add_Emp_Again()
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_DDT_009--Passed.png")
                self.log.info("Employee Added Successfully")
                self.status_list.append("Pass")
                XLutils.writeData(self.path, "Sheet1", r, 4, "Pass")
            else:
                self.ae.click_Add_Emp_Again()
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_DDT_009--Failed.png")
                self.status_list.append("Fail")
                XLutils.writeData(self.path, "Sheet1", r, 4, "Fail")
        self.lp.click_Menu()
        self.log.info("Click on Menu Dropdown")
        self.lp.click_Logout()
        self.log.info("Click on Logout Button")
        self.log.info("test_AddEmp_DDT_009 is Completed")
        if "Fail" not in self.status_list:
            self.log.info("test_AddEmp_DDT_009 is Passed")
            assert True
        else:
            self.log.info("test_AddEmp_DDT_009 is Failed")
            assert False
        self.driver.close()
