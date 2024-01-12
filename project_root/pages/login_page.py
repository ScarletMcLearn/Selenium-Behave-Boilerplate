# login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from utils.helpers import Helpers

class LoginPage(BasePage):
    def __init__(self, driver):
        """
        Constructor for the LoginPage class.

        :param driver: WebDriver instance for interacting with the web browser.
        """
        super().__init__(driver)

        # Initialize locators from the LoginPageLocators class
        self.locators = LoginPageLocators()

    def enter_credentials_and_submit(self, username, password):
        """
        Enter the provided username and password, and submit the login form.

        :param username: The username to be entered.
        :param password: The password to be entered.
        """
        self.driver.find_element(*self.locators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.locators.SUBMIT_BUTTON).click()

    def wait_for_successful_login(self):
        """
        Wait for the successful login indicator to be clickable.

        Assumes the presence of a successful login indicator element.
        """
        expected_locator = self.locators.SUCCESSFUL_LOGIN_INDICATOR
        Helpers.wait_for_element_clickable(
            self.driver,
            expected_locator[0],
            expected_locator[1],
            timeout=10
        )
