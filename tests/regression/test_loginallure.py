import pytest
import allure
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Verify valid login with standard user")
@allure.description("This test verifies that a valid SauceDemo user can login successfully and land on the inventory page.")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    with allure.step("Verify user is redirected to inventory page"):
        allure.attach(
            driver.current_url,
            name="Current URL after login",
            attachment_type=allure.attachment_type.TEXT
        )

        assert "inventory.html" in driver.current_url


@pytest.mark.regression
@allure.title("Verify error message for invalid login")
@allure.description("This test verifies that SauceDemo displays a proper error message when invalid credentials are entered.")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page("https://www.saucedemo.com/")
    login_page.login("wrong_user", "wrong_password")

    with allure.step("Verify login error message is displayed"):
        error = login_page.get_error_message()

        allure.attach(
            error,
            name="Actual login error message",
            attachment_type=allure.attachment_type.TEXT
        )

        assert "Username and password do not match" in error