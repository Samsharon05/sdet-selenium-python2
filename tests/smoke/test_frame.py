from pages.frame_page import FramesPage


class TestFrames:

    URL = "https://demoqa.com/frames"

    def test_iframe(self, driver):
        driver.get(self.URL)

        frame_page = FramesPage(driver)

        frame_page.switch_to_frame()
        text = frame_page.get_heading_text()

        assert "This is a sample page" in text

        frame_page.switch_to_default()