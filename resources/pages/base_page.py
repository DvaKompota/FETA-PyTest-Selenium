from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webelement import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from time import time, sleep


class BasePage:

    locator_example = (By.XPATH, 'some_xpath')

    def __init__(self, app_data):
        self.driver = app_data['driver']
        self.data = app_data['data']
        self.driver_wait = self.data['web_driver_settings']['wait_time']

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_element(self, locator, wait_time=None, poll_frequency=None) -> WebElement:
        if type(locator) is WebElement:
            return locator
        elif type(locator) is str:
            locator = getattr(self, locator)
        if poll_frequency:
            wait = WebDriverWait(self.driver, wait_time if wait_time else self.driver_wait, poll_frequency)
        else:
            wait = WebDriverWait(self.driver, wait_time if wait_time else self.driver_wait)
        return wait.until(EC.presence_of_element_located(locator), message=f'Element {locator} is not present')

    def is_displayed(self, locator):
        try:
            return self.get_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def wait_element_displayed(self, locator):
        wait = WebDriverWait(self.driver, self.driver_wait)
        try:
            wait.until(lambda driver: self.get_element(locator).is_displayed())
        except StaleElementReferenceException:
            sleep(0.5)
            wait.until(lambda driver: self.get_element(locator).is_displayed())

    def wait_element_not_displayed(self, locator):
        end_time = time() + self.driver_wait
        while time() < end_time:
            try:
                if not self.is_displayed(locator):
                    break
            except StaleElementReferenceException:
                sleep(0.5)
                if not self.is_displayed(locator):
                    break

    def click(self, locator):
        self.wait_element_displayed(locator)
        self.get_element(locator).click()

    def enter_text(self, locator, text):
        self.wait_element_displayed(locator)
        self.get_element(locator).send_keys(text)

    def get_element_text(self, locator):
        self.wait_element_displayed(locator)
        return self.get_element(locator).text

    def get_element_attribute(self, locator, attribute):
        self.wait_element_displayed(locator)
        return self.get_element(locator).get_attribute(attribute)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
