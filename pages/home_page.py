from selenium.webdriver.common.by import By

class HomePage:

    inventory_container = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver

    def is_inventory_visible(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()