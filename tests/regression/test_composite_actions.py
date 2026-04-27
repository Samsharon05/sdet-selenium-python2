import pytest
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.regression
def test_composite_action_keyboard(driver):
    
    bp = BasePage(driver)
    bp.navigate("https://demoqa.com/text-box")
    

    bp.wait_for_visible("//input[@id='userName']")
    bp.send_keys("//input[@id='userName']", "John Doe")
    

    name_value = bp.get_value("//input[@id='userName']")
    assert "John" in name_value

@pytest.mark.regression
def test_key_down_up(driver):
    bp = BasePage(driver)
    bp.navigate("https://demoqa.com/select-menu")
    

    bp.click("//select[@id='oldSelectMenu']")
    bp.key_down_up(Keys.ARROW_DOWN)
    bp.key_down_up(Keys.ARROW_DOWN)

    assert True
