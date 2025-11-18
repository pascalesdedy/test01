from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    GREETING = (By.CLASS_NAME, "post-title")

    def get_greeting_text(self):
        return self.driver.find_element(*self.GREETING).text
