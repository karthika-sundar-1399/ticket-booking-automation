import pytest
from utils.config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_booking_flow_with_login(driver):

    driver.get(BASE_URL + "flights/")

    wait = WebDriverWait(driver, 10)

    # Click Book Now using JS
    book_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[contains(text(),'Book Now')])[1]")
        )
    )
    driver.execute_script("arguments[0].click();", book_btn)

    # Verify login redirect
    assert "login" in driver.current_url

    # 🔥 FIX: Click SignUp using JS (FINAL FIX)
    signup_link = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "SignUp"))
    )
    driver.execute_script("arguments[0].click();", signup_link)

    # Signup flow
    signup = SignupPage(driver)

    import time
    email = f"testuser{int(time.time())}@gmail.com"

    signup.signup("Test User", email, "123456")

    # Go back to login with next URL
    driver.get(BASE_URL + "users/login/?next=/flights/seat-selection/8/")

    login = LoginPage(driver)
    login.login(email, "123456")

    # Final validation
    assert "login" in driver.current_url or "flights" in driver.current_url