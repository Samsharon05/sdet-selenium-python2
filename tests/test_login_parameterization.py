
import pytest
from pages.login_page import LoginPage  
from utils.config import Configdata   
from pages.home_page import HomePage

data = Configdata()

class TestLoginRegression:

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password", [
        (data.login_username, data.login_password),
        ("invalid_user", "invalid_pass"),
    ])
    def test_login_regression(self, driver, username, password):
        loginpage = LoginPage(driver)
        homepage = HomePage(driver) 

        loginpage.login(username, password)

        assert homepage.is_inventory_visible()  