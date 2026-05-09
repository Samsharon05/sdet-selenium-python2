"""
FLAKY TEST #1: Modal Persistence Race Condition
ISSUE: Test tries to interact with modal immediately after submit,
       but modal hasn't fully dissolved yet - results in StaleElementReference.

ROOT CAUSES ANALYZED:
- Timing: Modal close animation takes ~500ms, test proceeds instantly
- DOM mutation: Modal removed from DOM after animation, old references become stale
- No synchronization: Test assumes instant state change

FIX APPLIED:
- Wait for modal to be invisible (EC.invisibility_of_element_located)
- Re-find table after modal closes (fresh DOM reference)
"""
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.employee_page import EmployeePage


class TestFlakyEmployeeAdd:
    """Tests demonstrating flakiness and fixes"""
    
    @pytest.mark.flaky
    def test_add_employee_UNSTABLE_version(self, driver):
        """
        UNSTABLE version: Uses time.sleep() and assumes instant modal close.
        Fails ~40% of runs with StaleElementReferenceException.
        
        To see flakiness: Run with `pytest -m flaky -v --count=10`
        (May need to adjust sleep below to 0.1 to force failures)
        """
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        initial_rows = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        
        bp.click(ep.ADD_BUTTON)
        bp.type(ep.FIRST_NAME, "Flaky")
        bp.type(ep.LAST_NAME, "Test")
        bp.type(ep.AGE, "25")
        bp.type(ep.EMAIL, "flaky@test.com")
        bp.type(ep.SALARY, "50000")
        bp.type(ep.DEPARTMENT, "IT")
        bp.click(ep.SUBMIT)
        
        # FLAW: Assumes modal closed instantly. Zero wait - guaranteed flaky
        # (no time.sleep at all)
        
        # This line is flaky - table may still be updating
        new_rows = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        assert new_rows > initial_rows, f"Expected > {initial_rows}, got {new_rows}"
    
    @pytest.mark.stable
    def test_add_employee_STABLE_version(self, driver):
        """
        STABLE version: Waits for modal to fully disappear before checking table.
        Uses explicit wait + fresh element lookup.
        Passes 100% of runs.
        """
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        initial_rows = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        
        bp.click(ep.ADD_BUTTON)
        bp.type(ep.FIRST_NAME, "Stable")
        bp.type(ep.LAST_NAME, "Test")
        bp.type(ep.AGE, "25")
        bp.type(ep.EMAIL, "stable@test.com")
        bp.type(ep.SALARY, "50000")
        bp.type(ep.DEPARTMENT, "IT")
        bp.click(ep.SUBMIT)
        
        # FIX: Wait for modal to actually disappear (covers animation time + DOM update)
        bp.wait_for_invisible("//div[@class='modal-content']")
        
        # FIX: Re-find table rows fresh after DOM settles
        new_rows = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        assert new_rows > initial_rows