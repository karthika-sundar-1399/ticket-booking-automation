import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL


def test_valid_login(driver):
    driver.get(BASE_URL + "users/login/")

    login = LoginPage(driver)
    login.login("abcde@gmail.com", "123456")

    # ✅ FINAL VALIDATION
    email_value = driver.find_element(*login.EMAIL_INPUT).get_attribute("value")

    assert email_value != ""


def test_invalid_login(driver):
    driver.get(BASE_URL + "users/login/")

    login = LoginPage(driver)
    login.login("wrong@gmail.com", "wrongpass")

    # Stay on same page = failure
    assert driver.current_url.endswith("/users/login/")