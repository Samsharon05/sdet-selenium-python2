from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import Configdata
import pytest

data = Configdata()

class TestLogin:

    @pytest.mark.sanity
    def test_login(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.login(data.login_username, data.login_password)
        assert home_page.is_inventory_visible()