from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class AddressesPage(HomePage):

    addresses_heading = (By.XPATH, '//*[@class="page-heading"][.="Addresses"]')
    checkout_button = (By.XPATH, '//*[@name="processAddress"]')
