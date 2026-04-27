from pages.windows_page import WindowsPage


class TestWindows:

    URL = "https://demoqa.com/browser-windows"

    def test_new_tab(self, driver):
        driver.get(self.URL)

        window_page = WindowsPage(driver)

        window_page.open_new_tab()
        parent = window_page.switch_to_new_tab()

        text = window_page.get_heading_text()
        assert "This is a sample page" in text

        window_page.close_tab_and_return(parent)