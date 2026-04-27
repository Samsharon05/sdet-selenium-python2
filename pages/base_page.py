from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
    def click(self, by, value):
        element=self.wait_for_element(by, value)
        element.click()
    def send_keys(self, by, value, keys):
        element=self.wait_for_element(by, value)
        element.send_keys(keys)
    def wait_for_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))
    def type_text(self,by, value, text):
        element=self.wait_for_element(by,value)
        element.clear()
        element.send_keys(text)
    def wait_for_alert(self, timeout=10):
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
    
    
        