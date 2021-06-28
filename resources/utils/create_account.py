from resources.utils.file_ops import generate_customer


def create_account(app):
    page = app.home_page
    customer = generate_customer(page.data['test_customer'])
    page.open_home_page()
    page.click(page.sign_in_button)
    page = app.auth_page
    page.wait_element_displayed(page.auth_heading)
    page.enter_text(page.create_account_email_field, customer['email'])
    page.click(page.create_account_button)
    page = app.create_account_page
    page.wait_element_displayed(page.create_account_heading)
    [page.wait_element_displayed(element) for element in page.create_account_happy_elements]
    page.enter_text(page.pi_first_name_field, customer['first_name'])
    page.enter_text(page.pi_last_name_field, customer['last_name'])
    page.enter_text(page.pi_password_field, customer['password'])
    page.enter_text(page.address_address1_field, customer['address1'])
    page.enter_text(page.address_city_field, customer['city'])
    page.select_item_from_dropdown(customer["state"], page.address_state_menu)
    page.enter_text(page.address_zip_field, customer['zip_code'])
    page.enter_text(page.address_phone_field, customer['phone'])
    page.click(page.register_button)
    page = app.my_account_page
    page.wait_element_displayed(page.my_account_heading)
    page.click(page.sign_out_button)
    page.wait_element_displayed(app.auth_page.auth_heading)
