#generic
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if(browser=="chrome"):
        driver = webdriver.Chrome()
        print("launching chrome!!!")
    elif browser=="firefox":
        driver = webdriver.Firefox()
        print("launching firefox!!!")
    else:
        driver=webdriver.Edge()
        print("launching Edge!!!")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## pytest html report. ##########

def pytest_configure(config):
    config._metadata['Project Name'] = "Crud Application Flask"
    config._metadata['Module Name'] = 'Registration page DDT'
    config._metadata['Tester'] = "Shibasish"


# it is a hook for delete/modify environment info in to the html report.
# inorder to remove some non-essential(default) values generated automatically we will use pop to remove them.

# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    #command to run html repots = "pytest -v -s --html=reports\report.html testCase/test_register_DDT --browser chrome"