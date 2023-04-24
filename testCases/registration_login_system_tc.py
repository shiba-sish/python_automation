import pytest

from pageObject.loginpage import Login
from utilities.customlogger import LogGen
from utilities.readProperty import Read_config
from selenium import webdriver
from pageObject.homepage import Home

# creating class
class Test_01_homepage:
    baseurl=Read_config.getApplicationurl()
    username=Read_config.getApplicationurl()
    password=Read_config.getApplicationurl()
    logg=LogGen.logGen()
    # creating a function to check homepage is displayed or not
    def test_registration_login(self,setup):
        self.logg.info("**********Test_01_*********")
        self.logg.info("*********verifying_System_testcase*******")
        self.driver=setup
        # launch the browser
        self.driver.get(self.baseurl)
        self.hp=Home(self.driver)
        self.hp.clickOnLoginLink()
        self.lp=Login(self.driver)
        self.lp.login_form(self.username,self.password)
        # get the title of the page
        actual_home_title=self.driver.title

        # compare the title
        if actual_home_title=="FLASK-CRUD_APP_Dashboard_page.":
            assert True
            self.logg.info("*** Dashboard page title is passed ****")
            # close the browser
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepage_title.png")
            # close the browser
            self.driver.close()
            self.logg.info("**** dashboard page title is failed *****")
            assert False