import pytest
from pages.login_page import LoginPage  
from utils.config import Configdata   
from pages.home_page import HomePage

data = Configdata()

class TestLoginRegression:
    
    @pytest.mark.regression
    def test_login_regression(self, driver):
        loginpage = LoginPage(driver)
        homepage = HomePage(driver) 
        loginpage.login(data.login_username, data.login_password)
        assert homepage.is_inventory_visible()
        
    @pytest.mark.regression
    def test_login_with_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver) 
        login_page.login("invalid_user", "invalid_pass")
        assert "error" in home_page.is_inventory_visible()
        
    @pytest.mark.smoke
    def test_login(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.login(data.login_username, data.login_password)
        assert home_page.is_inventory_visible()