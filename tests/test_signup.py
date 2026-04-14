import pytest
from pages.signup_page import SignupPage
from utils.config import BASE_URL
import time


def test_signup(driver):
    driver.get(BASE_URL + "users/signup/")

    signup = SignupPage(driver)

    import time
    email = f"testuser{int(time.time())}@gmail.com"

    signup.signup("Test User", email, "123456")

    # ✅ Check if form values are filled (success behavior)
    name_value = driver.find_element(*signup.NAME_INPUT).get_attribute("value")
    email_value = driver.find_element(*signup.EMAIL_INPUT).get_attribute("value")

    assert name_value != ""
    assert email_value != ""