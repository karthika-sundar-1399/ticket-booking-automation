from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()