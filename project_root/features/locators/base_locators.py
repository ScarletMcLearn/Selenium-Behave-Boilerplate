# base_locators.py
from selenium.webdriver.common.by import By

class BaseLocators:
    # Common element locator using ID
    COMMON_ELEMENT = (By.ID, "common-element-id")
