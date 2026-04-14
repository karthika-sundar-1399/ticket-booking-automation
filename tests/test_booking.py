import pytest
from pages.booking_page import BookingPage
from utils.config import BASE_URL
from utils.data_reader import read_test_data
from utils.logger import get_logger

logger = get_logger()

test_data = read_test_data("test_data/booking_data.csv")


@pytest.mark.parametrize("data", test_data)
def test_ticket_booking_data_driven(driver, data):

    logger.info("Test started")

    driver.get(BASE_URL + "flights/")
    booking = BookingPage(driver)

    booking.book_ticket(
        data["from"],
        data["to"],
        data["date"]
    )

    # Get values after submission
    from_value = driver.find_element(*booking.FROM_INPUT).get_attribute("value")
    to_value = driver.find_element(*booking.TO_INPUT).get_attribute("value")

    if data["expected_result"] == "success":
        # ✅ Success → values should be filled
        assert from_value != "", "From field is empty"
        assert to_value != "", "To field is empty"

    else:
        # ✅ Failure → values remain same OR no change behavior
        assert from_value == data["from"]
        assert to_value == data["to"]