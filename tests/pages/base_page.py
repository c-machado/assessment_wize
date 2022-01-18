import pytest
import requests

from datetime import datetime
from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class BasePage(object):

    # It takes in the browser, which will be passed in from the test case
    def __init__(self, driver):
        # Set my local self.browser variable to be whatever browser it's passed in
        self.driver = driver

    def click_tab(self, tab_locator):
        self.driver.click_to_element(tab_locator)

    def close_bar(self, locator):
        self.driver.wait_for_page_load()
        self.driver.click_to_element(locator)

    def get_current_page(self):
        self.driver.switch_to_active_tab()
        print('current url ', self.driver.current_url())
        return self.driver.current_url()

    @staticmethod
    def get_date_in_api_format(date, format_date):
        return datetime.strptime(date, format_date).strftime(Constants.DATE_FORMAT_IN_API)

    @staticmethod
    def get_item_selector(item, locators):
        for item_id, locator_item in locators.items():
            if item_id == item:
                print('locator ', locator_item, 'submenu', item)
                return locator_item

    def get_status_redirect(self):
        return self.driver.execute_script("var xhr = new XMLHttpRequest();"
                                          "xhr.open('GET', window.location, false);"
                                          "xhr.send(null);" "return xhr.status")

    @staticmethod
    def check_internal_status(items):
        for internal_item in items:
            response = requests.get(internal_item)
            if response != 200:
                print('response', response, 'internal', internal_item)
            assert response.status_code == 200

    @staticmethod
    def remove_enter(string):
        import re
        pattern = re.compile(r'\n+')
        return re.sub(pattern, '', string)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scroll({top: document.body.scrollHeight-80, behavior: 'smooth'});")

    def scroll_to_fifty_percent(self):
        self.driver.execute_script("window.scroll({"
                                   "top: (document.body.scrollHeight/2), "
                                   "left: 0,"
                                   "behavior: 'smooth'});")

    def scroll_to_content(self):
        self.driver.execute_script("window.scroll({"
                                   "top: document.getElementById('footer-standard'),"
                                   "left: 0,"
                                   " behavior: 'smooth'});")

    def scroll_to_feed(self):
        self.driver.execute_script("window.scroll("
                                   "{top: document.getElementsByClassName('feed-article.ng-scope'),"
                                   "left: 0,"
                                   " behavior: 'smooth'});")
