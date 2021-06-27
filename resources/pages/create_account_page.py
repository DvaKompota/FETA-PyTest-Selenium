from selenium.webdriver.remote.webelement import By
from .auth_page import AuthenticationPage


class CreateAccountPage(AuthenticationPage):

    create_account_heading = (By.XPATH, '//*[@class="page-heading"][.="Create an account"]')
    pi_first_name_field = (By.XPATH, '//*[@id="customer_firstname"]')
    pi_last_name_field = (By.XPATH, '//*[@id="customer_lastname"]')
    pi_email_field = (By.XPATH, '//*[@id="email"]')
    pi_password_field = (By.XPATH, '//*[@id="passwd"]')

    address_first_name_field = (By.XPATH, '//*[@id="firstname"]')
    address_last_name_field = (By.XPATH, '//*[@id="lastname"]')
    address_address1_field = (By.XPATH, '//*[@id="address1"]')
    address_address2_field = (By.XPATH, '//*[@id="address2"]')
    address_city_field = (By.XPATH, '//*[@id="city"]')
    address_state_container = (By.XPATH, '//*[@id="uniform-id_state"]')
    address_state_menu = (By.XPATH, '//*[@id="id_state"]')
    address_state_value = (By.XPATH, f'{address_state_container[1]}/span')
    address_state_item_xpath = f'{address_state_menu[1]}/option'
    address_zip_field = (By.XPATH, '//*[@id="postcode"]')
    address_country_container = (By.XPATH, '//*[@id="uniform-id_country"]')
    address_country_menu = (By.XPATH, '//*[@id="id_country"]')
    address_phone_field = (By.XPATH, '//*[@id="phone_mobile"]')
    address_alias_field = (By.XPATH, '//*[@id="alias"]')

    register_button = (By.XPATH, '//*[@id="submitAccount"]')

    create_account_happy_elements = [create_account_heading,
                                     pi_first_name_field, pi_last_name_field, pi_email_field, pi_password_field,
                                     address_first_name_field, address_last_name_field, address_address1_field,
                                     address_address2_field, address_city_field, address_state_container,
                                     address_zip_field, address_country_container, address_phone_field,
                                     address_alias_field, register_button]
