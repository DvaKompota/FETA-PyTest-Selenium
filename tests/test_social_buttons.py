import pytest
import re


@pytest.mark.social_buttons
class TestSocialButtons:

    def test_facebook_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.facebook_button)
        page.switch_to_last_tab()
        assert page.get_current_url() == page.data['social_links']['facebook']

    def test_twitter_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.twitter_button)
        page.switch_to_last_tab()
        assert page.get_current_url() == page.data['social_links']['twitter']

    def test_youtube_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.youtube_button)
        page.switch_to_last_tab()
        assert page.get_current_url() == page.data['social_links']['youtube']

    def test_google_button(self, app):
        page = app.home_page
        page.open_home_page()
        page.click(page.google_button)
        page.switch_to_last_tab()
        # disabled because 1) google requires authorization; 2) Google+ doesn't support brand pages any more
        # assert page.get_current_url() == page.data['social_links']['google']
        group_no = re.search(r'\d*', page.data['social_links']['google'])[0]
        assert group_no in page.get_current_url()

