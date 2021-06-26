from selenium.webdriver.remote.webelement import By
from .category_page import CategoryPage


class DressesPage(CategoryPage):

    heading_banner = (By.XPATH, '//*[@class="category-name"][contains(text(), "Dresses")]')
    section_heading = (By.XPATH, '//*[@class="cat-name"][contains(text(), "Dresses")]')

    dresses_happy_elements = [heading_banner, section_heading]
