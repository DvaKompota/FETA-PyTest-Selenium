from selenium.webdriver.remote.webelement import By
from .home_page import HomePage


class AuthenticationPage(HomePage):

    auth_heading = (By.XPATH, '//*[@class="page-heading"][.="Authentication"]')
    create_account_form = (By.XPATH, '//*[@id="create-account_form"]')
    create_account_email_field = (By.XPATH, '//*[@id="email_create"]')
    create_account_button = (By.XPATH, '//*[@id="SubmitCreate"]')
    login_form = (By.XPATH, '//*[@id="login_form"]')
    login_email_field = (By.XPATH, '//*[@id="email"]')
    login_password_field = (By.XPATH, '//*[@id="passwd"]')
    forgot_password_link = (By.XPATH, '//*[@class="lost_password form-group"]/a')
    login_button = (By.XPATH, '//*[@id="SubmitLogin"]')
    login_alert = (By.XPATH, '//*[@id="center_column"]/*[@class="alert alert-danger"]')

    auth_happy_elements = [auth_heading, create_account_form, create_account_email_field, create_account_button,
                           login_form, login_email_field, login_password_field, forgot_password_link, login_button]
