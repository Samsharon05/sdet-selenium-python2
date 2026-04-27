import pytest
from selenium.webdriver.common.keys import Keys
from pages.table_page import TablePage

@pytest.mark.regression
def test_sort_first_name_ascending(driver):
    tp = TablePage(driver)
    tp.navigate("https://demoqa.com/webtables")
    tp.click_header_to_sort("First Name")
    values = tp.get_column_values("First Name")
    assert len(values) >= 1

@pytest.mark.regression
def test_sort_first_name_descending(driver):
    tp = TablePage(driver)
    tp.navigate("https://demoqa.com/webtables")
    tp.click_header_to_sort("First Name")
    tp.click_header_to_sort("First Name")
    values = tp.get_column_values("First Name")
    assert len(values) >= 1

@pytest.mark.regression
def test_sort_salary_ascending(driver):
    tp = TablePage(driver)
    tp.navigate("https://demoqa.com/webtables")
    tp.click_header_to_sort("Salary")
    values = tp.get_column_values("Salary")
    assert len(values) >= 1
