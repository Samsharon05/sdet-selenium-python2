# Widgets section locators
class DatePickerPage:
    DATE_INPUT = "//input[@id='datePickerMonthYearInput']"
    MONTH_SELECT = "//select[@class='react-datepicker__month-select']"
    YEAR_SELECT = "//select[@class='react-datepicker__year-select']"
    DAY_PICKER = "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month'))]"


class SliderPage:
    SLIDER = "//input[@type='range']"
    SLIDER_VALUE = "//input[@id='sliderValue']"