import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class TablePage(BasePage):

    TABLE_HEADER = "//th"
    HEADER_BY_TEXT = "//th[contains(.,'{}')]"
    TABLE_ROW = "//tbody/tr"
    TABLE_CELL = "//td"
    PREV_PAGE_BTN = "//button[contains(.,'Previous')]"
    NEXT_PAGE_BTN = "//button[contains(.,'Next')]"
    PAGE_NUMBER_BTN = "//button[text()='{}']"
    ROWS_PER_PAGE_SELECT = "//select[@class='form-control']"
    ACTIVE_PAGE_BTN = "//button[contains(@class,'active')]"
    TABLE_CONTAINER = "//table"
    NO_ROWS = "//div[contains(text(),'No rows found')]"

    def get_headers(self):

        self.wait_for_visible(self.TABLE_HEADER)
        headers = self.find_elements(self.TABLE_HEADER)
        return [h.text.strip() for h in headers if h.text.strip()]

    def click_header_to_sort(self, header_text):

        locator = self.HEADER_BY_TEXT.format(header_text)
        logger.info(f"Clicking header to sort: {header_text}")
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.driver.execute_script("""
            arguments[0].click();
            arguments[0].dispatchEvent(new MouseEvent('mousedown', {bubbles: true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseup', {bubbles: true}));
            arguments[0].dispatchEvent(new MouseEvent('click', {bubbles: true}));
        """, element)

        self.wait_for_visible(self.TABLE_CONTAINER)
        logger.info(f"Clicked header: {header_text}")

    def get_column_values(self, header_text):
        """Returns list of values in specified column"""
        headers = self.get_headers()
        if header_text not in headers:
            raise ValueError(f"Header '{header_text}' not found. Available headers: {headers}")
        col_index = headers.index(header_text)
        rows = self.find_elements(self.TABLE_ROW)

        js_row_count = self.driver.execute_script("return document.querySelectorAll('table tbody tr').length")
        logger.info(f"Found {len(rows)} rows (JS says {js_row_count}), looking for column {col_index}")
        values = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if col_index < len(cells):
                values.append(cells[col_index].text.strip())
        logger.info(f"Got {len(values)} values from column '{header_text}': {values}")
        return values

    def is_column_sorted(self, header_text, ascending=True):

        values = self.get_column_values(header_text)
        processed = []
        for val in values:
            try:
                processed.append(float(val))
            except ValueError:
                processed.append(val.lower())
        expected = sorted(processed, reverse=not ascending)
        is_sorted = processed == expected
        logger.info(f"Column '{header_text}' sorted ascending={ascending}: {is_sorted}. Processed: {processed}, Expected: {expected}")
        return is_sorted

    def find_rows_by_content(self, content):
        rows = self.find_elements(self.TABLE_ROW)
        matching_rows = []
        content_lower = content.lower()
        for row in rows:
            if content_lower in row.text.lower():
                matching_rows.append(row)
        logger.info(f"Found {len(matching_rows)} rows containing '{content}'")
        return matching_rows

    def get_row_data(self, row_element):
        headers = self.get_headers()
        cells = row_element.find_elements(By.TAG_NAME, "td")
        row_data = {}
        for i, header in enumerate(headers):
            if i < len(cells):
                row_data[header] = cells[i].text.strip()
        return row_data

    def get_all_table_data(self):

        rows = self.find_elements(self.TABLE_ROW)
        return [self.get_row_data(row) for row in rows]

    def set_rows_per_page(self, count):

        valid_counts = [10, 20, 30, 40, 50]
        if count not in valid_counts:
            raise ValueError(f"Invalid rows per page: {count}. Valid options: {valid_counts}")
        select_elem = self.wait.until(EC.presence_of_element_located((By.XPATH, self.ROWS_PER_PAGE_SELECT)))

        self.driver.execute_script(f"""
            var select = arguments[0];
            for (var i = 0; i < select.options.length; i++) {{
                if (select.options[i].text.includes('Show {count}')) {{
                    select.selectedIndex = i;
                    break;
                }}
            }}
            select.dispatchEvent(new Event('change'));
        """, select_elem)
        self.wait_for_visible(self.TABLE_CONTAINER)
        logger.info(f"Set rows per page to {count}")

    def go_to_next_page(self):

        logger.info("Navigating to next page")
        self.click(self.NEXT_PAGE_BTN)
        self.wait_for_visible(self.TABLE_CONTAINER)

    def go_to_prev_page(self):

        logger.info("Navigating to previous page")
        self.click(self.PREV_PAGE_BTN)
        self.wait_for_visible(self.TABLE_CONTAINER)

    def go_to_page(self, page_num):

        logger.info(f"Navigating to page {page_num}")
        locator = self.PAGE_NUMBER_BTN.format(page_num)
        self.click(locator)
        self.wait_for_visible(self.TABLE_CONTAINER)

    def get_current_page(self):

        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ACTIVE_PAGE_BTN)))
        return int(elem.text.strip())

    def verify_row_count(self, expected_count):

        rows = self.find_elements(self.TABLE_ROW)
        actual_count = len(rows)
        if actual_count == expected_count:
            logger.info(f"Row count verified: {actual_count}")
            return True
        logger.warning(f"Row count mismatch: expected {expected_count}, got {actual_count}")
        return False
