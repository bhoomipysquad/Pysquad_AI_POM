import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Hover_Check(BasePage):
    solutions_link = (By.XPATH  , "//a[normalize-space()='solutions@nivalabs.ai']")
    strategy_design = (By.XPATH,"//h1[normalize-space()='Comprehensive AI Strategy & Solution Design']")
    agile_development = (By.XPATH , "//h1[normalize-space()='Agile AI Development & Seamless Integration']")
    deployment_support = (By.XPATH , "//h1[normalize-space()='AI Deployment, Optimization & Continuous Support']")

    def solutions_url(self):
        self.scroll_by_pixels()
        self.click(By.XPATH , "//a[normalize-space()='solutions@nivalabs.ai']")
        time.sleep(2)
        self.switch_to_parent_window()


    def hover_over_menu(self):
        self.scroll_for_hover()
        actions = ActionChains(self.driver)
        elements = [
                        self.driver.find_element(*self.strategy_design),
                        self.driver.find_element(*self.agile_development),
                        self.driver.find_element(*self.deployment_support)
                    ]
        for element in elements:
            actions.move_to_element(element).perform()
            time.sleep(1)


    def open_social_media_pages(self):
         self.scroll_down_only()
         social_media_links = {
                                 "Instagram": {
                                                 "xpath": "//a[contains(@aria-label,'Instagram')]//*[name()='svg']",
                                                 "expected_url": "https://www.instagram.com/nivalabs.ai/"
                                              },
                                 "LinkedIn": {
                                                 "xpath": "//a[contains(@aria-label,'LinkedIn')]//*[name()='svg']",
                                                 "expected_url": "https://www.linkedin.com/company/nivalabs-ai/"
                                             },
                                 "Facebook": {
                                                 "xpath": "//a[@aria-label='Facebook']//*[name()='svg']",
                                                 "expected_url": "https://www.facebook.com/people/Nivalabs-AI/61575541688397/"
                                             }
                              }

         original_window = self.driver.current_window_handle
         for name, info in social_media_links.items():
             try:
                 element = self.driver.find_element(By.XPATH, info["xpath"])
                 element.click()
                 time.sleep(2)

                 windows = self.driver.window_handles
                 for window in windows:
                     if window != original_window:
                         self.driver.switch_to.window(window)
                         break

                 time.sleep(2)

                 act_url = self.driver.current_url
                 assert act_url.startswith(info["expected_url"]), f"{name} URL mismatch: {act_url}"

                 self.driver.close()

                 self.driver.switch_to.window(original_window)
                 time.sleep(2)

             except Exception as e:
                 print(f"Error occurred while clicking {name}: {e}")