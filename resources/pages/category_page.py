from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class CategoryPage(HomePage):

    subcategories_heading = (By.XPATH, '//*[@id="subcategories"]')
    product_list = (By.XPATH, '//*[@class="product_list grid row"]')
    left_column = (By.XPATH, '//*[@id="left_column"]')

    category_happy_elements = [subcategories_heading, product_list, left_column]
