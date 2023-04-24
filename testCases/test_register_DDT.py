from pageObject.registerpage import Register
from utilities import XLutils

from utilities.customlogger import LogGen
from utilities.readProperty import Read_config


class Test_003_DDT_register:
    #homepage URL
    baseurl=Read_config.getApplicationurl()
    # username=Read_config.getApplicationurl()
    # password=Read_config.getApplicationurl()
    #to generate logs report
    logg=LogGen.logGen()

    #path of excel sheet
    path=".//testdata/RegistrationData.xlsx"

    def test_register_ddt(self,setup):
        #always mention test case ID in the class name
        self.logg.info("\n********** Test_003 *********\n")
        self.logg.info("*********  verifying registration process  *******")
        self.driver = setup
        #open register page directly
        self.driver.get("http://127.0.0.1:5000/register")
        #create a referance variable of pom class
        self.rp=Register(self.driver)
        #fatch the data from excel sheet
        self.rows=XLutils.get_row_count(self.path,"Sheet1")
        # self.col=XLutils.get_column_count(self.path,"Sheet1")
        result_list=[] #empty list
        for i in range (2,self.rows+1):
            self.username=XLutils.read_data(self.path,"Sheet1",i,1)
            self.password=XLutils.read_data(self.path,"Sheet1",i,2)
            #expected result we have to verify latter
            self.expected_result=XLutils.read_data(self.path,"Sheet1",i,3)
            self.rp.register_form(username=self.username, password=self.password)

            #verify login page title
            act_title=self.driver.title
            exp_title="FLASK-CRUD_APP_login_page."

            # compare the title
            if act_title == exp_title:
                if self.expected_result=="pass":
                    self.logg.info("*** Register page  is passed ****")
                    #now comeback to register page
                    self.rp.clickOnRegisterLink()
                    result_list.append("pass")
                else:
                    self.logg.error("*** Register page  is Failed ****")
                    # now comeback to register page
                    self.rp.clickOnRegisterLink()
                    result_list.append("Fail")

            elif act_title!=exp_title:
                self.logg.error("***** Fail *****")
                result_list.append("Fail")

            self.logg.info("\n********** Test_003_DDT_register ***********\n")
            self.logg.info("\n********** Test case Done ***********\n")





#Note: inn python excel row no starts from 1 as shown in excel
