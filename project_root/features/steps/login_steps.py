# features/steps/user_login_steps.py
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Importing Config and LoginPage classes
from utils.config import Config
from pages.login_page import LoginPage

# Setting up the configuration
config = Config()
base_url = config.base_url

# Step Definitions

@given('the user is on the site "{site}"')
def step_user_on_site(context, site):
    # Initialize the LoginPage instance with the driver
    context.login_page = LoginPage(context.driver)
    context.login_page.driver.get(site)


@when('the user enters correct username "{username}" and password "{password}" and submits the form')
def step_user_enters_credentials(context, username, password):
    # Utilize the LoginPage method for entering credentials and submitting
    context.login_page.enter_credentials_and_submit(username, password)


@then('the user should be successfully logged in')
def step_user_successful_login(context):
    # Wait for successful login using the LoginPage method
    context.login_page.wait_for_successful_login()
    context.driver.quit()


@given('the user is on the site in config file')
def step_user_on_site_from_config(context):
    # Navigate to the site specified in the configuration file
    context.driver.get(base_url)


@when('the user enters correct username and password and submits the form')
def step_user_enters_credentials_from_config(context):
    # Retrieve valid credentials from the configuration file
    valid_username = config.valid_username
    valid_password = config.valid_password

    # Locate and fill the username and password fields
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    context.driver.find_element(*USERNAME_INPUT).send_keys(valid_username)
    context.driver.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    # Additional steps or assertions can be added as needed
