import pytest
import logging


@pytest.mark.home_page
class TestHomePage:

    def test_home_page_happy_elements(self, app):
        page = app.home_page
        page.open_home_page()
        assert all([page.is_displayed(element) for element in page.happy_elements])
