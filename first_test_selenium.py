from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from main_page import MainPage

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
main_page = MainPage(driver)
main_page.open()
assert "Python" in driver.title
main_page.searh("python")
assert "No results found." not in driver.page_source()
main_page.quit()