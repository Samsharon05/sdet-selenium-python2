import pytest
from selenium import webdriver
from utils.configD10 import Configdata

config = Configdata()

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