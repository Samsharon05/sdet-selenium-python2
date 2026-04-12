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