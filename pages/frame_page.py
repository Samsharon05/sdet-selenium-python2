from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FramesPage(BasePage):

    FRAME1 = "frame1"
    HEADING = (By.ID, "sampleHeading")

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.FRAME1)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def get_heading_text(self):
        return self.get_text(*self.HEADING)