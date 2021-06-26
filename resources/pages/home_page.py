from selenium.webdriver.remote.webelement import By
from .base_page import BasePage


class HomePage(BasePage):

    header = (By.XPATH, '//*[@id="header"]')
    sign_in_button = (By.XPATH, '//*[@class="login"]')
    search_bar = (By.XPATH, '//*[@id="search_query_top"]')
    shopping_cart = (By.XPATH, '//*[@class="shopping_cart"]')
    top_menu = (By.XPATH, '//*[@id="block_top_menu"]')
    women_section = (By.XPATH, f'{top_menu[1]}//a[@title="Women"]')
    dresses_section = (By.XPATH, f'{top_menu[1]}/ul/li/a[@title="Dresses"]')
    tshirts_section = (By.XPATH, f'{top_menu[1]}/ul/li/a[@title="T-shirts"]')

    facebook_button = (By.XPATH, '//*[@class="facebook"]')
    twitter_button = (By.XPATH, '//*[@class="twitter"]')
    youtube_button = (By.XPATH, '//*[@class="youtube"]')
    google_button = (By.XPATH, '//*[@class="google-plus"]')
    footer = (By.XPATH, '//*[@id="footer"]')

    happy_elements = [header, sign_in_button, search_bar, shopping_cart, top_menu, women_section, dresses_section,
                      tshirts_section, facebook_button, twitter_button, youtube_button, google_button, footer]

    def open_home_page(self):
        self.open_url(self.data['home_url'])
        self.wait_element_displayed(self.header)
