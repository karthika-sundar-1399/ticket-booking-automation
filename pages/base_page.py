from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))

        # Scroll
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # JS click (FINAL)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, value):
        element = self.wait.until(EC.presence_of_element_located(locator))

        # Scroll
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Focus using JS (IMPORTANT)
        self.driver.execute_script("arguments[0].focus();", element)

        # Clear using JS (important fix)
        self.driver.execute_script("arguments[0].value = '';", element)

        element.send_keys(value)