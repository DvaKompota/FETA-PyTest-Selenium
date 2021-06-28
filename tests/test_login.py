import pytest
from resources.utils.file_ops import generate_customer
from resources.utils.create_account import create_account


@pytest.mark.login
class TestLogin:

    def test_create_account(self, app):
        page = app.home_page
        customer = generate_customer(page.data['test_customer'])
        page.open_home_page()
        page.click(page.sign_in_button)
        page = app.auth_page
        page.wait_element_displayed(page.auth_heading)
        assert all([page.is_displayed(element) for element in page.home_happy_elements])
        assert all([page.is_displayed(element) for element in page.auth_happy_elements])
        page.enter_text(page.create_account_email_field, customer['email'])
        page.click(page.create_account_button)
        page = app.create_account_page
        page.wait_element_displayed(page.create_account_heading)
        [page.wait_element_displayed(element) for element in page.create_account_happy_elements]
        assert all([page.is_displayed(element) for element in page.create_account_happy_elements])
        # First name
        page.enter_text(page.pi_first_name_field, customer['first_name'])
        assert page.get_element_attribute(page.pi_first_name_field, "value") == customer['first_name']
        assert page.get_element_attribute(page.address_first_name_field, "value") == customer['first_name']
        # Last name
        page.enter_text(page.pi_last_name_field, customer['last_name'])
        assert page.get_element_attribute(page.pi_last_name_field, "value") == customer['last_name']
        assert page.get_element_attribute(page.address_last_name_field, "value") == customer['last_name']
        # Email
        assert page.get_element_attribute(page.pi_email_field, "value") == customer['email']
        # Password
        page.enter_text(page.pi_password_field, customer['password'])
        assert page.get_element_attribute(page.pi_password_field, "value") == customer['password']
        # Address1
        page.enter_text(page.address_address1_field, customer['address1'])
        assert page.get_element_attribute(page.address_address1_field, "value") == customer['address1']
        # City
        page.enter_text(page.address_city_field, customer['city'])
        assert page.get_element_attribute(page.address_city_field, "value") == customer['city']
        # State
        page.select_item_from_dropdown(customer["state"], page.address_state_menu)
        assert page.get_element_text(page.address_state_value) == customer['state']
        # Zip code
        page.enter_text(page.address_zip_field, customer['zip_code'])
        assert page.get_element_attribute(page.address_zip_field, "value") == str(customer['zip_code'])
        # Phone
        page.enter_text(page.address_phone_field, customer['phone'])
        assert page.get_element_attribute(page.address_phone_field, "value") == str(customer['phone'])
        # Submit
        page.click(page.register_button)
        page = app.my_account_page
        page.wait_element_displayed(page.my_account_heading)
        # Validate My Account page
        assert all([page.is_displayed(element) for element in page.my_account_happy_elements])
        assert page.is_displayed(page.sign_out_button)
        assert not page.is_displayed(page.sign_in_button)
        assert page.is_displayed(page.account_button)
        assert page.get_element_text(page.account_button) == f'{customer["first_name"]} {customer["last_name"]}'
        page.click(page.sign_out_button)
        page.wait_element_displayed(app.auth_page.auth_heading)

    def test_login_with_valid_credentials(self, app):
        page = app.auth_page
        customer = page.data['test_customer']
        create_account(app) if '{placeholder}' in customer['email'] else None
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_email_field, customer['email'])
        page.enter_text(page.login_password_field, customer['password'])
        page.click(page.login_button)
        page = app.my_account_page
        page.wait_element_displayed(page.my_account_heading)
        assert all([page.is_displayed(element) for element in page.my_account_happy_elements])
        assert page.is_displayed(page.sign_out_button)
        assert not page.is_displayed(page.sign_in_button)
        assert page.is_displayed(page.account_button)
        assert page.get_element_text(page.account_button) == f'{customer["first_name"]} {customer["last_name"]}'
        page.click(page.sign_out_button)
        page.wait_element_displayed(app.auth_page.auth_heading)

    def test_login_with_invalid_credentials(self, app):
        page = app.auth_page
        customer = page.data['test_customer']
        create_account(app) if '{placeholder}' in customer['email'] else None
        # Trying to login with empty email
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_password_field, customer['password'])
        page.click(page.login_button)
        page.wait_element_displayed(page.login_alert)
        assert "An email address required." in page.get_element_text(page.login_alert)
        # Trying to login with empty password
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_email_field, customer['email'])
        page.click(page.login_button)
        page.wait_element_displayed(page.login_alert)
        assert "Password is required." in page.get_element_text(page.login_alert)
        # Trying to login with invalid email (no last character)
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_email_field, customer['email'][:-1])
        page.enter_text(page.login_password_field, customer['password'])
        page.click(page.login_button)
        page.wait_element_displayed(page.login_alert)
        assert "Authentication failed." in page.get_element_text(page.login_alert)
        # Trying to login with invalid email (no first character)
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_email_field, customer['email'][1:])
        page.enter_text(page.login_password_field, customer['password'])
        page.click(page.login_button)
        page.wait_element_displayed(page.login_alert)
        assert "Authentication failed." in page.get_element_text(page.login_alert)
        # Trying to login with invalid password (no last character)
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_email_field, customer['email'])
        page.enter_text(page.login_password_field, customer['password'][:-1])
        page.click(page.login_button)
        page.wait_element_displayed(page.login_alert)
        assert "Authentication failed." in page.get_element_text(page.login_alert)
        # Trying to login with invalid password (no first character)
        page.open_home_page()
        page.click(page.sign_in_button)
        page.wait_element_displayed(page.auth_heading)
        page.enter_text(page.login_email_field, customer['email'])
        page.enter_text(page.login_password_field, customer['password'][1:])
        page.click(page.login_button)
        page.wait_element_displayed(page.login_alert)
        assert "Authentication failed." in page.get_element_text(page.login_alert)
