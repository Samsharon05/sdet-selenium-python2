from selenium.webdriver.common.by import By
import time
from pydoc import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# class TestWaits:

#     def test_dynamic_loading_fail(self):
#         driver = webdriver.Chrome()
#         driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
#         driver.find_element(By.TAG_NAME, "button").click()

#         time.sleep(2) 

#         text = driver.find_element(By.ID, "finish").text

#         assert "Hello World!" in text
        
# class TestWaits:

#     def test_dynamic_loading_wait(self):
#         driver = webdriver.Chrome()
#         driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

#         driver.find_element(By.TAG_NAME, "button").click()

#         wait = WebDriverWait(driver, 10)

#         text = wait.until(EC.visibility_of_element_located((By.ID, "finish"))).text

#         assert "Hello World!" in text
        

# class TestWaits:
#     def test_flaky_no_wait(self):
#         driver = webdriver.Chrome()
#         driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

#         driver.find_element(By.TAG_NAME, "button").click()

     
#         text = driver.find_element(By.ID, "finish").text

#         assert "Hello World!" in text
        
    
class TestWaits:
    def test_dynamic_loading_wait2(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        driver.find_element(By.TAG_NAME, "button").click()

        wait = WebDriverWait(driver, 10)

        text = wait.until(EC.presence_of_element_located((By.ID, "finish"))).text

        assert "Hello World!" in text

        driver.quit()