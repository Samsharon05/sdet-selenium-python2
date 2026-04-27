from pages.text_page import TextPage
import pytest
import os
from dotenv import load_dotenv


load_dotenv()


class TestTextForm:

    URL = "https://demoqa.com/automation-practice-form"

  
    @pytest.mark.regression
    def test_submit_form_success(self, driver):
        driver.get(self.URL)

        form = TextPage(driver)

        form.enter_first_name(os.getenv("FIRSTNAME"))
        form.enter_last_name(os.getenv("LASTNAME"))
        form.enter_email(os.getenv("EMAIL"))
        form.select_gender()
        form.enter_mobile(os.getenv("ADDRESS_PHONE"))

        form.enter_dob()
        form.enter_subject("Maths")
        form.select_hobbies()

        form.enter_address(os.getenv("ADDRESS_LINE1"))
        form.select_state("NCR")
        form.select_city("Delhi")

        form.click_submit()

        assert "Thanks for submitting the form" in driver.page_source



    @pytest.mark.regression
    def test_submit_without_required_fields(self, driver):
        driver.get(self.URL)

        form = TextPage(driver)
        form.click_submit()

        assert "Thanks for submitting the form" not in driver.page_source



    @pytest.mark.regression
    def test_invalid_email(self, driver):
        driver.get(self.URL)

        form = TextPage(driver)

        form.enter_first_name(os.getenv("FIRSTNAME"))
        form.enter_last_name(os.getenv("LASTNAME"))
        form.enter_email("invalid-email")
        form.select_gender()
        form.enter_mobile(os.getenv("ADDRESS_PHONE"))

        form.click_submit()

        assert "Thanks for submitting the form" not in driver.page_source



    @pytest.mark.regression
    def test_invalid_mobile(self, driver):
        driver.get(self.URL)

        form = TextPage(driver)

        form.enter_first_name(os.getenv("FIRSTNAME"))
        form.enter_last_name(os.getenv("LASTNAME"))
        form.enter_email(os.getenv("EMAIL"))
        form.select_gender()
        form.enter_mobile("123")

        form.click_submit()

        assert "Thanks for submitting the form" not in driver.page_source