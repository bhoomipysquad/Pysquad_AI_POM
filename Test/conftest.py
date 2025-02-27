import time
import pytest
from selenium import webdriver



Base_url = "https://ai.pysquad.com/"

#to open chrome and open URL
@pytest.fixture(scope="package")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Base_url)
    time.sleep(2)
    yield driver
    driver.quit()

