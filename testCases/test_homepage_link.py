import pytest
from utilities.customlogger import LogGen
from utilities.readProperty import Read_config
from selenium import webdriver
from pageObject.homepage import Home

# creating class
class Test_01_homepage:
    baseurl=Read_config.getApplicationurl()
    logg=LogGen.logGen()
    # creating a function to check homepage is displayed or not
    def test_homepage_title(self,setup):
        self.logg.info("**********Test_01_login*********")
        self.logg.info("*********verifying_homepage_title*******")
        self.driver=setup
        # launch the browser
        self.driver.get(self.baseurl)
        # get the title of the login page
        actual_home_title=self.driver.title

        # compare the title
        if actual_home_title=="FLASK-CRUD_APP_home_page.":
            assert True
            self.logg.info("*** home page title is passed ****")
            # close the browser
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepage_title.png")
            # close the browser
            self.driver.close()
            self.logg.info("**** home page title is failed *****")
            assert False

    # creating a function to check homepage is displayed or not
    def test_login_title(self, setup):
        self.logg.info("*********verifying_login_title*******")
        self.driver = setup
        # launch the browser
        self.driver.get(self.baseurl)
        # make an object of the home class
        self.hp=Home(self.driver)
        # now call the methods from the home class to perform the clicking on login link
        self.hp.clickOnLoginLink()
        # after navigation to the login page .get the title of the login page
        actual_login_title=self.driver.title

        # compare the title
        if actual_login_title == "FLASK-CRUD_APP_login_page.":
            assert True
            self.logg.info("*** login page title is passed ****")
            # close the browser
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_loginpage_title.png")
            # close the browser
            self.driver.close()
            self.logg.info("**** login page title is failed *****")
            assert False

    # creating a function to check Register page is displayed or not
    def test_register_title(self, setup):
        self.logg.info("*********verifying_register_title*******")
        self.driver = setup
        # launch the browser
        self.driver.get(self.baseurl)
        # make an object of the home class
        self.hp = Home(self.driver)
        # now call the methods from the home class to perform the clicking on login link
        self.hp.clickOnRegisterLink()
        # after navigation to the login page .get the title of the login page
        actual_title = self.driver.title

        # compare the title
        if actual_title == "FLASK-CRUD_APP_register_page.":
            assert True
            self.logg.info("*** Register page title is passed ****")
            # close the browser
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_loginpage_title.png")
            # close the browser
            self.driver.close()
            self.logg.info("**** Register page title is failed *****")
            assert False

    # creating a function to check Dropdown page is displayed or not
    def test_Dropdown_title(self, setup):
        self.logg.info("*********verifying_Dropdown_title*******")
        self.driver = setup
        # launch the browser
        self.driver.get(self.baseurl)
        # make an object of the home class
        self.hp = Home(self.driver)
        # now call the methods from the home class to perform the clicking on login link
        self.hp.clickOnDropdownLink()
        # after navigation to the login page .get the title of the login page
        actual_title = self.driver.title

        # compare the title
        if actual_title == "FLASK-CRUD_APP_dropdown_checkbox_page.":
            assert True
            self.logg.info("*** Dropdown page title is passed ****")
            # close the browser
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_loginpage_title.png")
            # close the browser
            self.driver.close()
            self.logg.info("**** Dropdown page title is failed *****")
            assert False

    # creating a function to check Alerts page is displayed or not
    def test_Alerts_title(self, setup):
        self.logg.info("*********verifying_Alerts_title*******")
        self.driver = setup
        # launch the browser
        self.driver.get(self.baseurl)
        # make an object of the home class
        self.hp = Home(self.driver)
        # now call the methods from the home class to perform the clicking on login link
        self.hp.clickOnAlertsLink()
        # after navigation to the login page .get the title of the login page
        actual_title = self.driver.title

        # compare the title
        if actual_title == "FLASK-CRUD_APP_alerts_page.":
            assert True
            self.logg.info("*** Alerts page title is passed ****")
            # close the browser
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_loginpage_title.png")
            # close the browser
            self.driver.close()
            self.logg.info("**** Alerts page title is failed *****")
            assert False

