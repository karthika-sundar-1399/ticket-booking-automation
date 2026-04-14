# Import pytest module for test configuration and fixtures
import pytest
# Import the get_driver function from driver_factory module to create WebDriver instance
from utils.driver_factory import get_driver


# Define a pytest fixture called 'driver' that will be available to all test functions
@pytest.fixture
def driver():
    # Call get_driver() to initialize a new WebDriver instance
    driver = get_driver()
    # Yield the driver to the test function so it can use it
    # After the test completes, the code after 'yield' will execute (teardown)
    yield driver
    # Close the browser and quit the WebDriver instance
    driver.quit()


# Define a pytest hook that runs after each test to capture screenshots on failure
# hookwrapper=True allows this hook to wrap around the test execution
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Yield execution to the test/hook and capture the outcome
    outcome = yield
    # Get the result/report from the test execution
    rep = outcome.get_result()

    # Check if this is the actual test call (not setup/teardown) and if the test failed
    if rep.when == "call" and rep.failed:
        # Try to get the driver instance from the test function's arguments
        driver = item.funcargs.get("driver")
        # If driver exists, take a screenshot and save it with the test name
        if driver:
            # Save a screenshot to the reports folder with the test name for evidence
            driver.save_screenshot(f"reports/{item.name}.png")