import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_config():
    browser.config.window_height = 1920
    browser.config.window_height = 1080


@pytest.fixture
def open_google(browser_config):
    browser.open('https://google.com')

    yield

    browser.quit()
