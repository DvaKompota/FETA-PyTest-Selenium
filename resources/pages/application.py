from resources.pages.base_page import BasePage
from resources.pages.home_page import HomePage
from resources.pages.women_page import WomenPage
from resources.pages.dresses_page import DressesPage
from resources.pages.tshirts_page import TshirtsPage
from resources.pages.search_page import SearchPage
from resources.pages.auth_page import AuthenticationPage
from resources.pages.create_account_page import CreateAccountPage
from resources.pages.my_account_page import MyAccountPage


class Application:

    def __init__(self, app_data):
        self.base_page = BasePage(app_data)
        self.home_page = HomePage(app_data)
        self.women_page = WomenPage(app_data)
        self.dresses_page = DressesPage(app_data)
        self.tshirts_page = TshirtsPage(app_data)
        self.search_page = SearchPage(app_data)
        self.auth_page = AuthenticationPage(app_data)
        self.create_account_page = CreateAccountPage(app_data)
        self.my_account_page = MyAccountPage(app_data)
