from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class PaymentPage(HomePage):

    payment_heading = (By.XPATH, '//*[@class="page-heading"][.="Please choose your payment method"]')
    pay_by_wire_button = (By.XPATH, '//*[@class="bankwire"]')
    pay_by_check_button = (By.XPATH, '//*[@class="cheque"]')
