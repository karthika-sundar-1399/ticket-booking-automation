from selenium.webdriver.common.by import By  # Import locator strategies like XPATH and LINK_TEXT
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions helpers
from pages.signup_page import SignupPage  # Import the SignupPage page object class
import time  # Import time to create a unique email address

BASE_URL = "https://9659058568.pythonanywhere.com/"  # Define the base URL for the site under test


def test_booking_flow_with_login(driver):
    # The test function that uses a WebDriver fixture named `driver`.

    wait = WebDriverWait(driver, 20)  # Create an explicit wait object with a 20 second timeout

    # Step 1: Open Flights Page
    driver.get(BASE_URL + "flights/")  # Navigate to the flights page using the base URL

    # Step 2: Click Book Now
    book_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[contains(text(),'Book Now')])[1]")
        )
    )  # Wait for the first Book Now button to appear in the page DOM
    driver.execute_script("arguments[0].click();", book_btn)  # Click the button using JavaScript

    # Step 3: Verify login
    assert "login" in driver.current_url.lower()  # Confirm the browser navigated to a login page

    # Step 4: Click SignUp
    signup_link = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "SignUp"))
    )  # Wait for the SignUp link to be present
    driver.execute_script("arguments[0].click();", signup_link)  # Click the SignUp link using JS

    # Step 5: Signup
    signup = SignupPage(driver)  # Instantiate the SignupPage object for signup actions
    email = f"testuser{int(time.time())}@gmail.com"  # Generate a unique email with the current timestamp
    signup.signup("Test User", email, "Sundar@123")  # Perform signup using the page object

    # Step 6: Wait for seat page
    wait.until(EC.url_contains("seat-selection"))  # Wait until the URL contains seat-selection

    # Choose the first available seat
    seat = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(@class,'seat')])[1]")
        )
    )  # Wait for the first seat element to be present

    driver.execute_script("""
        var evt = new MouseEvent('click', {
            bubbles: true,
            cancelable: true,
            view: window
        });
        arguments[0].dispatchEvent(evt);
    """, seat)  # Dispatch a JS click event on the seat element

    time.sleep(2)  # Pause briefly to allow the UI to update after seat selection

    # Step 7: Click Add Passengers
    add_passenger_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Add Passengers')]")
        )
    )  # Wait for the Add Passengers button
    driver.execute_script("arguments[0].click();", add_passenger_btn)  # Click Add Passengers via JS

    # Handle alert if it appears
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait up to 5 seconds for an alert
        alert = driver.switch_to.alert  # Switch to the alert popup
        print("Alert:", alert.text)  # Print the alert text for debugging
        alert.accept()  # Accept the alert
        return  # End the test early if the alert is shown

    except:
        pass  # If no alert is present, continue execution

    # Step 8: Add Passenger
    add_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Add Passenger')]")
        )
    )  # Wait for the Add Passenger button
    driver.execute_script("arguments[0].click();", add_btn)  # Click the Add Passenger button
