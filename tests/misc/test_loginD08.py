import pytest
from pages.login_pageD08 import LoginPage
from pages.home_pageD08 import HomePage
from utils.config import Configdata

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