import time
from Test.conftest import Base_url


# to check the Base URL is successfully opened or not
def test_conftest(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    assert driver.current_url == Base_url


