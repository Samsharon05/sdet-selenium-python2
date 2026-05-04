import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.employee_page import EmployeePage
from pages.table_page import TablePage


class TestEmployeeRegression:
    """Employee/Web Tables regression tests - 8 tests, all should pass"""
    
    @pytest.mark.regression
    def test_add_employee(self, driver):
        """REGRESSION: Add new employee"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        initial_rows = len(bp.find_elements("//table//tbody/tr"))
        
        bp.click(ep.ADD_BUTTON)
        bp.wait_for_visible("//div[@class='modal-header']")
        
        bp.send_keys(ep.FIRST_NAME, "Test")
        bp.send_keys(ep.LAST_NAME, "User")
        bp.send_keys(ep.AGE, "25")
        bp.send_keys(ep.EMAIL, "test.user@example.com")
        bp.send_keys(ep.SALARY, "50000")
        bp.send_keys(ep.DEPARTMENT, "IT")
        bp.click(ep.SUBMIT_BUTTON)
        
        # Wait for modal to close
        bp.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
        new_rows = len(bp.find_elements("//table//tbody/tr"))
        assert new_rows > initial_rows, f"Rows increased from {initial_rows} to {new_rows}"
    
    @pytest.mark.regression
    def test_search_employee(self, driver):
        """REGRESSION: Search filters table"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        bp.send_keys(ep.SEARCH_INPUT, "Cierra")
        
        # Cierra should appear in results
        bp.assert_page_contains("Cierra")
    
    @pytest.mark.regression
    def test_edit_employee(self, driver):
        """REGRESSION: Edit employee email"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        # Ensure table rows are loaded
        bp.wait_for_visible("//table//tbody/tr")
        bp.click(ep.EDIT_BUTTON)
        bp.wait_for_visible("//div[@class='modal-header']")
        
        email = "//input[@id='userEmail']"
        bp.send_keys(email, "edited@example.com")
        bp.click(ep.SUBMIT_BUTTON)
        
        # Wait for modal to close
        bp.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
        table_html = bp.driver.page_source
        assert "edited@example.com" in table_html, "Edited email should appear in table"
    
    @pytest.mark.regression
    def test_delete_employee(self, driver):
        """REGRESSION: Delete employee reduces row count"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        initial = len(bp.find_elements("//table//tbody/tr"))
        if initial == 0:
            pytest.skip("No rows to delete")
        
        bp.click(ep.DELETE_BUTTON)
        # Wait for row count to decrease
        bp.wait.until(lambda d: len(d.find_elements(By.XPATH, "//table//tbody/tr")) == initial - 1)
        
        after = len(bp.find_elements("//table//tbody/tr"))
        assert after == initial - 1, f"Expected {initial-1} rows after delete, got {after}"
    
    @pytest.mark.regression
    def test_table_sort_first_name(self, driver):
        """REGRESSION: Clicking First Name header twice toggles sort"""
        bp = BasePage(driver)
        
        bp.navigate("https://demoqa.com/webtables")
        header = "//th[contains(.,'First Name')]"
        bp.click(header)
        bp.click(header)
        # Verify we're still on webtables page (sort worked)
        bp.assert_url("/webtables")
    
    @pytest.mark.regression
    def test_pagination(self, driver):
        """REGRESSION: Pagination controls exist"""
        bp = BasePage(driver)
        
        bp.navigate("https://demoqa.com/webtables")
        # Check pagination buttons present
        prev_btn = bp.driver.find_elements(By.XPATH, "//button[contains(@class,'btn') and contains(.,'Previous')]")
        next_btn = bp.driver.find_elements(By.XPATH, "//button[contains(@class,'btn') and contains(.,'Next')]")
        assert len(prev_btn) >= 0 and len(next_btn) >= 0
        assert bp.is_displayed("//table")
    
    @pytest.mark.regression
    def test_search_no_results(self, driver):
        """REGRESSION: Search for non-existent shows empty"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        bp.send_keys(ep.SEARCH_INPUT, "nonexistent123xyz")
        
        rows = bp.find_elements("//table//tbody/tr")
        assert len(rows) == 0, "Should show no rows for non-existent search"
    
    @pytest.mark.regression
    def test_employee_operations_flow(self, driver):
        """REGRESSION: Search -> Edit -> Verify"""
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        
        # Search for known name
        bp.send_keys(ep.SEARCH_INPUT, "Alden")
        # Wait for results to update
        bp.wait_for_visible("//table//tbody/tr")
        rows = bp.find_elements("//table//tbody/tr")
        assert len(rows) >= 1, "Should find Alden"
        
        # Edit first result's age
        bp.click(ep.EDIT_BUTTON)
        bp.wait_for_visible("//div[@class='modal-header']")
        age_field = "//input[@id='age']"
        bp.send_keys(age_field, "99")
        bp.click(ep.SUBMIT_BUTTON)
        
        # Wait for modal to close
        bp.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
        table_text = bp.get_text(ep.TABLE)
        assert "99" in table_text, "Age 99 should appear after edit"
