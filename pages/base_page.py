# Import WebDriverWait for explicit waits (wait for elements to appear)
from selenium.webdriver.support.ui import WebDriverWait
# Import expected_conditions to define conditions to wait for
from selenium.webdriver.support import expected_conditions as EC


# Base class containing common methods used by all page object classes
class BasePage:

    # Constructor to initialize the BasePage with a driver instance
    def __init__(self, driver):
        # Store the WebDriver instance to interact with the browser
        self.driver = driver
        # Create a WebDriverWait object with a 10-second timeout for waiting
        self.wait = WebDriverWait(driver, 10)

    # Method to click on an element using a locator (tuple of By.type and identifier)
    def click(self, locator):
        # Wait until the element is present in the DOM
        element = self.wait.until(EC.presence_of_element_located(locator))

        # Scroll the element into view to ensure it's visible on the screen
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Click the element using JavaScript instead of Selenium click (more reliable)
        self.driver.execute_script("arguments[0].click();", element)

    # Method to send text input to a form field using a locator and value
    def send_keys(self, locator, value):
        # Wait until the element is present in the DOM
        element = self.wait.until(EC.presence_of_element_located(locator))

        # Scroll the element into view to ensure it's visible on the screen
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Focus on the element using JavaScript (ensures focus even for hidden elements)
        self.driver.execute_script("arguments[0].focus();", element)

        # Clear the input field by setting its value to empty string using JavaScript
        self.driver.execute_script("arguments[0].value = '';", element)

        # Send the text value to the now-empty element
        element.send_keys(value)