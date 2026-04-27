from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.loggers import get_logger

log = get_logger()

class LoginPage(BasePage):
    
    USERNAME = (By.ID, "user-name")   
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSSG=(By.CSS_SELECTOR, "h3[data-test='error']")
    
    def login(self, username, password):
        log.info("Entering username")
        self.type(*self.USERNAME, username)

        log.info("Entering password")
        self.type(*self.PASSWORD, password)

        log.info("Clicking login button")
        self.click(*self.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.find_element(*self.ERROR_MSSG).text
    
  
    
    
    
    