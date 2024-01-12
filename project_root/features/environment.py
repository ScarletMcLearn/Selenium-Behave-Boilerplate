# environment.py
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService

from utils.driver_manager import initialize_driver, quit_driver

def before_scenario(context, scenario):
    # Retrieve the desired browser from userdata or default to Chrome
    browser = context.config.userdata.get("browser", "chrome")

    # Initialize WebDriver for the scenario
    context.driver = initialize_driver(browser)

def after_scenario(context, scenario):
    # Quit the WebDriver after the scenario is completed
    quit_driver(context.driver)
