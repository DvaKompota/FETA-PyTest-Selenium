from selenium.webdriver.remote.webelement import By
from .home_page import HomePage
from decimal import Decimal
import re


class ShoppingCartPage(HomePage):

    cart_heading = (By.XPATH, '//*[@id="cart_title"]')
    cart_heading_counter = (By.XPATH, '//*[@class="heading-counter"]')
    order_steps_list = (By.XPATH, '//*[@id="order_step"]')
    cart_alert = (By.XPATH, '//*[@id="center_column"]/*[@class="alert alert-warning"]')

    cart_summary = (By.XPATH, '//*[@id="cart_summary"]')
    cart_summary_row_xpath = f'{cart_summary[1]}//tr[contains(@id, "product_")]'
    product_unit_price_xpath = '//*[@class="cart_unit"]'
    product_quantity_xpath = '//*[contains(@class, "cart_quantity_input")]'
    product_add_xpath = '//*[@title="Add"]'
    product_subtract_xpath = '//*[@title="Subtract"]'
    product_total_price_xpath = '//*[@class="cart_total"]'
    product_delete_xpath = '//*[@title="Delete"]'

    cart_total_products = (By.XPATH, '//*[@id="total_product"]')
    cart_total_shipping = (By.XPATH, '//*[@id="total_shipping"]')
    cart_total_price_no_tax = (By.XPATH, '//*[@id="total_price_without_tax"]')
    cart_tax = (By.XPATH, '//*[@id="total_tax"]')
    cart_total = (By.XPATH, '//*[@id="total_price"]')

    checkout_button = (By.XPATH, '//*[@class="cart_navigation clearfix"]//*[@title="Proceed to checkout"]')

    cart_happy_elements = [cart_heading, order_steps_list, cart_alert]

    def get_cart_products_count(self):
        self.wait_element_displayed(self.cart_heading_counter)
        text = self.get_element_text(self.cart_heading_counter)
        count = re.search(r'\d+', text)
        return int(count[0])

    def get_cart_product_name(self, product_number):
        product_row_xpath = f'({self.cart_summary_row_xpath})[{product_number}]'
        product_name_xpath = f'{product_row_xpath}{self.product_name_xpath}'
        product_name = self.get_element_text((By.XPATH, product_name_xpath))
        return product_name

    def get_cart_product_unit_price(self, product_number):
        product_row_xpath = f'({self.cart_summary_row_xpath})[{product_number}]'
        product_unit_price_xpath = f'{product_row_xpath}{self.product_unit_price_xpath}'
        product_unit_price = self.get_element_text((By.XPATH, product_unit_price_xpath)).replace("$", "")
        return Decimal(product_unit_price)

    def get_cart_product_quantity(self, product_number):
        product_row_xpath = f'({self.cart_summary_row_xpath})[{product_number}]'
        product_quantity_xpath = f'{product_row_xpath}{self.product_quantity_xpath}'
        product_quantity = self.get_element_attribute((By.XPATH, product_quantity_xpath), "value")
        return int(product_quantity)

    def delete_product_from_cart(self, product_number):
        product_row_xpath = f'({self.cart_summary_row_xpath})[{product_number}]'
        delete_product_xpath = f'{product_row_xpath}{self.product_delete_xpath}'
        self.click((By.XPATH, delete_product_xpath))

    def get_cart_product_total_price(self, product_number):
        product_row_xpath = f'({self.cart_summary_row_xpath})[{product_number}]'
        product_total_price_xpath = f'{product_row_xpath}{self.product_total_price_xpath}'
        product_total_price = self.get_element_text((By.XPATH, product_total_price_xpath)).replace("$", "")
        return Decimal(product_total_price)

    def get_cart_total_products_price(self):
        cart_total_products_price = self.get_element_text(self.cart_total_products).replace("$", "")
        return Decimal(cart_total_products_price)

    def get_cart_total_shipping_price(self):
        cart_total_shipping_price = self.get_element_text(self.cart_total_shipping).replace("$", "")
        return Decimal(cart_total_shipping_price)

    def get_cart_total_price_no_tax(self):
        cart_total_price_no_tax = self.get_element_text(self.cart_total_price_no_tax).replace("$", "")
        return Decimal(cart_total_price_no_tax)

    def get_cart_tax(self):
        cart_tax = self.get_element_text(self.cart_tax).replace("$", "")
        return Decimal(cart_tax)

    def get_cart_total(self):
        cart_total = self.get_element_text(self.cart_total).replace("$", "")
        return Decimal(cart_total)
