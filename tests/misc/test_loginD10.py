from selenium.webdriver.common.by import By
from pages.base_pageD10 import BasePage
from pages.login_pageD10 import LoginPage
from pages.home_pageD10 import homePage
from utils.configD10 import Configdata
import pytest
from utils.test_datareaderD10 import get_test_data
from utils.loggersD10 import get_logger

log = get_logger()

config= Configdata()


class TestLogin:
        
    @pytest.mark.smoke
    def test_login_succes(self, driver):
        log.info("Starting test")

        login = LoginPage(driver)
        home = homePage(driver)
        
        data = get_test_data("valid_user")

        log.info("Logging in with valid user")
        login.login(data["username"], data["password"])
        
        assert home.is_inventory_visible()

        log.info("Login successful")


    @pytest.mark.regression
    def test_login_invalid(self, driver):
        log.info("Starting test_login_invalid")

        login = LoginPage(driver)
        
        data = get_test_data("invalid_user")

        log.info("Logging in with invalid user")
        login.login(data["username"], data["password"])
        
        error = login.get_error_message().lower()

        log.info(f"Error message displayed: {error}")

        assert "username and password do not match" in error

        log.info("Invalid login test passed")
        
        log.info("THIS SHOULD APPEAR IN FILE")