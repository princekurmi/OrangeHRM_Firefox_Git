from Utilities.readproperties import ReadConfig
from PageObject.AddEmpPage import Add_Emp
from PageObject.LoginPage import LoginPage
from Utilities.Logger import LogGenerator


class Test_ReadCommonValues:
    url = ReadConfig.geturl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.log_gen()

    def test_login_008(self, setup, getDataForLogin):
        self.driver = setup
        self.log.info("test_login_008 is started")
        self.driver.get(self.url)
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.log.info("Going to this URL-->" + self.url)
        self.lp.enter_Username(getDataForLogin[0])
        self.log.info("Entering Username-->" + getDataForLogin[0])
        self.lp.enter_Password(getDataForLogin[1])
        self.log.info("Entering Password-->" + getDataForLogin[1])
        self.lp.click_Login()
        self.log.info("Click on Login Button")
        if self.lp.login_Status():
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_login_008--Passed.png")
                self.lp.click_Menu()
                self.log.info("Click on Menu Button")
                self.lp.click_Logout()
                self.log.info("Click on Logout Button")
                assert True
                self.log.info("test_login_008 is Passed")
            else:
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_Login_008--Failed.png")
                self.log.info("test_Login_008 is Failed")
                assert False
        else:
            if getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_login_008--Passed.png")
                self.log.info("test_login_008 is Failed")
                assert True
            else:
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_Login_008--Failed.png")
                self.log.info("test_Login_008 is Failed")
                assert False
        self.log.info("test_login_008 is Completed")
        print("test_login_008 is Completed")

    def test_AddEmp_008(self, setup, getDataForEmp):
        self.driver = setup
        self.log.info("test_AddEmp_008 is started")
        self.driver.get(self.url)
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.log.info("Going to this URL-->" + self.url)
        self.ae = Add_Emp(self.driver)
        self.lp.enter_Username(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.click_Login()
        self.log.info("Click Login Button")

        self.ae.click_PIM()
        self.log.info("Click on PIM Menu")
        self.ae.click_Add_Emp()
        self.log.info("Click on Add Button")
        self.ae.enter_First_Name(getDataForEmp[0])
        self.log.info("Enter First Name-->"+getDataForEmp[0])
        self.ae.enter_Last_Name(getDataForEmp[1])
        self.log.info("Enter Last Name-->"+getDataForEmp[1])
        self.ae.click_Submit_Button()
        self.log.info("Click on Submit Button")
        if self.ae.success_Add_Emp():
            if getDataForEmp[2] == "Pass":
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_008--Passed.png")
                self.log.info("Employee Added Successfully")
                self.log.info("test_AddEmp_008 is Passed")
                self.lp.click_Menu()
                self.log.info("Click on Menu Dropdown")
                self.lp.click_Logout()
                self.log.info("Click on Logout Button")
                assert True
            else:
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_008--Failed.png")
                self.log.info("test_AddEmp_008 is Failed")
                assert False
        else:
            if getDataForEmp[2] == "Fail":
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_008--Passed.png")
                self.log.info("test_AddEmp_008 is Passed")
                assert True
            else:
                self.driver.save_screenshot(
                    "D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_008--Failed.png")
                self.log.info("test_AddEmp_008 is Failed")
                assert False

        self.log.info("test_AddEmp_008 is Completed")
        print("test_AddEmp_008 is Completed")
        self.driver.close()
