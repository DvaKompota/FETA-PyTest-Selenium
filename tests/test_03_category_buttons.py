import pytest


@pytest.mark.category_buttons
class TestCategoryButtons:

    def test_women_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.women_section)
        page = app.women_page
        page.wait_element_displayed(page.heading_banner)
        assert all([page.is_displayed(element) for element in page.category_happy_elements])
        assert all([page.is_displayed(element) for element in page.women_happy_elements])

    def test_dresses_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.dresses_section)
        page = app.dresses_page
        page.wait_element_displayed(page.heading_banner)
        assert all([page.is_displayed(element) for element in page.category_happy_elements])
        assert all([page.is_displayed(element) for element in page.dresses_happy_elements])

    def test_tshirts_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.tshirts_section)
        page = app.tshirts_page
        page.wait_element_displayed(page.heading_banner)
        assert all([page.is_displayed(element) for element in [page.product_list, page.left_column]]) # no subcategories
        assert all([page.is_displayed(element) for element in page.tshirts_happy_elements])
