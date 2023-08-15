import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import loginPage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login:

    Url =Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_login_params_004(self, setup,getDataforlogin):
        self.driver = setup
        self.log.info("test_login_params_004 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Opening Url -->" + self.Url)
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.lp = loginPage(self.driver)
        self.lp.Enter_UserName(getDataforlogin[0])
        # self.lp.Enter_UserName(self.Username)
        self.log.info("Entering username-->" + (getDataforlogin[0]))
        # self.log.info("Entering username-->" + self.Username)
        # self.lp.Enter_UserName("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_Password(getDataforlogin[1])
        # self.lp.Enter_Password(self.Password)
        self.log.info("Entering pasword-->" + (getDataforlogin[1]))
        # self.log.info("Entering Password -->" + self.Password)
        # self.lp.Enter_Password("admin123")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Click_Login()
        self.log.info("Click on Login Button")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        # try:
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        #     print("test_login_001 is Passed")
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     login = True
        #     # assert True
        #     print(login)
        # except Ec:
        #     print("test_login_001 is Failed")
        #     print("test_login_001 is completed")
        #     login = False
        #     print(login)
        #     # assert False
        # if login == True:
        #     assert True
        # else:
        #     assert False
        # print(self.lp.Login_Status())

        StatusList = []
        if self.lp.Login_Status() == True:
            if getDataforlogin[2] =="Pass":
                self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_login_pass1.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on Menu Button ")
                self.lp.Click_Logout()
                self.log.info("Click on Logout Button")
                self.log.info("test_login_params_004 passed")
                StatusList.append("Pass")

            elif getDataforlogin[2] =="Fail":
                self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_login_fail2.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on Menu Button ")
                self.lp.Click_Logout()
                self.log.info("Click on Logout Button")
                self.log.info("test_login_params_004 is failed")
                StatusList.append("Fail")

        else:
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_login_fail3.png")
                self.log.info("test_login_params_004 Failed")
                StatusList.append("Fail")

            elif getDataforlogin[2] =="Fail":
                self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_login_pass.png")
                self.log.info("test_login_params_004 passed")
                StatusList.append("Pass")

        if "Fail" not in StatusList:
            assert True
            self.log.info("test_login_params_004 is Passed")
        else:
            assert False
            self.log.info("test_login_params_004 is failed")
        self.driver.close()
        self.log.info("test_login_002 is completed")


