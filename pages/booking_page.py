# Import By for locator strategies (ID, XPATH, NAME, etc.)
from selenium.webdriver.common.by import By
# Import BasePage class that contains common element interaction methods
from pages.base_page import BasePage


# Page object class for the booking page - handles all booking functionality
class BookingPage(BasePage):

    # Locator for the "From" destination input field using ID selector
    FROM_INPUT = (By.ID, "source")
    # Locator for the "To" destination input field using ID selector
    TO_INPUT = (By.ID, "destination")
    # Locator for the date input field using ID selector
    DATE_INPUT = (By.ID, "flightsearchdateInput")
    # Locator for the Search button using XPATH with partial text match
    SEARCH_BTN = (By.XPATH, "//button[contains(text(),'Search')]")

    # Method to enter the departure location in the From field
    def enter_from_location(self, value):
        # Call inherited send_keys method from BasePage with the From locator and value
        self.send_keys(self.FROM_INPUT, value)

    # Method to enter the destination location in the To field
    def enter_to_location(self, value):
        # Call inherited send_keys method from BasePage with the To locator and value
        self.send_keys(self.TO_INPUT, value)

    # Method to select the travel date in the date input field
    def select_date(self, value):
        # Call inherited send_keys method from BasePage with the Date locator and value
        self.send_keys(self.DATE_INPUT, value)

    # Method to click the Search button to perform flight search
    def click_search(self):
        # Call inherited click method from BasePage with the Search button locator
        self.click(self.SEARCH_BTN)

    # Main method that executes the complete booking ticket flow
    def book_ticket(self, from_loc, to_loc, date):
        # Step 1: Enter the departure location
        self.enter_from_location(from_loc)
        # Step 2: Enter the destination location
        self.enter_to_location(to_loc)
        # Step 3: Select the travel date
        self.select_date(date)
        # Step 4: Click the Search button to complete the booking search
        self.click_search()