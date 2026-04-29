import pytest
import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class TestFormAssertions:
    
    @pytest.mark.regression
    def test_form_validation_assertions(self, driver):
        bp = BasePage(driver)
        
        bp.navigate("https://demoqa.com/text-box")
        bp.assert_url("/text-box")
        

        bp.click("//button[@id='submit']")


        bp.assert_page_not_contains_text("Name:")
        test_name = "John Doe"
        test_email = "john.doe@example.com"
        
        bp.send_keys("//input[@id='userName']", test_name)
        bp.send_keys("//input[@id='userEmail']", test_email)
        bp.send_keys("//textarea[@id='currentAddress']", "123 Main St")
        bp.send_keys("//textarea[@id='permanentAddress']", "456 Oak Ave")
        
        bp.assert_input_value("//input[@id='userName']", test_name)
        bp.assert_input_value("//input[@id='userEmail']", test_email)
        
        bp.click("//button[@id='submit']")
        

        bp.wait_for_visible("//div[@class='mt-3 row']")
        output_xpath = "//div[@class='mt-3 row']/div/p"
        bp.assert_text_visible(output_xpath, test_name)
        bp.assert_text_visible(output_xpath, test_email)
        
        logger.info("Form validation assertions passed")
    
    @pytest.mark.regression
    def test_dropdown_and_checkbox_assertions(self, driver):
        bp = BasePage(driver)
        
        bp.navigate("https://demoqa.com/checkbox")
        bp.assert_url("/checkbox")
        

        bp.click("//button[@title='Expand all']")
        

        expand_btn = driver.find_element(By.XPATH, "//button[@title='Expand all']")
        assert "Collapse" in expand_btn.get_attribute("title"), "All should be expanded"
        
        bp.click("//span[@class='rct-checkbox']")
        

        checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
        is_checked = checkbox.find_element(By.XPATH, ".//input").is_selected()
        assert is_checked, "Checkbox should be checked"
        

        result_xpath = "//div[@id='result']//span[@class='text-success']"
        bp.wait_for_visible(result_xpath)
        result_text = bp.get_text(result_xpath)
        assert "home" in result_text.lower(), f"Result should include 'home', got: {result_text}"
        
        logger.info("Dropdown/checkbox assertions passed")
