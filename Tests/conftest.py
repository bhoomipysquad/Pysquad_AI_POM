import time
import pytest
from selenium import webdriver

Base_url = "https://www.nivalabs.ai/"

@pytest.fixture()
def open_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Base_url)
    time.sleep(2)
    yield driver
    driver.quit()
