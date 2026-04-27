import pytest
import os
from pages.base_page import BasePage
from pages.upload_page import UploadPage
from utils.config import DATA_FILE

@pytest.mark.regression
def test_file_upload_by_path(driver):
    """Test file upload using send_keys to input[type='file'].
    
    WHY THIS IS RELIABLE:
    - Directly sends file path to the file input element
    - No click-and-pray approach
    - Browser handles the upload natively
    """
    bp = BasePage(driver)
    up = UploadPage()
    bp.navigate("https://demoqa.com/upload-download")
    
    # Create a test file
    test_file = "test_upload.txt"
    with open(test_file, "w") as f:
        f.write("Test file upload content")
    
    bp.wait_for_visible(UploadPage.UPLOAD_INPUT)
    bp.upload_file(UploadPage.UPLOAD_INPUT, test_file)
    bp.verify_file_uploaded(success_indicator_xpath=UploadPage.UPLOAD_SUCCESS)
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    assert True

@pytest.mark.regression
def test_file_upload_with_json_data(driver):
    """Test file upload using data from JSON file"""
    bp = BasePage(driver)
    up = UploadPage()
    bp.navigate("https://demoqa.com/upload-download")
    
    # Get test data
    data = bp.get_data(DATA_FILE, "upload_file")
    
    # Create the test file
    with open(data, "w") as f:
        f.write("Test content from JSON data")
    
    bp.wait_for_visible(UploadPage.UPLOAD_INPUT)
    bp.upload_file(UploadPage.UPLOAD_INPUT, data)
    bp.verify_file_uploaded(expected_text=data)
    
    # Cleanup
    if os.path.exists(data):
        os.remove(data)
