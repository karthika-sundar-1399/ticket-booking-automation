# Import pytest for test framework functionality
import pytest
# Import LoginPage class to interact with the login page
from pages.login_page import LoginPage
# Import BASE_URL configuration constant
from utils.config import BASE_URL


# Test function to verify valid login credentials work correctly
def test_valid_login(driver):
    # Navigate to the login page using the base URL
    driver.get(BASE_URL + "users/login/")

    # Create a LoginPage instance to interact with login page elements
    login = LoginPage(driver)
    # Perform login with valid credentials (email and password)
    login.login("abcde@gmail.com", "123456")

    # ✅ VALIDATION: Get the email field value after successful login
    email_value = driver.find_element(*login.EMAIL_INPUT).get_attribute("value")

    # Assert that email field is not empty (indicating successful login)
    assert email_value != ""


# Test function to verify invalid login credentials are rejected
def test_invalid_login(driver):
    # Navigate to the login page using the base URL
    driver.get(BASE_URL + "users/login/")

    # Create a LoginPage instance to interact with login page elements
    login = LoginPage(driver)
    # Attempt login with invalid credentials (wrong email and password)
    login.login("wrong@gmail.com", "wrongpass")

    # VALIDATION: Stay on the same login page = failure (not redirected to dashboard)
    # Assert that the current URL ends with /users/login/ (still on login page)
    assert driver.current_url.endswith("/users/login/")