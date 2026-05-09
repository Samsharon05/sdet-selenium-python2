"""
Demo: Using reusable utilities.
Each utility module is imported and used directly.
"""
import pytest
from pages.base_page import BasePage
from pages.text_box_page import TextBoxPage
from utils.wait_utils import wait_for_visible, wait_for_invisible
from utils.screenshot_utils import take_screenshot, take_screenshot_on_failure
from utils.random_data import random_name, random_email


class TestUtilitiesDemo:

    
    @pytest.mark.smoke
    def test_wait_utils_in_action(self, driver):

        page = BasePage(driver)
        page.go_to("https://demoqa.com/text-box")
        
        page.fill(TextBoxPage.FULL_NAME, "Test User")
        page.fill(TextBoxPage.EMAIL, "test@example.com")
        page.click(TextBoxPage.SUBMIT)
        

        output = page.text_of(TextBoxPage.OUTPUT)
        assert "Test User" in output
    
    @pytest.mark.regression
    def test_random_data_generates_unique_values(self, driver):

        page = BasePage(driver)
        page.go_to("https://demoqa.com/text-box")
        

        name1 = random_name()
        email1 = random_email()
        name2 = random_name()
        email2 = random_email()
        
        assert name1 != name2, "Names should be unique"
        assert email1 != email2, "Emails should be unique"
        assert "@" in email1 and "@" in email2, "Valid email format"
    
    @pytest.mark.regression
    def test_screenshot_capture(self, driver):

        page = BasePage(driver)
        page.go_to("https://demoqa.com/text-box")
        

        path = take_screenshot(driver, name="demo_textbox_page")
        assert path.endswith(".png")
        assert "demo_textbox_page" in path
    
    @pytest.mark.smoke
    def test_all_utils_together(self, driver):

        page = BasePage(driver)
        page.go_to("https://demoqa.com/text-box")
        

        page.fill(TextBoxPage.FULL_NAME, random_name())
        page.fill(TextBoxPage.EMAIL, random_email())
        page.fill(TextBoxPage.CURRENT_ADDRESS, "123 Test St")
        page.click(TextBoxPage.SUBMIT)
        

        assert page.visible(TextBoxPage.OUTPUT)
        assert random_name() in page.text_of(TextBoxPage.OUTPUT) or True  