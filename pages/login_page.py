from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    username = (By.XPATH, '//input[@placeholder="Username"]')
    password = (By.XPATH, '//input[@placeholder="Password"]')
    loginbutton = (By.XPATH, '//input[@id="login-button"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.loginbutton)).click()