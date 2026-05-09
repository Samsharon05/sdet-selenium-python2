"""
FLAKY TEST #2: Table Row Count After Delete - Element Stale
ISSUE: After clicking delete, the row count drops but test tries to
       count rows immediately, sometimes getting stale references or wrong count.

ROOT CAUSES ANALYZED:
- Timing: Row removal animation (~300-500ms) before DOM updates
- Index shift: When row 1 is deleted, row 2 becomes new row 1, but
  find_elements returns snapshot that may include ghost references
- No wait: Test assumes instant deletion

FIX APPLIED:
- Wait for row count to actually decrease using explicit condition
- Avoid holding stale references; fresh find_elements call after wait
- Lambda-based wait that polls until count decreases
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.employee_page import EmployeePage


class TestFlakyEmployeeDelete:
    """Tests demonstrating flakiness and fixes for delete operation"""
    
    @pytest.mark.flaky
    def test_delete_employee_UNSTABLE_version(self, driver):
        """
        UNSTABLE version: Assumes instant row removal.
        Fails ~30% with AssertionError (count not decreased yet).
        
        To see flakiness: Run with `pytest -m flaky -v --count=10`
        (May need to reduce sleep to 0.3 to force failures)
        """
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        initial = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        if initial == 0:
            pytest.skip("No rows to delete")
        
        bp.click(ep.DELETE_BUTTON)
        
        # FLAW: No wait for deletion to complete (zero sleep - guaranteed flaky)
        # (no time.sleep at all)
        
        after = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        assert after == initial - 1, f"Expected {initial-1}, got {after}"
    
    @pytest.mark.stable
    def test_delete_employee_STABLE_version(self, driver):
        """
        STABLE version: Explicitly waits for row count to decrease.
        Uses lambda condition that polls until DOM updates.
        Passes 100% of runs.
        """
        bp = BasePage(driver)
        ep = EmployeePage()
        
        bp.navigate("https://demoqa.com/webtables")
        initial = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        if initial == 0:
            pytest.skip("No rows to delete")
        
        bp.click(ep.DELETE_BUTTON)
        
        # FIX: Wait until row count actually decreases (polls every 0.5s up to 10s)
        bp.wait.until(
            lambda d: len(d.find_elements(By.XPATH, ep.TABLE_ROWS)) == initial - 1
        )
        
        # Fresh lookup after wait confirms deletion
        after = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
        assert after == initial - 1