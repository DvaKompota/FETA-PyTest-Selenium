from selenium.webdriver.remote.webelement import By
from .base_page import BasePage


class HomePage(BasePage):

    header = (By.XPATH, '//*[@id="header"]')
    footer = (By.XPATH, '//*[@id="footer"]')
