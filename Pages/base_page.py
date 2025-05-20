from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.click()
        time.sleep(2)

    def scroll_up_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def scroll_by_pixels(self):
        self.scroll_down_only()
        self.driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(2)

    def scroll_down_only(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_up_only(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def scroll_for_hover(self):
        self.scroll_down_only()
        self.driver.execute_script("window.scrollBy(0, -600);")
        time.sleep(2)

    def scroll_until_element_found(self):
        for i in range(50):  # Scroll down 50 times
            self.driver.execute_script("window.scrollBy(0, 100);")
            time.sleep(0.5)

    def switch_window(self):
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(2)

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
