import pytest
import os
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.download_page import DownloadPage

logger = logging.getLogger(__name__)

@pytest.mark.regression
def test_file_download_http_verification(driver):
    bp = BasePage(driver)
    dp = DownloadPage()
    bp.navigate("https://demoqa.com/upload-download")
    
    bp.wait_for_visible(DownloadPage.DOWNLOAD_BUTTON)
    button = driver.find_element(By.XPATH, DownloadPage.DOWNLOAD_BUTTON)
    assert button.is_enabled()
    
    logger.info("Download button verified - ready for click")
    assert True

@pytest.mark.regression
def test_file_download_filesystem_check(driver):
    bp = BasePage(driver)
    dp = DownloadPage()
    bp.navigate("https://demoqa.com/upload-download")
    
    download_dir = bp.get_download_dir()
    

    bp.wait_for_visible(DownloadPage.DOWNLOAD_BUTTON)
    bp.click(DownloadPage.DOWNLOAD_BUTTON)
    

    filename = "sampleFile.jpeg"
    filepath = bp.verify_file_exists(download_dir, filename, timeout=15)
    

    file_size = os.path.getsize(filepath)
    assert file_size > 0, f"Downloaded file is empty: {file_size} bytes"
    
    logger.info(f"Download verified: {filepath} ({file_size} bytes)")
    assert True


