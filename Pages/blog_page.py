import time
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Blog(BasePage):
    view_all = (By.XPATH , "//button[normalize-space()='View All']")
    logo = (By.XPATH , "//a[@class='navbar-brand']")

    def blog(self):
        self.scroll_down_only()
        self.click(By.XPATH, "//button[normalize-space()='View All']")
        assert self.driver.current_url == "https://www.nivalabs.ai/blogs"
        time.sleep(2)
        self.scroll_until_element_found()
        self.scroll_up_only()
        blogs = [
            {
                "title": "Pandas Profiling: Automated Data Insights in Python",
                "url": "https://www.nivalabs.ai/blogs/pandas-profiling-automated-data-insights-in-python"
            },
            {
                "title": "AI Agent in a Nutshell: Quick Implementation with Python",
                "url": "https://www.nivalabs.ai/blogs/ai-agent-in-a-nutshell-quick-implementation-with-p"
            }
        ]
        for blog in blogs:
            self.click(By.XPATH, f"//a[contains(text(),'{blog['title']}')]")
            self.scroll_up_down()
            assert self.driver.current_url == blog["url"]
            self.driver.back()

        self.click(By.XPATH,"//a[@class='navbar-brand']")
