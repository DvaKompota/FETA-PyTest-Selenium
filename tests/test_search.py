import pytest


@pytest.mark.search
class TestSearch:

    def test_search_exact(self, app):
        page = app.home_page
        page.open_home_page()
        search_string = page.data['search_strings']['exact']
        page.enter_text(page.search_bar, search_string)
        page.click(page.search_button)
        page = app.search_page
        page.wait_element_displayed(page.search_heading)
        assert page.get_search_results_count() == 1
        product_name = page.get_product_name(1)
        assert search_string in product_name

    def test_search_vague(self, app):
        page = app.home_page
        page.open_home_page()
        search_string = page.data['search_strings']['vague']
        page.enter_text(page.search_bar, search_string)
        page.click(page.search_button)
        page = app.search_page
        page.wait_element_displayed(page.search_heading)
        assert page.get_search_results_count() > 1
        # disabled for now, because vague search returns not only name matches, but also info from product description
        # for product_number in range(1, page.get_search_results_count() + 1):
        #     name = page.get_product_name(product_number)
        #     assert search_string.lower() in name.lower()

    def test_search_nothing(self, app):
        page = app.home_page
        page.open_home_page()
        search_string = page.data['search_strings']['nothing']
        page.enter_text(page.search_bar, search_string)
        page.click(page.search_button)
        page = app.search_page
        page.wait_element_displayed(page.search_heading)
        assert page.get_search_results_count() == 0
        assert page.is_displayed(page.search_results_alert)
        assert search_string in page.get_element_text(page.search_results_alert)
