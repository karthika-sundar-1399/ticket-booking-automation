# Import the logging module for logging test execution details
import logging
# Import os module for file system operations
import os


# Function to get a configured logger instance for test execution
def get_logger():
    # Check if the 'logs' directory exists
    if not os.path.exists("logs"):
        # If logs directory doesn't exist, create it
        os.makedirs("logs")

    # Configure the logging system with specific settings
    logging.basicConfig(
        # Specify the file to write log messages to
        filename="logs/test.log",
        # Set the logging level to INFO (captures INFO and above severity messages)
        level=logging.INFO,
        # Define the format of log messages: timestamp - level - message
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Get and return the root logger instance
    return logging.getLogger()