from resources.pages.base_page import BasePage
from resources.pages.home_page import HomePage
from resources.pages.women_page import WomenPage
from resources.pages.dresses_page import DressesPage
from resources.pages.tshirts_page import TshirtsPage
from resources.pages.search_page import SearchPage
from resources.pages.auth_page import AuthenticationPage
from resources.pages.create_account_page import CreateAccountPage
from resources.pages.my_account_page import MyAccountPage
from resources.pages.shopping_cart_page import ShoppingCartPage
from resources.pages.product_page import ProductPage
from resources.pages.addresses_page import AddressesPage
from resources.pages.shipping_page import ShippingPage
from resources.pages.payment_page import PaymentPage
from resources.pages.order_summary_page import OrderSummaryPage
from resources.pages.order_confirmation_page import OrderConfirmationPage


class Application:
    """Returns an object, containing all the Page Objects of the web application under test.

    Includes BasePage with all its standard methods (get_element, is_displayed, click, etc.)
    and all the child page objects (HomePage, ProductPage, ShoppingCartPage, etc.)
    with all their locators (header, search_bar, product_name, footer, etc.)
    and specific methods (get_product_name, add_product_to_cart, etc.)
    """

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
        self.shopping_cart_page = ShoppingCartPage(app_data)
        self.product_page = ProductPage(app_data)
        self.addresses_page = AddressesPage(app_data)
        self.shipping_page = ShippingPage(app_data)
        self.payment_page = PaymentPage(app_data)
        self.order_summary_page = OrderSummaryPage(app_data)
        self.order_confirmation_page = OrderConfirmationPage(app_data)
