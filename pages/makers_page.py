from selenium.webdriver.common.by import By


class DemoQAPage:
    TEXT_BOX_URL = "https://demoqa.com/text-box"
    CHECKBOX_URL = "https://demoqa.com/checkbox"
    RADIO_URL = "https://demoqa.com/radio-button"

    HEADING = "//h1"

    USER_NAME = "//input[@id='userName']"
    USER_EMAIL = "//input[@id='userEmail']"
    CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = "//button[@id='submit']"
    OUTPUT = "//div[@id='output']"

    CHECKBOX = "//span[@class='rct-checkbox']"
    CHECKBOX_RESULT = "//div[@id='result']"

    YES_RADIO = "//label[@for='yesRadio']"
    RADIO_RESULT = "//p[@class='mt-3']"

    def __init__(self, driver):
        self.driver = driver