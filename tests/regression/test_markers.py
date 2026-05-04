import pytest
from pages.base_page import BasePage
from pages.makers_page import DemoQAPage


class TestDemoQAMarkers:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_text_box_page_loads(self, driver):
        bp = BasePage(driver)
        demoqa = DemoQAPage(driver)

        bp.navigate(demoqa.TEXT_BOX_URL)

        bp.assert_url("/text-box")
        bp.assert_text_visible(demoqa.HEADING, "Text Box")

    @pytest.mark.regression
    @pytest.mark.critical
    def test_text_box_submit_valid_data(self, driver):
        bp = BasePage(driver)
        demoqa = DemoQAPage(driver)

        bp.navigate(demoqa.TEXT_BOX_URL)

        name = "John Doe"
        email = "john.doe@example.com"
        current_address = "123 Main Street"
        permanent_address = "456 Oak Avenue"

        bp.send_keys(demoqa.USER_NAME, name)
        bp.send_keys(demoqa.USER_EMAIL, email)
        bp.send_keys(demoqa.CURRENT_ADDRESS, current_address)
        bp.send_keys(demoqa.PERMANENT_ADDRESS, permanent_address)

        bp.click(demoqa.SUBMIT_BUTTON)

        bp.wait_for_visible(demoqa.OUTPUT)
        bp.assert_text_visible(demoqa.OUTPUT, name)
        bp.assert_text_visible(demoqa.OUTPUT, email)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_checkbox_select_home(self, driver):
        bp = BasePage(driver)
        demoqa = DemoQAPage(driver)

        bp.navigate(demoqa.CHECKBOX_URL)

        bp.click(demoqa.CHECKBOX)

        bp.wait_for_visible(demoqa.CHECKBOX_RESULT)
        bp.assert_text_visible(demoqa.CHECKBOX_RESULT, "home")

    @pytest.mark.regression
    def test_radio_button_yes_selection(self, driver):
        bp = BasePage(driver)
        demoqa = DemoQAPage(driver)

        bp.navigate(demoqa.RADIO_URL)

        bp.click(demoqa.YES_RADIO)

        bp.assert_text_visible(demoqa.RADIO_RESULT, "Yes")