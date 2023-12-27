from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage
from utils.driver_manager import DriverManager
from utils.config import Config

def before_all(context):
    # Load configuration
    context.config = Config()

    # Initialize WebDriver
    context.driver_manager = DriverManager()
    context.driver = context.driver_manager.get_driver()

    # Initialize Page Objects
    context.base_page = BasePage(context.driver)

def before_feature(context, feature):
    # You can add any setup logic specific to a feature here
    pass

def before_scenario(context, scenario):
    # You can add any setup logic specific to a scenario here
    pass

def before_step(context, step):
    # You can add any logic to be executed before each step here
    pass

def after_step(context, step):
    # You can add any logic to be executed after each step here
    pass

def after_scenario(context, scenario):
    # You can add any teardown logic specific to a scenario here
    pass

def after_feature(context, feature):
    # You can add any teardown logic specific to a feature here
    pass

def after_all(context):
    # Teardown WebDriver and perform any cleanup
    context.driver_manager.quit_driver()

