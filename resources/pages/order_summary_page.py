from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class OrderSummaryPage(HomePage):

    order_summary_heading = (By.XPATH, '//*[@class="page-heading"][contains(., "Order summary")]')
    confirm_order_button = (By.XPATH, '//button[@type="submit"]/*[.="I confirm my order"]/..')
