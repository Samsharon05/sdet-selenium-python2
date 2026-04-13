import pytest
from pages.login_page import LoginPage  
from utils.config import Configdata   
from pages.home_page import HomePage

data = Configdata()

class TestLoginRegression:
    
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_successful_user(self, driver): 
        login_page = LoginPage(driver)
        home_page = HomePage(driver) 
        
        login_page.login(data.login_username, data.login_password)
        
        assert home_page.is_inventory_visible() is True
        
    @pytest.mark.regression
    def test_login_with_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        
        login_page.login("invalid_user", "invalid_pass")
        
        assert "error" in login_page.get_error_message().lower()