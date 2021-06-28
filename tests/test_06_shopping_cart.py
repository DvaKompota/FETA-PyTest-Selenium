import pytest


@pytest.mark.shopping_cart
class TestShoppingCart:

    def test_shopping_cart_page(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.cart_button)
        page = app.shopping_cart_page
        page.wait_element_displayed(page.cart_heading)
        assert all([page.is_displayed(element) for element in page.cart_happy_elements])

    def test_add_product_to_cart_via_widget(self, app):
        page = app.home_page
        page.open_home_page()
        assert "empty" in page.get_element_text(page.cart_button)
        assert "1" not in page.get_element_text(page.cart_button)
        page.hover_to_product(1)
        page.add_product_to_cart(1)
        page.click(page.cart_overlay_close)
        assert "empty" not in page.get_element_text(page.cart_button)
        assert "1" in page.get_element_text(page.cart_button)
        page.hover_to(page.cart_button)
        assert page.is_displayed(page.cart_product_item)
        page.click(page.cart_checkout_button)
        page = app.shopping_cart_page
        page.wait_element_displayed(page.cart_heading)
        page.wait_element_displayed(page.cart_summary)
        assert page.get_cart_products_count() == 1
        assert page.get_cart_product_name(1)
        assert page.get_cart_product_quantity(1) == 1
        unit_price = page.get_cart_product_unit_price(1)
        total_price = page.get_cart_product_total_price(1)
        total_products_price = page.get_cart_total_products_price()
        total_shipping_price = page.get_cart_total_shipping_price()
        total_price_no_tax = page.get_cart_total_price_no_tax()
        total_tax = page.get_cart_tax()
        total = page.get_cart_total()
        assert unit_price == total_price == total_products_price
        assert total_price_no_tax == total_products_price + total_shipping_price
        assert total == total_price_no_tax + total_tax
        assert page.is_displayed(page.checkout_button)
        page.delete_product_from_cart(1)
        page.open_home_page()

    def test_add_product_to_cart_via_overlay(self, app):
        page = app.home_page
        page.open_home_page()
        assert "empty" in page.get_element_text(page.cart_button)
        assert "1" not in page.get_element_text(page.cart_button)
        page.hover_to_product(1)
        page.add_product_to_cart(1)
        page.click(page.cart_overlay_checkout_button)
        page = app.shopping_cart_page
        page.wait_element_displayed(page.cart_heading)
        page.wait_element_displayed(page.cart_summary)
        assert page.get_cart_products_count() == 1
        assert page.get_cart_product_name(1)
        assert page.get_cart_product_quantity(1) == 1
        unit_price = page.get_cart_product_unit_price(1)
        total_price = page.get_cart_product_total_price(1)
        total_products_price = page.get_cart_total_products_price()
        total_shipping_price = page.get_cart_total_shipping_price()
        total_price_no_tax = page.get_cart_total_price_no_tax()
        total_tax = page.get_cart_tax()
        total = page.get_cart_total()
        assert unit_price == total_price == total_products_price
        assert total_price_no_tax == total_products_price + total_shipping_price
        assert total == total_price_no_tax + total_tax
        assert page.is_displayed(page.checkout_button)
        page.delete_product_from_cart(1)
        page.open_home_page()

    def test_add_product_to_cart_via_product_card(self, app):
        page = app.home_page
        page.open_home_page()
        assert "empty" in page.get_element_text(page.cart_button)
        assert "1" not in page.get_element_text(page.cart_button)
        page.click_on_product_img_link(1)
        page = app.product_page
        [page.wait_element_displayed(element) for element in page.product_happy_elements]
        page.click(page.product_add_to_cart_button)
        page.click(page.cart_overlay_checkout_button)
        page = app.shopping_cart_page
        page.wait_element_displayed(page.cart_heading)
        page.wait_element_displayed(page.cart_summary)
        assert page.get_cart_products_count() == 1
        assert page.get_cart_product_name(1)
        assert page.get_cart_product_quantity(1) == 1
        unit_price = page.get_cart_product_unit_price(1)
        total_price = page.get_cart_product_total_price(1)
        total_products_price = page.get_cart_total_products_price()
        total_shipping_price = page.get_cart_total_shipping_price()
        total_price_no_tax = page.get_cart_total_price_no_tax()
        total_tax = page.get_cart_tax()
        total = page.get_cart_total()
        assert unit_price == total_price == total_products_price
        assert total_price_no_tax == total_products_price + total_shipping_price
        assert total == total_price_no_tax + total_tax
        assert page.is_displayed(page.checkout_button)
        page.delete_product_from_cart(1)
        page.open_home_page()
