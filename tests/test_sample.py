from utils.driver_factory import get_driver

def test_open_site():
    driver = get_driver()
    driver.get("https://9659058568.pythonanywhere.com/")
    
    assert "TravelVerse" in driver.title
    
    driver.quit()