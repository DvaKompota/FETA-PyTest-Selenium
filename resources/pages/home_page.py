from selenium.webdriver.remote.webelement import By
from .base_page import BasePage


class HomePage(BasePage):

    header = (By.XPATH, '//*[@id="header"]')
    sign_in_button = (By.XPATH, '//*[@class="login"]')
    sign_out_button = (By.XPATH, '//*[@class="logout"]')
    account_button = (By.XPATH, '//*[@class="account"]')

    search_bar = (By.XPATH, '//*[@id="search_query_top"]')
    search_button = (By.XPATH, '//button[@name="submit_search"]')

    cart_block = (By.XPATH, '//*[@class="shopping_cart"]')
    cart_button = (By.XPATH, f'{cart_block[1]}/a')
    cart_product_list = (By.XPATH, f'{cart_block[1]}//*[@class="products"]')
    cart_product_item = (By.XPATH, f'{cart_product_list[1]}//*[contains(@data-id, "cart_block_product")]')
    cart_checkout_button = (By.XPATH, f'{cart_block[1]}//*[@id="button_order_cart"]')

    top_menu = (By.XPATH, '//*[@id="block_top_menu"]')
    women_section = (By.XPATH, f'{top_menu[1]}//a[@title="Women"]')
    dresses_section = (By.XPATH, f'{top_menu[1]}/ul/li/a[@title="Dresses"]')
    tshirts_section = (By.XPATH, f'{top_menu[1]}/ul/li/a[@title="T-shirts"]')

    homefeatured_list = (By.XPATH, '//*[@id="homefeatured"]')
    product_container_xpath = '//*[@class="product-container"]'
    product_img_link_xpath = '//*[@class="product_img_link"]'
    product_name_xpath = '//*[@class="product-name"]'
    product_price_xpath = '//*[@class="price"]'
    add_to_cart_button_xpath = '//a[@title="Add to cart"]'

    cart_overlay = (By.XPATH, '//*[@id="layer_cart"]')
    cart_overlay_checkout_button = (By.XPATH, '//*[@class="clearfix"]//*[@title="Proceed to checkout"]')
    cart_overlay_close = (By.XPATH, f'{cart_overlay[1]}//*[@title="Close window"]')

    facebook_button = (By.XPATH, '//*[@class="facebook"]')
    twitter_button = (By.XPATH, '//*[@class="twitter"]')
    youtube_button = (By.XPATH, '//*[@class="youtube"]')
    google_button = (By.XPATH, '//*[@class="google-plus"]')
    footer = (By.XPATH, '//*[@id="footer"]')

    home_happy_elements = [header, sign_in_button, search_bar, cart_button, top_menu, women_section, dresses_section,
                           tshirts_section, facebook_button, twitter_button, youtube_button, google_button, footer]

    def add_product_to_cart(self, product_number):
        product_container_xpath = f'({self.product_container_xpath})[{product_number}]'
        add_to_cart_button = (By.XPATH, f'{product_container_xpath}{self.add_to_cart_button_xpath}')
        self.click(add_to_cart_button)

    def click_on_product_img_link(self, product_number):
        product_container_xpath = f'({self.product_container_xpath})[{product_number}]'
        product_img_link = (By.XPATH, f'{product_container_xpath}{self.product_img_link_xpath}')
        self.click(product_img_link)

    def get_featured_products_count(self):
        self.wait_element_displayed(self.homefeatured_list)
        products = self.driver.find_elements_by_xpath(f'{self.homefeatured_list[1]}{self.product_container_xpath}')
        return len(products)

    def get_product_name(self, product_number):
        product_container_xpath = f'({self.product_container_xpath})[{product_number}]'
        product_name_xpath = f'{product_container_xpath}{self.product_name_xpath}'
        product_name = self.get_element_text((By.XPATH, product_name_xpath))
        return product_name

    def hover_to_product(self, product_number):
        product_container_xpath = f'({self.product_container_xpath})[{product_number}]'
        self.hover_to((By.XPATH, product_container_xpath))

    def open_home_page(self):
        self.open_url(self.data['home_url'])
        self.wait_element_displayed(self.header)
