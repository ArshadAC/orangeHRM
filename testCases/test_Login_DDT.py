import pytest

from pageObjects.LoginPage import loginPage
from utilities import XLutils
from utilities.Logger import LogGenerator
from utilities.readproperties import Readconfig

class Test_Login_DDT:
    Url = Readconfig.geturl()
    # Username = Readconfig.getusername()
    # Password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "E:\\Automation Project\\OrangeHRM\\testCases\\TestData\\LoginData.xlsx"


    def test_Login_DDT_005(self,setup):
        self.driver = setup
        self.log.info("test_Login_DDT_005 is started")
        self.log.info("opening browser")
        self.driver.get(self.Url)
        self.log.info("Opening Url-->"  + self.Url)
        self.lp = loginPage(self.driver)
        self.rows = XLutils.getrowCount(self.path,"Sheet1")
        print("Number of rows are--->" + str(self.rows))
        login_Status = []
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, "Sheet1",r,2)
            self.password = XLutils.readData(self.path, "Sheet1",r,3)
            self.exp_result = XLutils.readData(self.path,"Sheet1",r,4)

            self.lp.Enter_UserName(self.username)
            self.log.info("Entering Username--->" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering Password--->" + self.password)
            self.lp.Click_Login()
            self.log.info("Click on Login Button")

            if self.lp.Login_Status() == True:
                if self.exp_result == "Pass":
                    self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_Login_DDT_Pass.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on Menu Button")
                    self.lp.Click_Logout()
                    self.log.info("Click on Logout Button")
                    login_Status.append("Pass")
                    XLutils.writeData(self.path,"Sheet1",r,5,"Pass")

                elif self.exp_result == "Fail":
                    self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_Login_DDT_Fail.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on Menu Button")
                    self.lp.Click_Logout()
                    self.log.info("Click on Logout Button")
                    login_Status.append("Fail")
                    XLutils.writeData(self.path, "Sheet1", r, 5, "Fail")

            else:
                if self.exp_result == "Pass":
                    login_Status.append("Fail")
                    XLutils.writeData(self.path,"Sheet1",r,5,"Fail")
                    self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_Login_DDT_Fail.png")

                elif self.exp_result == "Fail":
                    login_Status.append("Pass")
                    XLutils.writeData(self.path,"Sheet1",r,5,"Pass")
                    self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_Login_DDT_Pass.png")


        print(login_Status)
        if "Fail" not in login_Status:
            self.log.info("test_Login_DDT_005 is Passed")
            assert True
        else:
            self.log.info("test_Login_DDT_005 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_Login_DDT_005 iscompleted")
