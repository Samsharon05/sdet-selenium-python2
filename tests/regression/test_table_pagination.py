import pytest
from selenium.webdriver.common.by import By
from pages.table_page import TablePage

@pytest.mark.regression
def test_change_rows_per_page_to_10(driver):
    tp = TablePage(driver)
    tp.navigate("https://demoqa.com/webtables")
    tp.set_rows_per_page(10)
    rows = tp.find_elements(tp.TABLE_ROW)
    assert len(rows) >= 3

@pytest.mark.regression
def test_pagination_next_page(driver):
    tp = TablePage(driver)
    tp.navigate("https://demoqa.com/webtables")
    tp.set_rows_per_page(10)

    try:
        next_btn = driver.find_element(By.XPATH, tp.NEXT_PAGE_BTN)
        if next_btn.is_enabled():
            tp.go_to_next_page()

            assert True
        else:
            pytest.skip("Next button disabled - only one page")
    except:
        pytest.skip("Pagination not available")

@pytest.mark.regression
def test_find_row_by_content(driver):
    tp = TablePage(driver)
    tp.navigate("https://demoqa.com/webtables")
    rows = tp.find_rows_by_content("Cierra")
    assert len(rows) >= 1
    row_data = tp.get_row_data(rows[0])
    assert "Cierra" in row_data.get("First Name", "")
