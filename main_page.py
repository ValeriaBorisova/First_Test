from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://www.python.org"

    def search_input(self):
        return self.driver.find_element(By.NAME, "q")

    def open(self):
        self.driver.get(self.url)

    def seacrh(self, item: str):
        self.search_input().clear
        self.search_input().send_keys("python")
        self.search_input().send_keys(Keys.RETURN)

    def quit(self):
        self.driver.quit()

    def page_source(self):
        return self.driver.page_source
