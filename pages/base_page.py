from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        
        # Scroll to element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        # Wait a bit for UI stabilization
        self.wait.until(EC.element_to_be_clickable(locator))
        
        # Use JS click (FINAL FIX)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, value):
        element = self.wait.until(EC.presence_of_element_located(locator))
        
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        # Click before typing (very important)
        element.click()
        
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text