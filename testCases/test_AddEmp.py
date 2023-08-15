import time
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from pageObjects.Add_Employee import AddEmployee
from pageObjects.LoginPage import loginPage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator

class Test_Add_Employee:

    Url =Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_Add_Emp_003(self,setup):
        self.diver = setup
        self.log.info("test_Add_Emp_003 is started")
        self.log.info("Oening Browser")
        self.diver.get(self.Url)
        self.log.info("Opening_Url--->" + self.Url)
        self.lp = loginPage(self.diver)
        self.lp.Enter_UserName(self.Username)
        self.log.info("Entering Username--->" + self.Username)
        # self.lp.Enter_UserName("Admin")
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password--->" + self.Password)
        # self.lp.Enter_Password("admin123")
        self.lp.Click_Login()
        self.log.info("Click Login Button")
        self.ae = AddEmployee(self.diver)
        self.ae.Click_PIM()
        self.log.info("Click PIM Button")
        self.ae.Click_Add()
        self.log.info("Click Add Customer Button")
        self.ae.Enter_Firstname("jhon")
        self.log.info("Entering first name Jhon")
        self.ae.Enter_Middlename("jay")
        self.log.info("Entering Middle Name--jay")
        self.ae.Enter_lastname("bush")
        self.log.info("Entering Lastname---bush")
        self.ae.Click_Save()
        self.log.info("Click on save Button")
        if self.ae.ADD_Employee_Status() == True:
            self.diver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_Add_Emp_Pass.png")
            self.log.info("test_Add_Emp_003 is Passed")
            assert True

        else:
            self.log.info("test_Add_Emp_003 is Failed")
            assert False
        self.diver.close()
        self.log.info("test_Add_Emp_003 is completed")