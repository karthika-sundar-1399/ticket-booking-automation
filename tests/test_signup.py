# Import pytest for test framework functionality
import pytest
# Import SignupPage class to interact with the signup page
from pages.signup_page import SignupPage
# Import BASE_URL configuration constant
from utils.config import BASE_URL
# Import time module to generate unique timestamps
import time


# Test function to verify user signup functionality
def test_signup(driver):
    # Navigate to the signup page using the base URL
    driver.get(BASE_URL + "users/signup/")

    # Create a SignupPage instance to interact with signup page elements
    signup = SignupPage(driver)

    # Import time module again (note: could be at top of file for better practice)
    import time
    # Generate a unique email using current timestamp to avoid duplicate email errors
    email = f"testuser{int(time.time())}@gmail.com"

    # Perform signup with test user data (name, unique email, password)
    signup.signup("Test User", email, "123456")

    # ✅ VALIDATION: Get the name field value after successful signup
    name_value = driver.find_element(*signup.NAME_INPUT).get_attribute("value")
    # Get the email field value after successful signup
    email_value = driver.find_element(*signup.EMAIL_INPUT).get_attribute("value")

    # Assert that name field is not empty (indicating successful signup)
    assert name_value != ""
    # Assert that email field is not empty (indicating successful signup)
    assert email_value != ""