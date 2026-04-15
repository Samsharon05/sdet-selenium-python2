from selenium.webdriver.common.by import By
from pages.base_pageD10 import BasePage

class homePage(BasePage):
    
    INVENTORY_ITEM = (By.ID, "inventory_container")
    
    def is_inventory_visible(self):
        return self.find_element(*self.INVENTORY_ITEM).is_displayed()
    