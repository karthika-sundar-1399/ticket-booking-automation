from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):

    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "confirm_password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(),'Sign Up')]")

    def signup(self, name, email, password):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)
        self.click(self.SIGNUP_BUTTON)