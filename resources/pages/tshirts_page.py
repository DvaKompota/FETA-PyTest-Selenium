from selenium.webdriver.remote.webelement import By
from .category_page import CategoryPage


class TshirtsPage(CategoryPage):

    heading_banner = (By.XPATH, '//*[@class="category-name"][contains(text(), "T-shirts")]')
    section_heading = (By.XPATH, '//*[@class="cat-name"][contains(text(), "T-shirts")]')

    tshirts_happy_elements = [heading_banner, section_heading]
