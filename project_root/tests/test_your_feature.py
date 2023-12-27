from behave import given, when, then
from pages.your_page1 import YourPage1
from pages.your_page2 import YourPage2
from utils.helpers import wait_for_element_visible

@given('I am on the application home page')
def step_given_application_home_page(context):
    context.base_page.open_url(context.config.base_url)
    context.your_page1 = YourPage1(context.driver)

@when('I navigate to "{page}"')
def step_when_navigate_to_page(context, page):
    # Example: Navigate to the desired page using Page Object
    if page.lower() == 'your page 1':
        context.your_page1.navigate()

    elif page.lower() == 'your page 2':
        context.your_page2 = YourPage2(context.driver)
        context.your_page2.navigate()

    else:
        raise ValueError(f"Unknown page: {page}")

@when('I perform some action on "{element}"')
def step_when_perform_action(context, element):
    # Example: Perform an action on a specific element using Page Object
    if element.lower() == 'button':
        context.your_page1.click_some_button()

    elif element.lower() == 'input':
        context.your_page2.enter_text_in_input()

    else:
        raise ValueError(f"Unknown element: {element}")

@then('I should see "{expected_text}" on the page')
def step_then_verify_text_on_page(context, expected_text):
    # Example: Verify expected text on the page using Page Object
    actual_text = context.your_page2.get_text_from_element()
    assert actual_text == expected_text, f"Expected: {expected_text}, Actual: {actual_text}"

@then('I should see the "{element}" displayed')
def step_then_verify_element_displayed(context, element):
    # Example: Verify if a specific element is displayed using Page Object
    if element.lower() == 'logo':
        assert context.your_page1.is_logo_displayed(), f"{element} is not displayed"

    elif element.lower() == 'header':
        assert wait_for_element_visible(context.your_page2.get_header_element()), f"{element} is not displayed"

    else:
        raise ValueError(f"Unknown element: {element}")
