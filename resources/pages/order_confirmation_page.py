from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class OrderConfirmationPage(HomePage):

    order_confirmation_heading = (By.XPATH, '//*[@class="page-heading"][.="Order confirmation"]')
