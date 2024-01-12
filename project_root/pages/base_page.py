# base_page.py
class BasePage:
    def __init__(self, driver):
        """
        Constructor for the BasePage class.

        :param driver: WebDriver instance for interacting with the web browser.
        """
        self.driver = driver
