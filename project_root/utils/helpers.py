# helpers.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Helpers:
    @staticmethod
    def wait_for_element_visible(driver, by, value, timeout=10):
        """
        Wait for an element to be visible on the page.

        :param driver: WebDriver instance.
        :param by: The locator strategy (e.g., By.ID, By.XPATH).
        :param value: The value of the locator.
        :param timeout: Maximum time to wait for the element to be visible (default is 10 seconds).
        :return: The located WebElement.
        :raises TimeoutError: If the element is not visible within the specified timeout.
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element not visible within {timeout} seconds. {e}")

    @staticmethod
    def wait_for_element_clickable(driver, by, value, timeout=10):
        """
        Wait for an element to be clickable on the page.

        :param driver: WebDriver instance.
        :param by: The locator strategy (e.g., By.ID, By.XPATH).
        :param value: The value of the locator.
        :param timeout: Maximum time to wait for the element to be clickable (default is 10 seconds).
        :return: The located WebElement.
        :raises TimeoutError: If the element is not clickable within the specified timeout.
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element not clickable within {timeout} seconds. {e}")

    @staticmethod
    def wait_for_url_contains(driver, expected_url_part, timeout=10):
        """
        Wait for the URL to contain a specific part.

        :param driver: WebDriver instance.
        :param expected_url_part: The expected part of the URL.
        :param timeout: Maximum time to wait for the URL to contain the expected part (default is 10 seconds).
        :raises TimeoutError: If the URL does not contain the expected part within the specified timeout.
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.url_contains(expected_url_part)
            )
        except Exception as e:
            raise TimeoutError(f"URL does not contain '{expected_url_part}' within {timeout} seconds. {e}")
