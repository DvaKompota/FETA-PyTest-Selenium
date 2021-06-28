import pytest
from resources.utils.create_account import create_account


@pytest.mark.checkout
class TestCheckout:

    def test_checkout_for_logged_in_customer_pay_by_wire(self, app):
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
        page.open_home_page()
        page.hover_to_product(1)
        page.add_product_to_cart(1)
        page.click(page.cart_overlay_checkout_button)
        page = app.shopping_cart_page
        page.wait_element_displayed(page.cart_heading)
        page.click(page.checkout_button)
        page = app.addresses_page
        page.wait_element_displayed(page.addresses_heading)
        page.click(page.checkout_button)
        page = app.shipping_page
        page.wait_element_displayed(page.shipping_heading)
        page.click(page.checkout_button)
        page.wait_element_displayed(page.shipping_terms_error)
        assert "You must agree to the terms of service" in page.get_element_text(page.shipping_terms_error)
        page.click(page.shipping_terms_error_close)
        page.click(page.shipping_terms_check)
        page.click(page.checkout_button)
        page = app.payment_page
        page.wait_element_displayed(page.payment_heading)
        page.click(page.pay_by_wire_button)
        page = app.order_summary_page
        page.wait_element_displayed(page.order_summary_heading)
        page.click(page.confirm_order_button)
        page = app.order_confirmation_page
        page.wait_element_displayed(page.order_confirmation_heading)
        page.click(page.sign_out_button)
        page.wait_element_displayed(app.auth_page.auth_heading)

    def test_checkout_for_logged_in_customer_pay_by_check(self, app):
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
        page.open_home_page()
        page.hover_to_product(1)
        page.add_product_to_cart(1)
        page.click(page.cart_overlay_checkout_button)
        page = app.shopping_cart_page
        page.wait_element_displayed(page.cart_heading)
        page.click(page.checkout_button)
        page = app.addresses_page
        page.wait_element_displayed(page.addresses_heading)
        page.click(page.checkout_button)
        page = app.shipping_page
        page.wait_element_displayed(page.shipping_heading)
        page.click(page.checkout_button)
        page.wait_element_displayed(page.shipping_terms_error)
        assert "You must agree to the terms of service" in page.get_element_text(page.shipping_terms_error)
        page.click(page.shipping_terms_error_close)
        page.click(page.shipping_terms_check)
        page.click(page.checkout_button)
        page = app.payment_page
        page.wait_element_displayed(page.payment_heading)
        page.click(page.pay_by_check_button)
        page = app.order_summary_page
        page.wait_element_displayed(page.order_summary_heading)
        page.click(page.confirm_order_button)
        page = app.order_confirmation_page
        page.wait_element_displayed(page.order_confirmation_heading)
        page.click(page.sign_out_button)
        page.wait_element_displayed(app.auth_page.auth_heading)
