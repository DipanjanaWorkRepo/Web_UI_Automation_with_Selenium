from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup(browser):

    if browser=='chrome':
        driver = webdriver.Chrome(executable_path=r"C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/chromedriver.exe")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path=r"C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/geckodriver.exe")
    else:
        # setting up chrome as default browser if by mistake no browser type is specified in CLI command
        driver = webdriver.Chrome(
            executable_path=r"C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/chromedriver.exe")


    return driver

def pytest_addoption(parser):  #This will get value from the command prompt
    parser.addoption(parser)

@pytest.fixture(scope="session")
def browser(request):  #This will return the browser value to the setup() method above
    return request.config.getoption("--browser")

# Hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Dipanjana'

# Hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)