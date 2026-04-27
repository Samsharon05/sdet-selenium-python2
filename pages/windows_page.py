from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WindowsPage(BasePage):

    NEW_TAB_BTN = (By.ID, "tabButton")
    HEADING = (By.ID, "sampleHeading")

    def open_new_tab(self):
        self.click(*self.NEW_TAB_BTN)

    def switch_to_new_tab(self):
        parent = self.driver.current_window_handle
        handles = self.driver.window_handles

        for handle in handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

        return parent

    def get_heading_text(self):
        return self.get_text(*self.HEADING)

    def close_tab_and_return(self, parent):
        self.driver.close()
        self.driver.switch_to.window(parent)