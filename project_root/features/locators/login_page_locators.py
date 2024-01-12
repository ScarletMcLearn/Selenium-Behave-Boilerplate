# login_page_locators.py
from selenium.webdriver.common.by import By
from .base_locators import BaseLocators

class LoginPageLocators(BaseLocators):
    # Locators for the login page
    USERNAME_INPUT = (By.ID, "user-name")             # Username input field
    PASSWORD_INPUT = (By.ID, "password")               # Password input field
    SUBMIT_BUTTON = (By.ID, "login-button")            # Login submit button
    SUCCESSFUL_LOGIN_INDICATOR = (By.CLASS_NAME, "title")  # Indicator for successful login
