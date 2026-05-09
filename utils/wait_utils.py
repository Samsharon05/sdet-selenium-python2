
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_for_clickable(driver, xpath, timeout=10):

    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )


def wait_for_visible(driver, xpath, timeout=10):

    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )


def wait_for_invisible(driver, xpath, timeout=10):

    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.XPATH, xpath))
    )


def wait_for_text(driver, xpath, text, timeout=10):

    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element((By.XPATH, xpath), text)
    )


def wait_for_url_contains(driver, fragment, timeout=10):

    return WebDriverWait(driver, timeout).until(
        EC.url_contains(fragment)
    )