# Import By for locator strategies (ID, XPATH, NAME, etc.)
from selenium.webdriver.common.by import By
# Import WebDriverWait for explicit waits (wait for elements to appear)
from selenium.webdriver.support.ui import WebDriverWait
# Import expected_conditions to define conditions to wait for
from selenium.webdriver.support import expected_conditions as EC   # ✅ FIX
# Import BasePage class that contains common element interaction methods
from pages.base_page import BasePage


# Page object class for the signup page - handles all signup functionality
class SignupPage(BasePage):

    # Locator for the name input field using NAME attribute
    NAME_INPUT = (By.NAME, "name")
    # Locator for the email input field using NAME attribute
    EMAIL_INPUT = (By.NAME, "email")
    # Locator for the password input field using NAME attribute
    PASSWORD_INPUT = (By.NAME, "password")
    # Locator for the confirm password input field using NAME attribute
    CONFIRM_PASSWORD_INPUT = (By.NAME, "confirm_password")
    # Locator for the Sign Up button using XPATH with partial text match
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(),'Sign Up')]")

    # Main method that executes the complete signup flow
    def signup(self, name, email, password):
        # Step 1: Enter the user's name using inherited send_keys method
        self.send_keys(self.NAME_INPUT, name)
        # Step 2: Enter the user's email using inherited send_keys method
        self.send_keys(self.EMAIL_INPUT, email)
        # Step 3: Enter the user's password using inherited send_keys method
        self.send_keys(self.PASSWORD_INPUT, password)

        # ✅ Step 4: Enter confirm password using JavaScript (more reliable)
        # Wait until the confirm password element is present in the DOM
        confirm = self.wait.until(
            EC.presence_of_element_located(self.CONFIRM_PASSWORD_INPUT)
        )
        # Set the confirm password field value using JavaScript and pass password as second argument
        self.driver.execute_script("arguments[0].value = arguments[1];", confirm, password)

        # Step 5: Click the Sign Up button to submit the signup form
        self.click(self.SIGNUP_BUTTON)