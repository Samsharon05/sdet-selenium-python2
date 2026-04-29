import pytest
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.employee_page import EmployeePage
from utils.config import DATA_FILE

logger = logging.getLogger(__name__)

class TestEmployeeAssertions:
    
    @pytest.mark.regression
    def test_employee_add_with_comprehensive_assertions(self, driver):
        """Add employee with verification at every step"""
        bp = BasePage(driver)
        ep = EmployeePage()
        data = bp.get_data(DATA_FILE, "new_employee")
        
        bp.navigate("https://demoqa.com/webtables")
        bp.assert_url("/webtables")
        bp.assert_title("Web Tables")
        
        expected_headers = ["First Name", "Last Name", "Age", "Email", "Salary", "Department", "Actions"]
        bp.assert_table_headers(expected_headers)
  
        initial_rows = len(bp.find_elements("//div[contains(@class,'rt-tr-group')]"))
        bp.assert_table_row_count("//div[contains(@class,'rt-table')]", 3)  # demoqa starts with 3
        
        bp.click(ep.ADD_BUTTON)
        modal_xpath = "//div[@class='modal-header' and contains(.,'Add New')]"
        bp.wait_for_visible(modal_xpath)
        bp.assert_text_visible(modal_xpath, "Add New")

        bp.send_keys("//input[@id='firstName']", data["firstName"])
        bp.send_keys("//input[@id='lastName']", data["lastName"])
        bp.send_keys("//input[@id='age']", data["age"])
        bp.send_keys("//input[@id='userEmail']", data["email"])
        bp.send_keys("//input[@id='salary']", data["salary"])
        bp.assert_input_value("//input[@id='firstName']", data["firstName"])
        bp.assert_input_value("//input[@id='lastName']", data["lastName"])
        bp.assert_input_value("//input[@id='age']", data["age"])
        bp.assert_input_value("//input[@id='userEmail']", data["email"])
        bp.assert_input_value("//input[@id='salary']", data["salary"])
        
        bp.click("//button[@id='submit']")
        bp.assert_element_visible(modal_xpath, should_be_visible=False)
        bp.assert_table_row_count("//div[contains(@class,'rt-table')]", initial_rows + 1)

        bp.assert_table_column_contains("//div[contains(@class,'rt-table')]", 0, data["firstName"])
        bp.assert_table_column_contains("//div[contains(@class,'rt-table')]", 3, data["email"])
        last_row_cell = f"//div[contains(@class,'rt-tr-group')][last()]//div[contains(@class,'rt-td')][1]"
        bp.assert_text_visible(last_row_cell, data["firstName"])
        
        logger = logging.getLogger(__name__)
        logger.info(f"Employee {data['firstName']} {data['lastName']} added and verified")
    
    @pytest.mark.regression
    def test_employee_search_verified(self, driver):
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        bp.assert_url("/webtables")
        

        bp.click(ep.ADD_BUTTON)
        bp.send_keys("//input[@id='firstName']", "SearchTest")
        bp.send_keys("//input[@id='lastName']", "User")
        bp.send_keys("//input[@id='age']", "30")
        bp.send_keys("//input[@id='userEmail']", "searchtest@example.com")
        bp.send_keys("//input[@id='salary']", "50000")
        bp.click("//button[@id='submit']")
        bp.wait_for_visible(ep.TABLE)
        search_term = "SearchTest"
        bp.send_keys(ep.SEARCH_INPUT, search_term)
        
        bp.assert_table_column_contains("//div[contains(@class,'rt-table')]", 0, search_term)
        
        all_rows = bp.find_elements("//div[contains(@class,'rt-tr-group')]")
        for row in all_rows:
            row_text = row.text.lower()
            assert search_term.lower() in row_text, (
                f"Non-matching row found in search results: {row_text}"
            )
        

        search_input_value = bp.driver.find_element(By.ID, "searchBox").get_attribute("value")
        assert search_term == search_input_value, "Search term should remain in field"
        
        logger = logging.getLogger(__name__)
        logger.info("Employee search verified")
    
    @pytest.mark.regression
    def test_employee_delete_verified(self, driver):
        """Delete employee with verification at every step"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        bp.assert_url("/webtables")
        initial_rows = len(bp.find_elements("//div[contains(@class,'rt-tr-group')]"))
        assert initial_rows > 0, "Need at least 1 row to test delete"
        
        first_delete_btn = f"(//div[contains(@class,'rt-tr-group')]//button[contains(@title,'Delete')])[1]"
        bp.click(first_delete_btn)
        

        confirm_xpath = "//div[@class='modal-header' and contains(.,'Delete')]"
        bp.wait_for_visible(confirm_xpath)
        bp.assert_text_visible(confirm_xpath, "Delete")
        

        bp.click("//button[@id='deleteRecordSubmit']")
        
        bp.wait_for_visible(ep.TABLE)
        current_rows = len(bp.find_elements("//div[contains(@class,'rt-tr-group')]"))
        assert current_rows == initial_rows - 1, (
            f"Row count should decrease by 1\nInitial: {initial_rows}\nCurrent: {current_rows}"
        )
        bp.assert_page_not_contains_text("DeletedEmployeeName")
        
        logger = logging.getLogger(__name__)
        logger.info(" Employee delete verified")
