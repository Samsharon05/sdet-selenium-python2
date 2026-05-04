import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, ButtonsPage, RadioButtonPage
from utils.test_data_manager import data_manager


class TestElements:

    
    @pytest.mark.smoke
    @pytest.mark.elements
    def test_text_box_submit(self, driver):

        bp = BasePage(driver)
        tp = TextBoxPage()
        
        bp.navigate("https://demoqa.com/text-box")
        bp.wait_for_visible(tp.FULL_NAME)
        
        name = data_manager.get_unique_username()
        bp.send_keys(tp.FULL_NAME, name)
        bp.send_keys(tp.EMAIL, data_manager.get_unique_email("test"))
        bp.send_keys(tp.CURRENT_ADDRESS, "123 Main St")
        bp.send_keys(tp.PERMANENT_ADDRESS, "456 Oak Ave")
        bp.click(tp.SUBMIT)
        

        bp.wait_for_visible(tp.OUTPUT)
        output = bp.get_text(tp.OUTPUT)
        assert name in output
    
    @pytest.mark.regression
    @pytest.mark.elements
    def test_button_double_click(self, driver):

        bp = BasePage(driver)
        bp.navigate("https://demoqa.com/buttons")
        
        action = ActionChains(bp.driver)
        btn = bp.wait.until(EC.element_to_be_clickable((By.ID, 'doubleClickBtn')))
        action.move_to_element(btn).perform()
        action.double_click(btn).perform()
        
        bp.wait_for_visible(ButtonsPage.DOUBLE_CLICK_MSG)
        msg = bp.get_text(ButtonsPage.DOUBLE_CLICK_MSG).lower()
        assert "double click" in msg
    
    @pytest.mark.regression
    @pytest.mark.elements
    def test_button_right_click(self, driver):

        bp = BasePage(driver)
        bp.navigate("https://demoqa.com/buttons")
        
        action = ActionChains(bp.driver)
        btn = bp.wait.until(EC.element_to_be_clickable((By.ID, 'rightClickBtn')))
        action.move_to_element(btn).perform()
        action.context_click(btn).perform()
        
        bp.wait_for_visible(ButtonsPage.RIGHT_CLICK_MSG)
        msg = bp.get_text(ButtonsPage.RIGHT_CLICK_MSG).lower()
        assert "right click" in msg
    
    @pytest.mark.regression
    @pytest.mark.elements
    def test_button_dynamic_click(self, driver):

        bp = BasePage(driver)
        bp.navigate("https://demoqa.com/buttons")
        bp.wait_for_visible(ButtonsPage.CLICK_ME_BTN)
        bp.click(ButtonsPage.CLICK_ME_BTN)
        
        bp.wait_for_visible(ButtonsPage.CLICK_ME_MSG)
        msg = bp.get_text(ButtonsPage.CLICK_ME_MSG).lower()
        assert "dynamic click" in msg
    
    @pytest.mark.smoke
    @pytest.mark.elements
    def test_radio_button_select(self, driver):

        bp = BasePage(driver)
        bp.navigate("https://demoqa.com/radio-button")
        bp.wait_for_visible(RadioButtonPage.YES_RADIO)
        
        bp.click(RadioButtonPage.YES_RADIO)
        bp.wait_for_visible(RadioButtonPage.RADIO_RESULT)
        result = bp.get_text(RadioButtonPage.RADIO_RESULT).lower()
        assert "yes" in result