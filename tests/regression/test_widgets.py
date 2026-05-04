import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.widgets_page import DatePickerPage, SliderPage
from utils.test_data_manager import data_manager
from selenium.webdriver.common.action_chains import ActionChains


class TestWidgets:

    
    @pytest.mark.smoke
    @pytest.mark.widgets
    def test_date_picker_select(self, driver):

        bp = BasePage(driver)
        dp = DatePickerPage()
        
        bp.navigate("https://demoqa.com/date-picker")
        bp.wait_for_visible(dp.DATE_INPUT)
        
        date_input = bp.driver.find_element(By.XPATH, dp.DATE_INPUT)
        date_input.clear()
        date_input.send_keys("15/03/1995")
        
        value = date_input.get_attribute("value")
        assert "1995" in value or "03" in value
    
    @pytest.mark.regression
    @pytest.mark.widgets
    def test_slider_move(self, driver):

        bp = BasePage(driver)
        sp = SliderPage()
        
        bp.navigate("https://demoqa.com/slider")
        bp.wait_for_visible(sp.SLIDER)
        
        slider = bp.driver.find_element(By.XPATH, sp.SLIDER)
        value_elem = bp.driver.find_element(By.XPATH, sp.SLIDER_VALUE)
        
        initial = value_elem.get_attribute("value")
        
        actions = ActionChains(bp.driver)
        actions.move_to_element(slider).perform()
        actions.click_and_hold(slider).move_by_offset(30, 0).release().perform()
        

        import time
        time.sleep(0.5)
        new_val = value_elem.get_attribute("value")
        assert new_val != initial, f"Slider should have changed from {initial} to {new_val}"
    
    @pytest.mark.regression
    @pytest.mark.widgets
    def test_date_picker_with_unique_data(self, driver):

        bp = BasePage(driver)
        dp = DatePickerPage()
        
        bp.navigate("https://demoqa.com/date-picker")
        bp.wait_for_visible(dp.DATE_INPUT)
        
        date_str = f"15/{data_manager.get_unique_username()[-6:-3]}/2000"
        date_input = bp.driver.find_element(By.XPATH, dp.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date_str)
        
        value = date_input.get_attribute("value")
        assert "2000" in value