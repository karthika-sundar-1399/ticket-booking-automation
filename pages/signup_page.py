from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   # ✅ FIX
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

        # ✅ Confirm password using JS
        confirm = self.wait.until(
            EC.presence_of_element_located(self.CONFIRM_PASSWORD_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", confirm, password)

        self.click(self.SIGNUP_BUTTON)