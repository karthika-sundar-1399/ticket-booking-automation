# Import By for locator strategies (ID, XPATH, NAME, etc.)
from selenium.webdriver.common.by import By
# Import BasePage class that contains common element interaction methods
from pages.base_page import BasePage


# Page object class for the login page - handles all login functionality
class LoginPage(BasePage):

    # Locator for the email input field using NAME attribute
    EMAIL_INPUT = (By.NAME, "email")
    # Locator for the password input field using NAME attribute
    PASSWORD_INPUT = (By.NAME, "password")
    # Locator for the Login button using XPATH with partial text match
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")

    # Method to enter email address in the email input field
    def enter_email(self, email):
        # Call inherited send_keys method from BasePage with the email locator and value
        self.send_keys(self.EMAIL_INPUT, email)

    # Method to enter password in the password input field
    def enter_password(self, password):
        # Call inherited send_keys method from BasePage with the password locator and value
        self.send_keys(self.PASSWORD_INPUT, password)

    # Method to click the Login button to submit the login form
    def click_login(self):
        # Call inherited click method from BasePage with the Login button locator
        self.click(self.LOGIN_BUTTON)

    # Main method that executes the complete login flow
    def login(self, email, password):
        # Step 1: Enter the email address
        self.enter_email(email)
        # Step 2: Enter the password
        self.enter_password(password)
        # Step 3: Click the Login button to submit the form
        self.click_login()