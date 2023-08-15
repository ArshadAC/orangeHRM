from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By


class AddEmployee:
    Click_PIM_Button_XPATH = (By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"
                                       "[normalize-space()='PIM']")
    Click_Add_Button_XPATH = (By.XPATH,"//button[normalize-space()='Add']")
    Text_Firstname_XPATH = (By.XPATH,"//input[@placeholder='First Name']")
    Text_MiddleName_XPATH = (By.XPATH,"//input[@placeholder='Middle Name']")
    Text_LastName_XPATH = (By.XPATH,"//input[@placeholder='Last Name']")
    Click_Save_Button_XPATH = (By.XPATH,"//button[@type='submit']")
    Click_Personal_Detail = (By.XPATH,"//a[@class='orangehrm-tabs-item --active']")

    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_Button_XPATH).click()

    def Click_Add(self):
        self.driver.find_element(*AddEmployee.Click_Add_Button_XPATH).click()

    def Enter_Firstname(self,firstname):
        self.driver.find_element(*AddEmployee.Text_Firstname_XPATH).send_keys(firstname)

    def Enter_Middlename(self,middlename):
        self.driver.find_element(*AddEmployee.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_lastname(self,lastname):
        self.driver.find_element(*AddEmployee.Text_LastName_XPATH).send_keys(lastname)

    def Click_Save(self):
        self.driver.find_element(*AddEmployee.Click_Save_Button_XPATH).click()

    def ADD_Employee_Status(self):
        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element(*AddEmployee.Click_Personal_Detail)
            return True
        except Ec:
            return False

