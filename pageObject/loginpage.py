from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    # find the login button
    homelink_xpath="//a[@id='homelink']"
    registerlink_xpath="//a[@id='registerlink']"
    dropdownlink_xpath="//a[@id='dropdownlink']"
    alertslink_xpath="//a[@id='alertslink']"

    usernametbx_xpath="//input[@id='exampleInputEmail1']"
    passwordtbx_xpath="//input[@id='exampleInputPassword1']"
    singupbtn_xpath="//button[@type='submit']"


    # creating a default constructor to initialize the datamembers
    def __init__(self,driver):
        self.driver=driver

    # function to click on login link
    def clickOnHomeLink(self):
        self.driver.find_element(By.XPATH,self.homelink_xpath).click()
    def clickOnRegisterLink(self):
        self.driver.find_element(By.XPATH,self.registerlink_xpath).click()
    def clickOnDropdownLink(self):
        self.driver.find_element(By.XPATH,self.dropdownlink_xpath).click()
    def clickOnAlertsLink(self):
        self.driver.find_element(By.XPATH,self.alertslink_xpath).click()
    def login_form(self,username,password):
        self.driver.find_element(By.XPATH,self.usernametbx_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,self.passwordtbx_xpath).send_keys(password)
        self.driver.find_element(By.XPATH,self.singupbtn_xpath).click()

        # in the above function we have used self becoz functions are present in home class