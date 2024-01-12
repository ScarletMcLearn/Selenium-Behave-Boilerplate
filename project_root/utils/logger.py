# your_script.py

from logger import Logger

# Get the logger instance
logger = Logger().get_logger()

# Log informational and error messages
logger.info("This is an informational message.")
logger.error("This is an error message.")
