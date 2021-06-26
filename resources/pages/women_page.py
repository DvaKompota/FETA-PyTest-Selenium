from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class WomenPage(HomePage):

    heading_banner = (By.XPATH, '//*[@class="category-name"][contains(text(), "Women")]')
    section_heading = (By.XPATH, '//*[@class="cat-name"][contains(text(), "Women")]')
    subcategories_heading = (By.XPATH, '//*[@id="subcategories"]')
    product_list = (By.XPATH, '//*[@class="product_list grid row"]')
    left_column = (By.XPATH, '//*[@id="left_column"]')

    women_happy_elements = [heading_banner, section_heading, subcategories_heading, product_list, left_column]

    def open_home_page(self):
        self.open_url(self.data['home_url'])
        self.wait_element_displayed(self.header)
