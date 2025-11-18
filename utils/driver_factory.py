from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser="chrome"):
    if browser == "chrome":
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception("Browser not supported")
