from selenium.webdriver.common.by import By
from pages.base_pageD09 import BasePage


class HomePage(BasePage):

    INVENTORY = (By.ID, "inventory_container")

    def is_inventory_visible(self):
        return self.wait_for_element(*self.INVENTORY).is_displayed()
    