import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage

@pytest.mark.regression
def test_login_negative(driver):
    bp = BasePage(driver)
    bp.navigate("https://demoqa.com/login")
    
    bp.send_keys(LoginPage.USER_NAME, "wronguser")
    bp.send_keys(LoginPage.PASSWORD, "wrongpass")
    bp.click(LoginPage.LOGIN_BUTTON)
    
    bp.wait_for_visible(LoginPage.LOGIN_BUTTON)
    login_button = driver.find_element("xpath", LoginPage.LOGIN_BUTTON)
    assert login_button is not None
