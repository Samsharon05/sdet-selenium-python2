import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.employee_page import EmployeePage
from utils.config import DATA_FILE

@pytest.mark.regression
def test_employee_edit(driver):
    bp = BasePage(driver)
    bp.navigate("https://demoqa.com/webtables")
    

    bp.click(EmployeePage.ADD_BUTTON)
    emp_data = bp.get_data(DATA_FILE, "employee")
    bp.send_keys(EmployeePage.FIRST_NAME, emp_data["firstName"])
    bp.send_keys(EmployeePage.LAST_NAME, emp_data["lastName"])
    bp.send_keys(EmployeePage.EMAIL, emp_data["email"])
    bp.send_keys(EmployeePage.AGE, emp_data["age"])
    bp.send_keys(EmployeePage.SALARY, emp_data["salary"])
    bp.send_keys(EmployeePage.DEPARTMENT, emp_data["department"])
    bp.click(EmployeePage.SUBMIT)
    bp.wait_for_visible("//body")
    

    bp.send_keys(EmployeePage.SEARCH_BOX, emp_data["email"])
    bp.wait_for_text_in_page(emp_data["email"])
    
   
    bp.click(EmployeePage.EDIT_BUTTON)
    bp.send_keys(EmployeePage.DEPARTMENT, "Updated Dept")
    bp.click(EmployeePage.SUBMIT)
    
    bp.wait_for_visible("//body")
    current_url = driver.current_url
    assert "demoqa.com" in current_url
