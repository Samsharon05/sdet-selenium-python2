import pytest
from pages.login_pageD09 import LoginPage
from pages.home_pageD09 import HomePage
from utils.configD09 import Configdata
from utils.test_data_readerD09 import get_test_data
from utils.data_generatorD09 import generate_random_email

config = Configdata()


class TestLogin:

    @pytest.mark.regression
    def test_login_success(self, driver):
        login = LoginPage(driver)
        home = HomePage(driver)

        data = get_test_data("valid_user")

        login.login(data["username"], data["password"])

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