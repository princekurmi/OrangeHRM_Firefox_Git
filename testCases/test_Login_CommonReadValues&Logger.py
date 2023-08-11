from Utilities.readproperties import ReadConfig
from PageObject.AddEmpPage import Add_Emp
from PageObject.LoginPage import LoginPage
from Utilities.Logger import LogGenerator

class Test_ReadCommonValues:

    url = ReadConfig.geturl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.log_gen()

    def test_login_007(self, setup):
        self.driver = setup
        self.log.info("test_login_007 is started")
        self.driver.get(self.url)
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.log.info("Going to this URL-->"+self.url)
        self.lp.enter_Username(self.username)
        self.log.info("Entering Username-->"+self.username)
        self.lp.enter_Password(self.password)
        self.log.info("Entering Password-->"+self.password)
        self.lp.click_Login()
        self.log.info("Click on Login Button")
        if self.lp.login_Status():
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_login_007--Passed.png")
            self.lp.click_Menu()
            self.log.info("Click on Menu Button")
            self.lp.click_Logout()
            self.log.info("Click on Logout Button")
            assert True
            self.log.info("test_login_007 is Passed")
        else:
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_login_007--Failed.png")
            self.log.info("test_login_007 is Failed")
            assert False
        self.log.info("test_login_007 is Completed")
        print("test_login_007 is Completed")

        self.log.info("info")
        self.log.warning("warning")
        self.log.debug("debug")
        self.log.error("error")
        self.log.critical("critical")
        self.driver.close()

    def test_AddEmp_007(self, setup):
        self.driver = setup
        self.log.info("test_login_007 is started")
        self.driver.get(self.url)
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.log.info("Going to this URL-->"+self.url)
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
        self.ae.enter_First_Name("Prince")
        self.log.info("Enter First Name")
        self.ae.enter_Last_Name("Kurmi")
        self.log.info("Enter Last Name")
        self.ae.click_Submit_Button()
        self.log.info("Click on Submit Button")
        if self.ae.success_Add_Emp():
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_007--Passed.png")
            self.log.info("Employee Added Successfully")
            self.log.info("test_AddEmp_007 is Passed")
            self.lp.click_Menu()
            self.log.info("Click on Menu Dropdown")
            self.lp.click_Logout()
            self.log.info("Click on Logout Button")
            assert True
        else:
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_007--Failed.png")
            self.log.info("test_AddEmp_007 is Failed")
            assert False
        self.log.info("test_AddEmp_007 is Completed")
        print("test_AddEmp_007 is Completed")
        self.driver.close()
