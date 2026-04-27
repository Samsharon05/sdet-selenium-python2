from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TextPage(BasePage):

    FNAME = (By.ID, "firstName")
    LNAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.XPATH, "//label[@for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    DOB = (By.ID, "dateOfBirthInput")
    SUBJECT = (By.ID, "subjectsInput")
    HOBBY1 = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    HOBBY2 = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    SUBMIT = (By.ID, "submit")

    def enter_first_name(self, fname):
        self.type_text(*self.FNAME, fname)

    def enter_last_name(self, lname):
        self.type_text(*self.LNAME, lname)

    def enter_email(self, email):
        self.type_text(*self.EMAIL, email)

    def select_gender(self):
        self.click(*self.GENDER)

    def enter_mobile(self, mobile):
        self.type_text(*self.MOBILE, mobile)

    def enter_dob(self):
        dob = self.driver.find_element(*self.DOB)
        dob.clear()
        dob.send_keys("10 Jan 1995")
        dob.send_keys(Keys.ENTER)

    def enter_subject(self, subject):
        sub = self.driver.find_element(*self.SUBJECT)
        sub.send_keys(subject)
        sub.send_keys(Keys.ENTER)

    def select_hobbies(self):
        hobby1 = self.driver.find_element(*self.HOBBY1)
        hobby2 = self.driver.find_element(*self.HOBBY2)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", hobby1)
        self.driver.execute_script("arguments[0].click();", hobby1)
        self.driver.execute_script("arguments[0].click();", hobby2)

    def enter_address(self, address):
        self.type_text(*self.ADDRESS, address)

    def select_state(self, state):
        state_input = self.driver.find_element(By.ID, "react-select-3-input")
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

    def select_city(self, city):
        city_input = self.driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

    def click_submit(self):
        element = self.driver.find_element(*self.SUBMIT)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)