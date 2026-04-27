import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import Configdata
from utils.data_generator import generate_random_email
from utils.test_datareader import get_test_data
from utils.loggers import get_logger

log = get_logger()

config= Configdata()


data = Configdata()


class TestLogin:

    @pytest.mark.smoke
    def test_login_success(self, driver):
        login = LoginPage(driver)
        home = HomePage(driver)

        login.login(data.login_username, data.login_password)

        assert home.is_inventory_visible()

    @pytest.mark.regression
    def test_login_invalid(self, driver):
        login = LoginPage(driver)

        login.login("wrong", "wrong")

        assert "username and password do not match" in login.get_error_message().lower()
        
    @pytest.mark.regression
    def test_inventory_loaded(self, driver):
        login = LoginPage(driver)
        home = HomePage(driver)

        login.login("standard_user", "secret_sauce")

        assert home.is_inventory_visible()
    
    @pytest.mark.regression
    def test_login_invalid(self, driver):
        login = LoginPage(driver)

        data = get_test_data("invalid_user")

        login.login(data["username"], data["password"])

        assert "username and password do not match" in login.get_error_message().lower()
        
    def test_runtime_data(self):
        email = generate_random_email()
        assert "@test.com" in email
    

    @pytest.mark.smoke
    def test_login_succes(self, driver):
        log.info("Starting test")

        login = LoginPage(driver)
        home = HomePage(driver)

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