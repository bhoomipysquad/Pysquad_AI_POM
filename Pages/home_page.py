from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Home_page(BasePage):
    page_up_button  = (By.XPATH ,"//*[name()='path' and contains(@stroke,'currentCol')]")
    nivalabs_logo = (By.XPATH , "//a[@class='navbar-brand']")

    def check_page_scrolling(self):
        self.scroll_up_down()

    def check_page_up_button(self):
        self.scroll_down_only()
        self.click(By.XPATH , "//*[name()='path' and contains(@stroke,'currentCol')]")

    def check_logo(self):
        self.scroll_down_only()
        self.click(By.XPATH , "//a[@class='navbar-brand']")
