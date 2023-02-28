import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def set_browser_size():
    browser.config.window_width = 1900
    browser.config.window_height = 1080

def test_google_should_not_find_text(set_browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('testgoogleshouldnotfindtext').press_enter()
    browser.element('#topstuff').should(have.text('По запросу testgoogleshouldnotfindtext ничего не найдено.'))