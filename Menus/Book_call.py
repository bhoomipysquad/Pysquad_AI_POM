import time
from selenium.webdriver.common.by import By


class Book_Call:
    def __init__(self,driver):
        self.driver = driver

    #to click on menus using forloop
    def to_click_on_menu(self):
      all_menu = {
               "AI_Agent_xpath" : "//button[normalize-space()='AI Agent']",
               "RAG_Xpath" : "//button[normalize-space()='RAG']",
               "AI_Service_xpath" : "//button[normalize-space()='AI Service']",
               "pysquad_logo_xpath" : "//img[@alt='Logo']",
               "Automation_xpath" : "//button[normalize-space()='Automation']",
               "Arrow_xpath" : "//img[@alt='scrollNext_image']"
                 }
      for menu, xpath in all_menu.items():
             try:
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
                time.sleep(2)
             except Exception as e:
                  print(f"Error occurred while clicking {menu}: {e}")

    #to click on "Book a call" button
    Book_a_call_xpath = "//button[normalize-space()='Book a call']"
    def click_book_call(self):
        self.driver.find_element(By.XPATH,self.Book_a_call_xpath).click()
        time.sleep(2)




