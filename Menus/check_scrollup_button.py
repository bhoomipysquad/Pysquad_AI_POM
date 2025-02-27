import time
from selenium.webdriver.common.by import By


class Check_ScrollUp_Button:
    def __init__(self,driver):
        self.driver = driver

    #to check scrollup button
    scroll_up_button_xpath = "//*[name()='path' and contains(@stroke,'currentCol')]"
    def check_scrollup_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.scroll_up_button_xpath).click()
        time.sleep(2)

