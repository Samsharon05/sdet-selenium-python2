import logging
from logging import config
import os
from datetime import datetime
import pytest
from selenium import webdriver
from utils.config import Configdata

data = Configdata()

@pytest.fixture(scope="function")
def driver():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=opt)
    driver.get(data.link)
    driver.maximize_window()

    yield driver
    driver.quit()
    
@pytest.fixture(scope="function")
def driver():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture(scope="function")
def driver():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=opt)
    driver.get(config.base_url)
    driver.maximize_window()
    driver.save_screenshot("screenshot.png")

    yield driver
    driver.quit()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")

@pytest.fixture
def driver():
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    logger.info("Browser opened")
    driver.get("https://demoqa.com")
    logger.info("Navigated to demoqa.com")
    
    yield driver
    
    driver.quit()
    logger.info("Browser closed")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
            
            driver.save_screenshot(screenshot_path)
            logger.error(f"Test FAILED - Screenshot saved: {screenshot_path}")
            
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "downloads")

@pytest.fixture
def driver():
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    logger.info("Browser opened")
    driver.get("https://demoqa.com")
    logger.info("Navigated to demoqa.com")
    
    yield driver
    
    driver.quit()
    logger.info("Browser closed")