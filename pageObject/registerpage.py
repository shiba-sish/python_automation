from selenium import webdriver
from selenium.webdriver.common.by import By

class Register:
    # find the login button
    Loginlink_xpath="//a[text()='Login']"
    homelink_xpath="//a[@id='homelink']"
    dropdownlink_xpath="//a[@id='dropdownlink']"
    alertslink_xpath="//a[@id='alertslink']"
    registerlink_xpath="//a[@id='registerlink']"

    usernametbx_xpath = "//input[@id='exampleInputEmail1']"
    passwordtbx_xpath = "//input[@id='exampleInputPassword1']"
    registerbtn_xpath = "//button[@type='submit']"


    # creating a default constructor to initialize the datamembers
    def __init__(self,driver):
        self.driver=driver

    # function to click on login link
    def clickOnLoginLink(self):
        self.driver.find_element(By.XPATH,self.Loginlink_xpath).click()
    def clickOnHomeLink(self):
        self.driver.find_element(By.XPATH,self.homelink_xpath).click()
    def clickOnDropdownLink(self):
        self.driver.find_element(By.XPATH,self.dropdownlink_xpath).click()
    def clickOnAlertsLink(self):
        self.driver.find_element(By.XPATH,self.alertslink_xpath).click()
    def clickOnRegisterLink(self):
        self.driver.find_element(By.XPATH,self.registerlink_xpath).click()

    def register_form(self, username, password):
         self.driver.find_element(By.XPATH, self.usernametbx_xpath).send_keys(username)
         self.driver.find_element(By.XPATH, self.passwordtbx_xpath).send_keys(password)
         self.driver.find_element(By.XPATH, self.registerbtn_xpath).click()
        # in the above function we have used self becoz functions are present in home class