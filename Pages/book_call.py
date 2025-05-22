import time
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Book_Call(BasePage):
    book_call_button = (By.XPATH , "//button[normalize-space()='Book a call']")
    close_button = (By.XPATH , "//div[@class='calendly-popup-close']")

    def book_call(self):
        self.click(*self.book_call_button)
        time.sleep(5)
        self.click(*self.close_button)
