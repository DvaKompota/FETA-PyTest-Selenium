from os.path import join
import pytest
from resources.utils.file_ops import get_yaml


@pytest.mark.base_page
class TestBasePage:

    def test_page_inheritance(self, app):
        assert app.base_page.locator_example
        assert app.home_page.header
        assert app.home_page.footer

    def test_open_url(self, app):
        app.base_page.open_url('https://www.google.com/')
        assert app.base_page.get_title()

    def test_page_has_test_data(self, app):
        relative_path_from_here_to_yaml = join("..", "..", "resources", "test_data", 'data.yaml')
        data = get_yaml(__file__, relative_path_from_here_to_yaml)
        assert app.base_page.data['test_customer']['first_name'] == data['test_customer']['first_name']
