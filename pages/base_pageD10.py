from asyncio import log

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.loggersD10 import get_logger


log = get_logger()
class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, by, value,):
        return self.driver.find_element(by, value)
    
    def wait_for_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))
    
    def click(self, by, value):
        log.info(f"Clicking element: {value}")
        element = self.wait_for_element(by, value)
        element.click()
        
    def type(self, by, value, text):
        log.info(f"Typing text: {text}")
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)
    
   

    
    
    
        
    
