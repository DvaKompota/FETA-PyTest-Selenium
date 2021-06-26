import pytest
from os.path import join
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from resources.pages.application import Application
from resources.utils.file_ops import get_yaml


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def data():
    relative_path_from_here_to_yaml = join("..", "resources", "test_data", 'customer_data.yaml')
    data = get_yaml(__file__, relative_path_from_here_to_yaml)
    return data


@pytest.fixture(scope="session")
def app(driver: webdriver, data):
    app_data = {"driver": driver, "data": data}
    return Application(app_data)
