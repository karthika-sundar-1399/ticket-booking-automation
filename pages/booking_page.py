from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookingPage(BasePage):

    FROM_INPUT = (By.ID, "source")
    TO_INPUT = (By.ID, "destination")
    DATE_INPUT = (By.ID, "flightsearchdateInput")
    SEARCH_BTN = (By.XPATH, "//button[contains(text(),'Search')]")

    def enter_from_location(self, value):
        self.send_keys(self.FROM_INPUT, value)

    def enter_to_location(self, value):
        self.send_keys(self.TO_INPUT, value)

    def select_date(self, value):
        self.send_keys(self.DATE_INPUT, value)

    def click_search(self):
        self.click(self.SEARCH_BTN)

    def book_ticket(self, from_loc, to_loc, date):
        self.enter_from_location(from_loc)
        self.enter_to_location(to_loc)
        self.select_date(date)
        self.click_search()