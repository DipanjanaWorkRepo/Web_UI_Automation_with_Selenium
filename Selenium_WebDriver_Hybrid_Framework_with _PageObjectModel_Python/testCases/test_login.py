from selenium import webdriver
from pageObject.logInPage import logInPage
import pytest
from utilities.readProperties import readConfig
from utilities.customLogger import logGen

class Test_001_login:
    base_url = readConfig.getApplURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = logGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self, setup):  # setup class from pytest.fixure defined in conftest.py

        self.logger.info("********** Verifying HomePage Test **********")
        self.driver = setup  # setup fixture provides driver details
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.logger.info("********** HomePage Test Passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            assert False
            self.logger.error("********** HomePage Test Failed **********")  #logger capturing error msg
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("********** Verifying LogIn Test **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = logInPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassWord(self.password)
        self.login_page.clickLogIn()

        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** LogIn Test Passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.logger.error("********** LogIn Test Failed **********")
            self.driver.close()

