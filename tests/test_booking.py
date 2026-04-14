# Import pytest for test framework functionality
import pytest
# Import BookingPage class to interact with the booking page
from pages.booking_page import BookingPage
# Import BASE_URL configuration constant
from utils.config import BASE_URL
# Import read_test_data function to read test data from CSV
from utils.data_reader import read_test_data
# Import get_logger function to create a logger instance
from utils.logger import get_logger

# Initialize the logger to capture test execution logs
logger = get_logger()

# Read all test data from the booking_data.csv file
test_data = read_test_data("test_data/booking_data.csv")


# Define a parameterized test that runs once for each row in the test data
# @pytest.mark.parametrize will create separate test runs for each data row
@pytest.mark.parametrize("data", test_data)
def test_ticket_booking_data_driven(driver, data):
    # Log the start of the test execution
    logger.info("Test started")

    # Navigate to the flights page using the base URL
    driver.get(BASE_URL + "flights/")
    # Create a BookingPage instance to interact with booking page elements
    booking = BookingPage(driver)

    # Call the book_ticket method with test data (from, to, date columns from CSV)
    booking.book_ticket(
        data["from"],      # Departure location from test data
        data["to"],        # Destination location from test data
        data["date"]       # Travel date from test data
    )

    # Retrieve the "From" field value after the booking submission
    from_value = driver.find_element(*booking.FROM_INPUT).get_attribute("value")
    # Retrieve the "To" field value after the booking submission
    to_value = driver.find_element(*booking.TO_INPUT).get_attribute("value")

    # Check if the expected result is "success" (comparing string from CSV)
    if data["expected_result"] == "success":
        # ✅ Success scenario: verify that both fields are filled with values
        # Assert that "From" field is not empty (meaning booking was successful)
        assert from_value != "", "From field is empty"
        # Assert that "To" field is not empty (meaning booking was successful)
        assert to_value != "", "To field is empty"

    else:
        # ✅ Failure scenario: verify that values remain same (no change behavior)
        # Assert that "From" field has the exact value that was entered
        assert from_value == data["from"]
        # Assert that "To" field has the exact value that was entered
        assert to_value == data["to"]