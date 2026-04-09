import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opt)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
    