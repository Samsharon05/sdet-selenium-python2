from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class EmployeePage(BasePage):
    WEB_TABLE_LINK = "//span[contains(text(),'Web Tables')]"
    ADD_BUTTON = "//button[@id='addNewRecordButton']"
    FIRST_NAME = "//input[@id='firstName']"
    LAST_NAME = "//input[@id='lastName']"
    EMAIL = "//input[@id='userEmail']"
    AGE = "//input[@id='age']"
    SALARY = "//input[@id='salary']"
    DEPARTMENT = "//input[@id='department']"
    SUBMIT = "//button[@id='submit']"
    TABLE_ROW = "//div[@class='rt-tr-group']"
    DELETE_BUTTON = "//span[@title='Delete']"
    EDIT_BUTTON = "//span[@title='Edit']"
    SEARCH_BOX = "//input[@id='searchBox']"
    NO_ROWS = "//div[contains(text(),'No rows found')]"
