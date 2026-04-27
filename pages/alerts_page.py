from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AlertsPage(BasePage):

    ALERT_BTN = (By.ID, "alertButton")
    CONFIRM_BTN = (By.ID, "confirmButton")
    PROMPT_BTN = (By.ID, "promtButton")

    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def click_simple_alert(self):
        self.click(*self.ALERT_BTN)

    def click_confirm_alert(self):
        self.click(*self.CONFIRM_BTN)

    def click_prompt_alert(self):
        self.click(*self.PROMPT_BTN)

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def send_text_to_alert(self, text):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def get_confirm_result(self):
        return self.get_text(*self.CONFIRM_RESULT)

    def get_prompt_result(self):
        return self.get_text(*self.PROMPT_RESULT)