import pytest
import logging


@pytest.mark.home_page
class TestHomePage:

    def test_home_page_happy_elements(self, app):
        page = app.home_page
        page.open_home_page()
        assert all([page.is_displayed(element) for element in page.home_happy_elements])

    def test_home_page_women_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.women_section)
        page = app.women_page
        page.wait_element_displayed(page.heading_banner)
        assert all([page.is_displayed(element) for element in page.category_happy_elements])
        assert all([page.is_displayed(element) for element in page.women_happy_elements])

    def test_home_page_dresses_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.dresses_section)
        page = app.dresses_page
        page.wait_element_displayed(page.heading_banner)
        assert all([page.is_displayed(element) for element in page.category_happy_elements])
        assert all([page.is_displayed(element) for element in page.dresses_happy_elements])

    def test_home_page_tshirts_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.tshirts_section)
        page = app.tshirts_page
        page.wait_element_displayed(page.heading_banner)
        assert all([page.is_displayed(element) for element in [page.product_list, page.left_column]]) # no subcategories
        assert all([page.is_displayed(element) for element in page.tshirts_happy_elements])
