import pytest
import requests

import datetime
from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class BasePage(object):

    # It takes in the browser, which will be passed in from the test case
    def __init__(self, driver):
        # Set my local self.browser variable to be whatever browser it's passed in
        self.driver = driver

    @staticmethod
    def check_internal_status(items):
        for internal_item in items:
            response = requests.get(internal_item)
            if response != 200:
                print('response', response, 'internal', internal_item)
            assert response.status_code == 200

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
        # return a string in the converted format
        """Now, formatting datetime object into any date format.
        We can convert any datetime object to nearly any representation
        of date format using strftime() method."""
        return datetime.datetime.strptime(date, format_date).strftime(Constants.DATE_FORMAT_IN_API)

    @staticmethod
    def get_date_format_per_locale(locale, date_format_per_locale):
        for locale_format, date_format in date_format_per_locale.items():
            if locale_format == locale:
                return date_format

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

    def click_to_load_more_articles_in_feed(self):
        self.driver.click_to_element(PageLocators.feed_load_more)

    # TODO: Install a new locale on MAC, so India can be tested with the corresponding label en_IN,
    # meanwhile it will be tested with en_GB which is basically the same format than en_IN
    def is_date_format_correct(self, date_string, date_format, locale_string):
        # date_string = date.get_attribute("innerHTML")
        # print('date_string', date.get_attribute("innerHTML"))
        print('date_format', date_format)
        from datetime import datetime
        self.set_locale(locale_string)
        print('date locale updated: ', datetime.strptime(date_string, date_format))
        try:
            is_format_expected = bool(datetime.strptime(date_string, date_format))
        except ValueError:  # wrong date format
            is_format_expected = False
        print("Does date match format? : " + str(is_format_expected))
        return is_format_expected

    @staticmethod
    def remove_enter(string):
        import re
        pattern = re.compile(r'\n+')
        return re.sub(pattern, '', string)

    def scroll_to_bottom(self):
        self.driver.wait_for_page_load()
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

    @staticmethod
    def set_locale(locale_string):
        import locale
        locale.setlocale(locale.LC_ALL, locale_string)
        loc = locale.getlocale()
        print(loc)