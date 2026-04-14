# Import get_driver function to create a WebDriver instance
from utils.driver_factory import get_driver

# Basic test function to verify the application loads and title is correct
def test_open_site():
    # Create a new Chrome WebDriver instance using the factory function
    driver = get_driver()
    # Navigate to the application's home page using the full URL
    driver.get("https://9659058568.pythonanywhere.com/")
    
    # Assert that "TravelVerse" text appears in the page title
    assert "TravelVerse" in driver.title
    
    # Close the browser and quit the WebDriver instance
    driver.quit()