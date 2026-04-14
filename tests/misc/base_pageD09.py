from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    def type(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def click(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()
        
    def type(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def click(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()