import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWaits:

    @pytest.mark.regression
    def test_dynamic_loading_wait(self, driver):
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        driver.find_element(By.TAG_NAME, "button").click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        assert "Hello World!" in element.text