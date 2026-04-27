from selenium import webdriver
from pages.alerts_page import AlertsPage
import pytest
import os


class TestAlerts:

    @pytest.mark.regression
    def test_simple_alert(self, driver):
        driver.get("https://demoqa.com/alerts")
        alerts = AlertsPage(driver)
        alerts.click_timer_alert()
        alerts.accept_alert()
        
    @pytest.mark.regression
    def test_timer_alert(self, driver):
        driver.get("https://demoqa.com/alerts")
        alerts = AlertsPage(driver)
        alerts.click_timer_alert()
        alerts.accept_alert()
    
    @pytest.mark.regression
    def test_send_text(self, driver):
        driver.get("https://demoqa.com/alerts")
        alerts = AlertsPage(driver)
        alerts.click_prompt_alert()
        text = os.getenv("CARD_NUMBER", "sam")
        alerts.send_text_to_alert(text)   
        
    @pytest.mark.regression
    def test_dismiss_prompt_alert(self, driver):
        driver.get("https://demoqa.com/alerts")
        alerts = AlertsPage(driver)
        alerts.click_prompt_alert()
        alerts.dismiss_alert()