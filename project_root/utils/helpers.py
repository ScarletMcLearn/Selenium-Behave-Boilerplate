from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Helpers:
    @staticmethod
    def wait_for_element_visible(driver, by, value, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element not visible within {timeout} seconds. {e}")

    @staticmethod
    def wait_for_element_clickable(driver, by, value, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element not clickable within {timeout} seconds. {e}")

    @staticmethod
    def wait_for_url_contains(driver, expected_url_part, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.url_contains(expected_url_part)
            )
        except Exception as e:
            raise TimeoutError(f"URL does not contain '{expected_url_part}' within {timeout} seconds. {e}")
