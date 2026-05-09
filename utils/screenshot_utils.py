
import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional


def take_screenshot(driver: WebDriver, name: Optional[str] = None, folder: str = "screenshots") -> str:
    """
    Take a screenshot and save to folder.
    Returns the file path.
    """
    os.makedirs(folder, exist_ok=True)
    
    if name is None:
        name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    
    filepath = os.path.join(folder, f"{name}.png")
    driver.save_screenshot(filepath)
    return filepath


def take_screenshot_on_failure(driver: WebDriver, test_name: str) -> str:
    """Take screenshot with test name prefix for failures."""
    safe_name = test_name.replace(" ", "_").replace("/", "_")
    return take_screenshot(driver, f"FAIL_{safe_name}")