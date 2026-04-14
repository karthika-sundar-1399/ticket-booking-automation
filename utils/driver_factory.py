# Import the webdriver module from Selenium for browser automation
from selenium import webdriver
# Import Service class to configure Chrome driver service
from selenium.webdriver.chrome.service import Service
# Import ChromeDriverManager to automatically download and manage ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager


# Factory function that creates and returns a configured Chrome WebDriver instance
def get_driver():
    # Create a ChromeOptions object to configure browser settings
    options = webdriver.ChromeOptions()
    # Add argument to start the Chrome browser in maximized window mode
    options.add_argument("--start-maximized")

    # Create and initialize a Chrome WebDriver instance with the following configuration:
    driver = webdriver.Chrome(
        # Use Service class with ChromeDriverManager to automatically download and manage ChromeDriver
        service=Service(ChromeDriverManager().install()),
        # Pass the configured options to the Chrome WebDriver
        options=options
    )
    # Return the configured WebDriver instance for use in tests
    return driver