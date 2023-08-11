import pytest

from PageObject.LoginPage import LoginPage
from Utilities import XLutils
from Utilities.Logger import LogGenerator
from Utilities.readproperties import ReadConfig


class Test_Login_DDT:
    url = ReadConfig.geturl()
    path = "D:/Software Testing/TK OrangeHRM/testCases/TestData/LoginScenarios.xlsx"
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_Page_Title_001(self, setup):
        self.driver = setup
        self.log.info("test_Page_Title_001 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Going to this url-->" + self.url)
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is-->" + self.driver.title)
        else:
            self.log.info("test_Page_Title_001 is Failed")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    def test_Login_DDT_10(self, setup):
        self.driver = setup
        self.log.info("test_Login_DDT_10 has Started")
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Opening this URL-->" + self.url)
        self.row = XLutils.getRowCount(self.path, "Sheet1")
        self.log.info("The number of rows are-->" + str(self.row))
        self.status_list = []
        for row in range(2, self.row + 1):
            self.scenario = XLutils.readData(self.path, "Sheet1", row, 4)
            self.user = XLutils.readData(self.path, "Sheet1", row, 2)
            self.pwd = XLutils.readData(self.path, "Sheet1", row, 3)
            self.lp.enter_Username(self.user)
            self.log.info("Entering Username-->" + self.user)
            self.lp.enter_Password(self.pwd)
            self.log.info("Entering Password-->" + self.pwd)
            self.lp.click_Login()
            self.log.info("Clicking On Login Button")
            if self.lp.login_Status():
                self.status_list.append("Pass")
                self.log.info("Login is Done")
                XLutils.writeData(self.path, "Sheet1", row, 5, "Pass")
                self.driver.save_screenshot(
                    f"D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_Login_DDT_10-{self.scenario}-Passed.png")
                self.lp.click_Menu()
                self.log.info("Clicking on Menu Button")
                self.lp.click_Logout()
                self.log.info("Clicking on Logout")
            elif not self.lp.login_Status():
                self.status_list.append("Fail")
                self.driver.save_screenshot(
                    f"D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_Login_DDT_10-{self.scenario}-Failed.png")
                self.log.info("Login was Failed")
                XLutils.writeData(self.path, "Sheet1", row, 5, "Fail")
        self.log.info(f"Status list-->{self.status_list}")
        print(self.status_list)
        self.driver.close()
        if self.status_list[0] == "Pass" and self.status_list[1:] == ["Fail", "Fail", "Fail"]:
            self.log.info("test_Login_DDT_10 is Passed")
            assert True
        else:
            self.log.info("test_Login_DDT_10 is Failed")
            assert False
        self.log.info("test_Login_DDT_10 is Completed")
        # assert any(status == "Pass" for status in self.status_list), "Test case failed: No 'Pass' status found"
        # if "Pass" not in self.status_list:
        #     raise AssertionError("Test case failed: No 'Pass' status found")
