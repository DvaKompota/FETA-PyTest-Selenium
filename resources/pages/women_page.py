from selenium.webdriver.remote.webelement import By
from .category_page import CategoryPage


class WomenPage(CategoryPage):

    heading_banner = (By.XPATH, '//*[@class="category-name"][contains(text(), "Women")]')
    section_heading = (By.XPATH, '//*[@class="cat-name"][contains(text(), "Women")]')

    women_happy_elements = [heading_banner, section_heading]
