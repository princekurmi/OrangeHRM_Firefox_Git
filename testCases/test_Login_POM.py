import time

from PageObject.AddEmpPage import Add_Emp
from PageObject.LoginPage import LoginPage


class Test_POM:

    def test_login_0001(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.enter_Username("Admin")
        self.lp.enter_Password("admin123")
        self.lp.click_Login()
        if self.lp.login_Status():
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_login_0001--Passed.png")
            self.lp.click_Menu()
            self.lp.click_Logout()
            assert True
        else:
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_login_0001--Failed.png")
            assert False
        print("test_login_0001 is Completed")
        self.driver.close()

    def test_AddEmp_0001(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.ae = Add_Emp(self.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.enter_Username("Admin")
        self.lp.enter_Password("admin123")
        self.lp.click_Login()

        self.ae.click_PIM()
        self.ae.click_Add_Emp()
        self.ae.enter_First_Name("Prince")
        self.ae.enter_Last_Name("Kurmi")
        self.ae.click_Submit_Button()
        if self.ae.success_Add_Emp():
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_0001--Passed.png")
            self.lp.click_Menu()
            self.lp.click_Logout()
            assert True
        else:
            self.driver.save_screenshot("D:\\Software Testing\\TK OrangeHRM\\Screenshots\\test_AddEmp_0001--Failed.png")
            assert False
        print("test_AddEmp_0001 is Completed")
        self.driver.close()
