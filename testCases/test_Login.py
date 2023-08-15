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

    @pytest.mark.sanity
    def test_Page_Title_001(self, setup):

        self.driver = setup
        self.log.info("test_Page_Title_001 started")
        self.log.info("opening browser")
        self.driver.get(self.Url)
        self.log.info("Go to this Url-->" + self.Url)
        if self.driver.title == "OrangeHRM":
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is-->" + self.driver.title)
            assert True
        else:
            self.log.info("test_Page_Title_001 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_Page_Title_001 is completed")

    @pytest.mark.regression
    def test_login_002(self, setup):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Opening Url -->" + self.Url)
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.lp = loginPage(self.driver)
        self.lp.Enter_UserName(self.Username)
        self.log.info("Entering username-->" + self.Username)
        # self.lp.Enter_UserName("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password -->" + self.Password)
        # self.lp.Enter_Password("admin123")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Click_Login()
        self.log.info("Click on Login Button")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(5)
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
        if self.lp.Login_Status() == True:

            self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_login_pass.png")
            self.lp.Click_Menu_Button()
            self.log.info("Click on Menu Button ")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")
            assert True
        else:
            assert False

        self.driver.close()
        self.log.info("test_login_002 is completed")
