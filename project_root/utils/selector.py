from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def find(identifier, selector, wait_time, driver, find_all=True):
    """
    Find the first element or all elements based on the identifier and selector,
    with the specified explicit wait time.

    Parameters:
    - identifier (str): The type of identifier to be used (e.g., ID, NAME, XPATH).
    - selector (str): The value of the identifier (e.g., the ID value, XPATH expression).
    - wait_time (float): The explicit wait time in seconds.
    - driver (webdriver): The Selenium WebDriver instance.
    - find_all (bool): If True, find all matching elements; if False, find the first one. Default is True.

    Returns:
    - If find_all is True, returns a list of elements; if False, returns the first matching element.
    - Returns None if no elements are found within the specified wait time.
    """
    by_map = {
        "ID": By.ID,
        "NAME": By.NAME,
        "XPATH": By.XPATH,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "TAG_NAME": By.TAG_NAME,
        "CLASS_NAME": By.CLASS_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
    }

    by = by_map.get(identifier.upper())
    if by is None:
        raise ValueError("Invalid identifier. Supported values are: ID, NAME, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, CLASS_NAME, CSS_SELECTOR")

    try:
        if find_all:
            elements = WebDriverWait(driver, wait_time).until(
                EC.presence_of_all_elements_located((by, selector))
            )
        else:
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((by, selector))
            )
    except TimeoutError:
        if find_all:
            return []
        else:
            return None

    return elements if find_all else element


# Example usage:
driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")

# Find all elements with ID "myDynamicElement" and wait for up to 10 seconds
all_elements = find("ID", "myDynamicElement", 10, driver, find_all=True)
print(all_elements)

# Find the first element with NAME "username" and wait for up to 5 seconds
first_element = find("NAME", "username", 5, driver, find_all=False)
print(first_element)

driver.quit()
