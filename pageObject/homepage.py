from selenium import webdriver
from selenium.webdriver.common.by import By

class Home:
    # find the login button
    Loginlink_xpath="//a[text()='Login']"
    registerlink_xpath="//a[@id='registerlink']"
    dropdownlink_xpath="//a[@id='dropdownlink']"
    alertslink_xpath="//a[@id='alertslink']"


    # creating a default constructor to initialize the datamembers
    def __init__(self,driver):
        self.driver=driver

    # function to click on login link
    def clickOnLoginLink(self):
        self.driver.find_element(By.XPATH,self.Loginlink_xpath).click()
    def clickOnRegisterLink(self):
        self.driver.find_element(By.XPATH,self.registerlink_xpath).click()
    def clickOnDropdownLink(self):
        self.driver.find_element(By.XPATH,self.dropdownlink_xpath).click()
    def clickOnAlertsLink(self):
        self.driver.find_element(By.XPATH,self.alertslink_xpath).click()
        # in the above function we have used self becoz functions are present in home class