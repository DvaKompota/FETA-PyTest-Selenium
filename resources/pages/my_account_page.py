from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class MyAccountPage(HomePage):

    my_account_heading = (By.XPATH, '//*[@class="page-heading"][.="My account"]')

    orders_button = (By.XPATH, '//a[@title="Orders"]')
    credit_slips_button = (By.XPATH, '//a[@title="Credit slips"]')
    addresses_button = (By.XPATH, '//a[@title="Addresses"]')
    personal_info_button = (By.XPATH, '//a[@title="Information"]')
    wishlists_button = (By.XPATH, '//a[@title="My wishlists"]')

    my_account_happy_elements = [my_account_heading, orders_button, credit_slips_button, addresses_button,
                                 personal_info_button, wishlists_button]
