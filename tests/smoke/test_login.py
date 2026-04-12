from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.loginpage import LoginPage
from utils.config import Configdata

data = Configdata()

class TestLoginPage:
    def test_login(self, driver):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.visibility_of_element_located(LoginPage.username)).send_keys(data.login_username)
        wait.until(EC.visibility_of_element_located(LoginPage.password)).send_keys(data.login_password)
        wait.until(EC.element_to_be_clickable(LoginPage.loginbutton)).click()
        
        