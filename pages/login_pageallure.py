import allure
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_box = (By.ID, "user-name")
    password_box = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open_login_page(self, url):
        with allure.step("Open SauceDemo login page"):
            self.driver.get(url)

    def enter_username(self, username):
        with allure.step("Enter username"):
            self.driver.find_element(*self.username_box).send_keys(username)

    def enter_password(self, password):
        with allure.step("Enter password"):
            self.driver.find_element(*self.password_box).send_keys(password)

    def click_login(self):
        with allure.step("Click login button"):
            self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        with allure.step("Perform login"):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

    def get_error_message(self):
        with allure.step("Get login error message"):
            return self.driver.find_element(*self.error_message).text