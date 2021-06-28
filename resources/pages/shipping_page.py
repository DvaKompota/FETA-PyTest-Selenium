from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class ShippingPage(HomePage):

    shipping_heading = (By.XPATH, '//*[@class="page-heading"][.="Shipping"]')
    shipping_terms_check = (By.XPATH, '//*[@id="uniform-cgv"]')
    shipping_terms_error = (By.XPATH, '//*[@class="fancybox-error"]')
    shipping_terms_error_close = (By.XPATH, '//*[@title="Close"]')
    checkout_button = (By.XPATH, '//*[@name="processCarrier"]')
