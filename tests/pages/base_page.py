import pytest

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class BasePage(object):

    # It takes in the browser, which will be passed in from the test case
    def __init__(self, browser):
        # Set my local self.browser variable to be whatever browser it's passed in
        self.browser = browser

    def click_tab(self, tab_locator):
        self.browser.click_to_element(tab_locator)

    def get_status_redirect(self):
        return self.browser.execute_script("var xhr = new XMLHttpRequest();" 
                                           "xhr.open('GET', window.location, false);"
                                           "xhr.send(null);" "return xhr.status")

    def close_cookie_banner(self):
        self.browser.click_to_element(PageLocators.cookie_banner)

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scroll({top: document.body.scrollHeight-80, behavior: 'smooth'});")

    def scroll_to_content(self):
        self.browser.execute_script("window.scroll({top: document.getElementById('footer-standard'),"
                                    " behavior: 'smooth'});")

