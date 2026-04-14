from selenium.webdriver.common.by import By
from pages.base_pageD09 import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.type(*self.USERNAME, username)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def get_error_message(self):  
        return self.wait_for_element(*self.ERROR_MSG).text