import time
from selenium.webdriver.common.by import By


class Social_Media:
    def __init__(self,driver):
        self.driver = driver

    #open social media pages using forloop
    def open_social_media_pages(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        social_media = { "Instagram_xpath" : "//a[contains(@aria-label,'Instagram')]//*[name()='svg']",
                         "Linked_in_xpath" : "//a[contains(@aria-label,'LinkedIn')]//*[name()='svg']",
                         "Twitter_xpath" : "//a[@aria-label='Twitter']//*[name()='svg']"
                        }

        for menu, xpath in social_media.items():
           try:
               element = self.driver.find_element(By.XPATH, xpath)
               element.click()
               time.sleep(2)
               original_window = self.driver.window_handles[0]
               new_window = self.driver.window_handles[1]
               self.driver.switch_to.window(new_window)
               time.sleep(2)
               self.driver.close()
               self.driver.switch_to.window(original_window)
               time.sleep(2)
           except Exception as e:
               print(f"Error occurred while clicking {menu}: {e}")