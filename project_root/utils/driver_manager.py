from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverManager:
    def __init__(self, browser='chrome', headless=True):
        self.browser = browser.lower()
        self.headless = headless
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        if self.browser == 'chrome':
            driver = self.init_chrome_driver()
        elif self.browser == 'firefox':
            driver = self.init_firefox_driver()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")

        # Set implicit wait to handle dynamic elements
        driver.implicitly_wait(10)  # Adjust the wait time as needed

        return driver
    

    
    def init_chrome_driver(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')

        return webdriver.Chrome(options=chrome_options)

    def init_firefox_driver(self):
        firefox_options = FirefoxOptions()
        if self.headless:
            firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--window-size=1920,1080')

        return webdriver.Firefox(options=firefox_options, desired_capabilities=DesiredCapabilities.FIREFOX)

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
