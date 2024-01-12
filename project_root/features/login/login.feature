# user_login.feature

Feature: User Login

  Scenario: Successful Login Using Feature Params
    # Navigate to the specified site
    Given the user is on the site "https://www.saucedemo.com/"
    # Provide correct username and password, then submit the form
    When the user enters correct username "standard_user" and password "secret_sauce" and submits the form
    # Check if the user is successfully logged in
    Then the user should be successfully logged in

  Scenario: Successful Login Using Config File
    # Navigate to the site specified in the configuration file
    Given the user is on the site in config file
    # Provide correct username and password, then submit the form
    When the user enters correct username and password and submits the form
    # (Add additional steps or assertions if needed for verification)
