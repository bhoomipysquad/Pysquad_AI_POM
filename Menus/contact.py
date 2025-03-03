import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Contact_Us:
    def __init__(self,driver):
        self.driver = driver

    #to open contact us page
    Contact_us_xpath = "//a[contains(@class,'text-white !text-sm')]"
    def click_contact_us(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -300);")
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.Contact_us_xpath).click()
        time.sleep(2)
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(2)

    # to hover over the text
    Comprehensive_AI_Strategy_xpath = "//h1[normalize-space()='Comprehensive AI Strategy & Solution Design']"
    Agile_AI_Development = "//h1[normalize-space()='Agile AI Development & Seamless Integration']"
    AI_Deployment = "//h1[normalize-space()='AI Deployment, Optimization & Continuous Support']"

    def hover_over_event(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        actions = ActionChains(self.driver)
        first_menu = actions.move_to_element(self.driver.find_element(By.XPATH,self.Comprehensive_AI_Strategy_xpath))
        first_menu.perform()
        time.sleep(1)
        second_menu = actions.move_to_element(self.driver.find_element(By.XPATH,self.Agile_AI_Development))
        second_menu.perform()
        time.sleep(1)
        third_menu = actions.move_to_element(self.driver.find_element(By.XPATH,self.AI_Deployment))
        third_menu.perform()
        time.sleep(1)



