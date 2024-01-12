# driver_manager.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def initialize_driver(browser="chrome"):
    """
    Initialize a WebDriver instance based on the specified browser.

    :param browser: Browser name ("chrome" or "firefox"). Default is "chrome".
    :return: WebDriver instance.
    :raises ValueError: If an unsupported browser is specified.
    """
    if browser.lower() == "chrome":
        return webdriver.Chrome()
    elif browser.lower() == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

def quit_driver(driver):
    """
    Quit the provided WebDriver instance.

    :param driver: WebDriver instance to be quit.
    """
    if driver:
        driver.quit()

# # Example Usage:

# # Example 1: Initialize a ChromeDriver
# chrome_driver = initialize_driver()
# chrome_driver.get("https://www.example.com")
# # Perform actions with the ChromeDriver
# quit_driver(chrome_driver)  # Quit the ChromeDriver

# # Example 2: Initialize a FirefoxDriver
# firefox_driver = initialize_driver(browser="firefox")
# firefox_driver.get("https://www.example.com")
# # Perform actions with the FirefoxDriver
# quit_driver(firefox_driver)  # Quit the FirefoxDriver
