import pytest
from os.path import join
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from resources.pages.application import Application
from resources.utils.file_ops import get_yaml


@pytest.fixture(scope="session")
def driver(data):
    settings = data['web_driver_settings']
    options = Options()
    options.add_argument('--headless') if settings['headless'] else None
    options.add_argument('start-maximized') if settings['maximized'] else None
    options.add_argument('start-fullscreen') if settings['fullscreen'] else None
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def data():
    relative_path_from_here_to_yaml = join("..", "resources", "test_data", 'data.yaml')
    data = get_yaml(__file__, relative_path_from_here_to_yaml)
    return data


@pytest.fixture(scope="session")
def app(driver: webdriver, data):
    app_data = {"driver": driver, "data": data}
    return Application(app_data)
