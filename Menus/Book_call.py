import time
from selenium.webdriver.common.by import By


class Book_Call:
    def __init__(self,driver):
        self.driver = driver

    #to click on "Book a call" button
    Book_a_call_xpath = "//button[normalize-space()='Book a call']"
    calendly_xpath = "//div[@class='HvybhIo63ZbBJxHh7Ann RK3ps09FjZwzHTaYDakl']"
    timezone_xpath = "//div[@class='tEuGaNZxLYHN3rpC1UNA xSnXLssjt6TA8zBk06Iq']"
    close_button_xpath = "//div[@class='calendly-popup-close']"
    pysquad_logo_xpath = "//img[@alt='Logo']"

    def click_book_call(self):
        self.driver.find_element(By.XPATH,self.Book_a_call_xpath).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, self.close_button_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pysquad_logo_xpath).click()
        time.sleep(2)