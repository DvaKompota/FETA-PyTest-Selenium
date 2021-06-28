from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class ProductPage(HomePage):

    product_big_pic = (By.XPATH, '//*[@id="bigpic"]')
    product_name = (By.XPATH, '//*[@itemprop="name"]')
    product_price = (By.XPATH, '//*[@id="our_price_display"]')
    product_quantity = (By.XPATH, '//*[@id="quantity_wanted"]')
    product_quantity_plus = (By.XPATH, '//*[contains(@class, "product_quantity_up")]')
    product_quantity_minus = (By.XPATH, '//*[contains(@class, "product_quantity_down")]')
    product_size_select = (By.XPATH, '//select[@id="group_1"]')
    product_add_to_cart_button = (By.XPATH, '//*[@id="add_to_cart"]/button')

    product_happy_elements = [product_big_pic, product_name, product_price, product_quantity, product_quantity_plus,
                              product_quantity_minus, product_add_to_cart_button]
