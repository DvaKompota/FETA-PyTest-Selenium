from selenium.webdriver.remote.webelement import By
from .home_page import HomePage
import re


class SearchPage(HomePage):

    search_heading = (By.XPATH, '//*[@class="page-heading  product-listing"]')
    search_heading_counter = (By.XPATH, '//*[@class="heading-counter"]')
    search_results_list = (By.XPATH, '//*[@class="product_list grid row"]')
    search_results_alert = (By.XPATH, '//*[@class="alert alert-warning"]')
    search_product_container_xpath = '//*[@class="product-container"]'
    search_product_name_xpath = '//*[@class="product-name"]'

    left_column = (By.XPATH, '//*[@id="left_column"]')

    category_happy_elements = [search_heading, search_results_list, left_column]

    def get_search_results_count(self):
        self.wait_element_displayed(self.search_heading_counter)
        text = self.get_element_text(self.search_heading_counter)
        count = re.search(r'\d*', text)
        return int(count[0])

    def get_product_name(self, product_number):
        product_container_xpath = f'({self.search_product_container_xpath})[{product_number}]'
        product_name_xpath = f'{product_container_xpath}{self.search_product_name_xpath}'
        product_name = self.get_element_text((By.XPATH, product_name_xpath))
        return product_name


