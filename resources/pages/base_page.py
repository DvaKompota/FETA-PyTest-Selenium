from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import time, sleep


class BasePage:
    """Base class for every page object of the web application under test

    Includes all basic page methods, applicable to every page, like (get_element,
    is_displayed, click, enter_text, get_element_text, and many more)
    Requires app_data dictionary (containing WebDriver, test data, and other settings) as an input
    """

    locator_example = 'some_xpath'

    def __init__(self, app_data: dict) -> None:
        """Initialize self

        :param app_data:        Dictionary, containing WebDriver, test data, and other settings
        :return:                None
        """
        self.driver = app_data['driver']
        self.data = app_data['data']
        self.driver_wait = self.data['web_driver_settings']['wait_time']

    def open_url(self, url: str) -> None:
        """Open the provided url in a web browser

        :param url:             String, to be typed into the text field
        :return:                None
        """
        self.driver.get(url)

    def get_title(self):
        """Return the page title of the currently active browser tab

        :return:                String, representing the page title of the currently active browser tab
        """
        return self.driver.title

    def get_element(self, locator: WebElement or str or tuple, wait_time: int or float = None,
                    poll_frequency: int or float = None) -> WebElement:
        """Return a WebElement which matches the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param wait_time:       Int, representing time in seconds for element to appear.  Defaults to page's wait_time.
        :param poll_frequency:  Int, that overrides the WebDriverWait class's default poll frequency if needed
        :return:                WebElement matching the provided locator
        """
        if type(locator) is WebElement:
            return locator
        elif type(locator) is str:
            try:
                page_attribute = getattr(self, locator)
                locator = (By.XPATH, page_attribute) if type(page_attribute) is str else page_attribute
            except AttributeError:
                locator = (By.XPATH, locator)
        if len(locator) != 2:
            raise ValueError(f"The locator '{locator}' does not have exactly 2 elements")
        if poll_frequency:
            wait = WebDriverWait(self.driver, wait_time if wait_time else self.driver_wait, poll_frequency)
        else:
            wait = WebDriverWait(self.driver, wait_time if wait_time else self.driver_wait)
        return wait.until(EC.presence_of_element_located(locator), message=f'Element {locator} is not present')

    def is_displayed(self, locator: WebElement or str or tuple, retries: int = 1) -> bool:
        """Check if an element with the provided locator is displayed or not

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param retries:         Int, representing how many retries should happen if the element reference is stale
        :return:                True if the element is displayed
                                False if the element is hidden or does not exist
        """
        end_time = time() + self.driver_wait
        while time() < end_time:
            try:
                element = self.get_element(locator, wait_time=0.05, poll_frequency=0.01)
                return bool(element.is_displayed())
            except TimeoutException:
                return False
            except NoSuchElementException:
                return False
            except StaleElementReferenceException as exception:
                if retries > 0:
                    retries -= 1
                else:
                    raise exception

    def wait_element_displayed(self, locator: WebElement or str or tuple, wait_time: int or float = None) -> None:
        """Wait until an element with the provided locator is displayed within a timeout period

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param wait_time:       Int, representing timeout period to wait for the element to appear
        :return:                None
        """
        end_time = time() + wait_time if wait_time else self.driver_wait
        while time() < end_time:
            if self.is_displayed(locator):
                break

    def wait_element_not_displayed(self, locator: WebElement or str or tuple, wait_time: int or float = None) -> None:
        """Wait until an element with the provided locator is not displayed within a timeout period

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param wait_time:       Int, representing timeout period to wait for the element to disappear
        :return:                None
        """
        end_time = time() + wait_time if wait_time else self.driver_wait
        while time() < end_time:
            if not self.is_displayed(locator):
                break

    def click(self, locator: WebElement or str or tuple) -> None:
        """Click an element with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        self.wait_element_displayed(locator)
        self.get_element(locator).click()

    def clear_field(self, locator: WebElement or str or tuple) -> None:
        """Clear a text field with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        self.wait_element_displayed(locator)
        element = self.get_element(locator)
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(Keys.BACKSPACE)

    def enter_text(self, locator: WebElement or str or tuple, text: str) -> None:
        """Type-in the provided text into a text field with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param text:            String, to be typed into the text field
        :return:                None
        """
        self.wait_element_displayed(locator)
        self.get_element(locator).send_keys(text)

    def get_current_url(self) -> str:
        """Return the URL address of the currently active browser tab

        :return:                String, containing URL address of the currently active browser tab
        """
        return self.driver.current_url

    def get_element_attribute(self, locator: WebElement or str or tuple, attribute: str) -> any:
        """Return an attribute value for the provided attribute key of an element with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param attribute:       String, representing the attribute name (key) of the element with the provided locator
        :return:                Attribute value (usually string, int or float) of the element with the provided locator
        """
        self.wait_element_displayed(locator)
        return self.get_element(locator).get_attribute(attribute)

    def get_element_text(self, locator: WebElement or str or tuple) -> str:
        """Return a string of text contained in an element with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                String, representing the text contained in an element with the provided locator
        """
        self.wait_element_displayed(locator)
        return self.get_element(locator).text

    def hover_to(self, locator: WebElement or str or tuple) -> None:
        """Hover over an element with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        ActionChains(self.driver).move_to_element(self.get_element(locator)).perform()

    def select_item_from_dropdown(self, item_text: str, dd_locator: WebElement or str or tuple) -> None:
        """Select a drop-down item with the provided text from a drop-down menu with the provided locator

        :param item_text:       String, representing the text contained in a drop-down item in a drop-down menu
                                with the provided dd_locator
        :param dd_locator:      One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        select = Select(self.get_element(dd_locator))
        select.select_by_visible_text(item_text)

    def switch_to_last_tab(self) -> None:
        """Switch the browser to the last opened browser tab

        :return:                None
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])
