from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.ID, "submit")
    SUCCESSTEXT = (By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")
    
    def login(self, username, password):
        self.visit("https://practicetestautomation.com/practice-test-login/")
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.BUTTON)

    def get_error_message(self):
        return self.get_text((By.XPATH, "//*[@id='error']"))
    
    