import random
import time

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
        self.random_article = 0

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
        # self.scroll_to_bottom()
        self.driver.click_to_element(locator)

    def get_current_page(self):
        self.driver.switch_to_active_tab()
        print('current url ', self.driver.current_url())
        return self.driver.current_url()

    @staticmethod
    def get_year_in_given_date(date_to_convert, format_date):
        return (datetime.datetime.strptime(date_to_convert, format_date)).year

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

    def get_format_per_year(self, locale, constants_date_format, date_article_in_api):
        self.set_locale(locale)
        format_expected = self.get_date_format_per_locale(locale, constants_date_format)
        print('format0', format_expected)
        date_expected = datetime.datetime.strptime(date_article_in_api, Constants.DATE_FORMAT_IN_API).strftime(
            format_expected)
        print('return date_expected', date_expected)
        return date_expected

    @staticmethod
    def get_item_selector(item, locators):
        for item_id, locator_item in locators.items():
            if item_id == item:
                print('locator ', locator_item, 'submenu', item)
                return locator_item

    def get_random_index_in_list(self, element_list):
        element_list_length = len(element_list)
        print('list length of articles in feed', element_list_length)
        self.random_article = random.randint(0, element_list_length - 1)
        return self.random_article

    def get_scroll_locator(self, url):
        if self.is_category_page_horizontal(url):
            return PageLocators.feed_articles_category_horizontal_top
        else:
            return PageLocators.feed_articles_list_top

    def get_status_redirect(self):
        return self.driver.execute_script("var xhr = new XMLHttpRequest();"
                                          "xhr.open('GET', window.location, false);"
                                          "xhr.send(null);" "return xhr.status")

    def go_back_previous_page(self):
        return self.driver.execute_script("window.history.go(-1)")

    def click_to_load_more_articles_in_feed(self):
        self.driver.click_to_element(PageLocators.feed_load_more)

    @staticmethod
    def is_category_page_horizontal(keyword_url):
        if keyword_url.__contains__(Constants.GERMANY_CATEGORY_PAGE) or \
                keyword_url.__contains__(Constants.INDIA_CATEGORY_PAGE) or \
                keyword_url.__contains__(Constants.AUSTRALIA_CATEGORY_PAGE):
            return True

    def is_element_visible(self, *locator):
        return self.driver.find_element(*locator).is_displayed()

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
    def order_list_by_date_desc(article_dates_list):
        for index in range(len(article_dates_list)-2):
            article_current_date = datetime.datetime.strptime(article_dates_list[index], Constants.DATE_FORMAT_IN_API)
            article_next_date = datetime.datetime.strptime(article_dates_list[index+1], Constants.DATE_FORMAT_IN_API)
            if article_current_date < article_next_date:
                return False
            return True

    @staticmethod
    def remove_enter(string):
        import re
        pattern = re.compile(r'\n+')
        return re.sub(pattern, '', string)

    def replace_space(self, string):
        import re
        string_without_special_chars = string
        if self.contains_ampersand_char(string):
            string_without_special_chars = re.sub("&amp;", "and", string)
        pattern = re.compile(r'\s+')
        string_no_spaces_no_special_chars = re.sub(pattern, '-', string_without_special_chars.strip())
        return string_no_spaces_no_special_chars

    @staticmethod
    def contains_ampersand_char(string):
        import re
        regexp = re.compile("&amp;")
        if regexp.search(string):
            return True

    @staticmethod
    def contains_filtered_tag(tag_to_filter, primary_tags):
        true_match = False
        import re
        for tag in primary_tags:
            match = re.search(tag_to_filter.lower(), tag)
            if match:
                print(match)
                true_match = True
        return true_match

    def replace_ampersand_char(self, string):
        if self.contains_ampersand_char(string):
            import re
            return re.sub("&amp;", "&", string)
        else:
            return string

    def remove_html_tags(self, raw_html):
        import re
        cleaner = re.compile('<.*?>')
        clean_text = re.sub(cleaner, '', raw_html)
        if self.contains_ampersand_char(clean_text):
            clean_text = self.replace_ampersand_char(clean_text)
            return clean_text
        else:
            return clean_text

    def scroll_to_bottom(self):
        self.driver.wait_for_page_load()
        self.driver.execute_script("window.scroll({"
                                   "top: (document.body.scrollHeight), "
                                   "left: 0,"
                                   "behavior: 'smooth'});")
        time.sleep(1)

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
        time.sleep(1)

    def scroll_to_feed(self, random_article, keyword_url):
        print('RANDOM IN scroll_to_feed', random_article)
        locator = self.get_scroll_locator(keyword_url)
        if random_article <= 3:
            element = self.driver.find_element(*locator)
            from selenium.webdriver import Keys
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        else:
            self.scroll_to_bottom()
            time.sleep(1)

    @staticmethod
    def set_locale(locale_string):
        import locale
        locale.setlocale(locale.LC_ALL, locale_string)
        loc = locale.getlocale()
        print(loc)
