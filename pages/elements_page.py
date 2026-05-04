# Elements section locators
class TextBoxPage:
    FULL_NAME = "//input[@id='userName']"
    EMAIL = "//input[@id='userEmail']"
    CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"
    SUBMIT = "//button[@id='submit']"
    OUTPUT = "//div[contains(@class,'border')]"


class ButtonsPage:
    DOUBLE_CLICK_BTN = "//button[@id='doubleClickBtn']"
    RIGHT_CLICK_BTN = "//button[@id='rightClickBtn']"
    CLICK_ME_BTN = "//button[text()='Click Me']"
    DOUBLE_CLICK_MSG = "//p[contains(text(),'double click')]"
    RIGHT_CLICK_MSG = "//p[contains(text(),'right click')]"
    CLICK_ME_MSG = "//p[contains(text(),'dynamic click')]"


class RadioButtonPage:
    YES_RADIO = "//input[@id='yesRadio']/.."
    IMPRESSIVE_RADIO = "//input[@id='impressiveRadio']/.."
    RADIO_RESULT = "//span[@class='text-success']"