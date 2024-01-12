# utilities/logger_utils.py

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s [%(levelname)s] - %(message)s",  # Define the log message format
    handlers=[
        logging.FileHandler("automation.log"),  # Log to a file named "automation.log"
        logging.StreamHandler()  # Log to the console
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

# Decorator for logging and error handling
def log_and_handle_errors(func):
    """
    Decorator function for logging and handling errors in other functions.

    :param func: The function to be decorated.
    :return: The decorated function.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)  # Execute the original function
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")  # Log the error
            raise  # Re-raise the exception after logging
    return wrapper
