from resources.pages.base_page import BasePage
from resources.pages.home_page import HomePage
from resources.pages.women_page import WomenPage
from resources.pages.dresses_page import DressesPage


class Application:

    def __init__(self, app_data):
        self.base_page = BasePage(app_data)
        self.home_page = HomePage(app_data)
        self.women_page = WomenPage(app_data)
        self.dresses_page = DressesPage(app_data)
