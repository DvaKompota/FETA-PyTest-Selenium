from selenium.webdriver.remote.webelement import By


class BasePage:

    locator_example = (By.XPATH, 'some_xpath')

    def __init__(self, app_data):
        self.driver = app_data['driver']
        self.data = app_data['data']

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
