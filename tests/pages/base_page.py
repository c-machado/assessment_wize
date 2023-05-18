import datetime
import logging
import random
import re
import time

import pytest
import requests
from babel.dates import format_date
from bs4 import BeautifulSoup

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class BasePage:
    # It takes in the browser, which will be stage in from the test case
    def __init__(self, driver):
        # Set my local self.browser variable to be whatever browser it's stage in
        self.driver = driver
        self.random_article = 0
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def check_internal_status(items):
        for internal_item in items:
            response = requests.get(internal_item)
            assert response.status_code == 200

    def click_tab(self, tab_locator):
        self.driver.click_to_element(tab_locator)

    def close_bar(self, locator):
        self.driver.wait_for_page_load()
        self.logger.info(
            '%s local storage',
            self.driver.execute_script(
                "window.localStorage.getItem('cookieConsent');"
            ),
        )
        if Constants.PROD_URL not in self.driver.current_url():
            self.clear_local_storage()
            self.driver.click_to_element(locator)
        else:
            self.driver.click_to_element(locator)

    def clear_local_storage(self):
        self.driver.execute_script('window.localStorage.clear();')
        self.driver.refresh()

    def get_current_page(self):
        self.driver.switch_to_active_tab()
        return self.driver.current_url()

    @staticmethod
    def get_element_in_list(elements_list, element):
        for index, title in enumerate(elements_list):
            if element == index:
                return title

    @staticmethod
    def get_year_in_given_date(date_to_convert, format_date):
        return (datetime.datetime.strptime(date_to_convert, format_date)).year

    @staticmethod
    def get_month_in_given_date_babel_format(date, locale):
        return format_date(date, format='MMM', locale=locale)

    @staticmethod
    def get_day_in_given_date_babel_format(date, locale):
        return format_date(date, format='dd', locale=locale)

    @staticmethod
    def get_year_in_given_date_babel_format(date, locale):
        return format_date(date, format='yyyy', locale=locale)

    @staticmethod
    def get_date_in_api_format(date, format_date):
        # return a string in the converted format
        """Now, formatting datetime object into any date format.
        We can convert any datetime object to nearly any representation
        of date format using strftime() method."""
        return datetime.datetime.strptime(date, format_date).strftime(
            Constants.DATE_FORMAT_IN_API
        )

    def get_item_selector(self, item, locators):
        for item_id, locator_item in locators.items():
            if item_id == item:
                self.logger.info('%s locator_item', locator_item)
                self.logger.info('%s submenu', item)
                return locator_item

    # If the viewport is mobile the article to select will be the first one visible in the feed
    def get_random_index_in_list(self, element_list, get_viewport):
        # time.sleep(1)
        element_list_length = len(element_list)
        self.logger.info('%s length list in random', element_list_length)
        try:
            self.random_article = (
                random.randint(0, element_list_length - 1)
                if get_viewport == 'desktop'
                else 0
            )
        except Exception as e:
            print(e)
        return self.random_article

    def get_scroll_locator(self, url, random_article):
        if self.is_category_page_horizontal(url) and random_article == 0:
            random_articlem_index = random_article + 1
            locator = re.sub(
                'index_to_scroll',
                str(random_articlem_index),
                Constants.SCROLL_TO_CATEGORY_HORIZONTAL_FEED,
            )
            self.logger.info('%s locator cat horizontal', locator)
            return locator
        elif random_article >= 0:
            random_index = random_article + 1
            locator = re.sub(
                'index_to_scroll',
                str(random_index),
                Constants.SCROLL_TO_HOME_FEED,
            )
            self.logger.info('%s locator feed starts at 1', locator)
            return locator

    @staticmethod
    def get_text_from_span(element):
        soup = BeautifulSoup(element.get_attribute('outerHTML'), 'xml')
        return soup.find('span').text

    def get_status_redirect(self):
        return self.driver.execute_script(
            'var xhr = new XMLHttpRequest();'
            "xhr.open('GET', window.location, false);"
            'xhr.send(null);'
            'return xhr.status'
        )

    def go_back_previous_page(self):
        return self.driver.execute_script('window.history.go(-1)')

    def click_to_load_more_articles_in_feed(self):
        self.driver.click_to_element(PageLocators.feed_load_more)

    @staticmethod
    def is_category_page_horizontal(keyword_url):
        if keyword_url in Constants.CATEGORY_HORIZONTAL:
            return True

    def is_element_visible(self, *locator):
        self.logger.info(self.driver.find_element(*locator).is_displayed())
        return self.driver.find_element(*locator).is_displayed()

    @staticmethod
    def is_substring(str1, str2):
        if re.search(str1, str2):
            return True

    def get_date_babel_format(self, date_string, date_format, locale_string):
        from datetime import datetime

        self.logger.info('%s date_format', date_format)
        date = datetime.strptime(date_string, Constants.DATE_FORMAT_IN_API)
        self.logger.info('%s date_tr', date)
        date_babel = format_date(date, format=date_format, locale=locale_string)
        self.logger.info('%s date_article_babel', date_babel)
        return date_babel

    @staticmethod
    def order_list_by_date_desc(article_dates_list):
        for index in range(len(article_dates_list) - 2):
            article_current_date = datetime.datetime.strptime(
                article_dates_list[index], Constants.DATE_FORMAT_IN_API
            )
            article_next_date = datetime.datetime.strptime(
                article_dates_list[index + 1], Constants.DATE_FORMAT_IN_API
            )
            if article_current_date < article_next_date:
                return False
            return True

    @staticmethod
    def remove_enter(string):
        pattern = re.compile(r'\n+')
        return re.sub(pattern, '', string)

    def replace_space(self, string):
        string_without_special_chars = string
        if self.contains_ampersand_char(string):
            string_without_special_chars = re.sub('&amp;', 'and', string)
        pattern = re.compile(r'\s+')
        string_no_spaces_no_special_chars = re.sub(
            pattern, '-', string_without_special_chars.strip()
        )
        return string_no_spaces_no_special_chars

    @staticmethod
    def format_ampersand_in_url(string):
        string_without_special_chars = string
        if re.compile('&'):
            string_without_special_chars = re.sub('&', 'and', string)
        pattern = re.compile(r'\s+')
        string_no_spaces_no_special_chars = re.sub(
            pattern, '-', string_without_special_chars.strip()
        )
        return string_no_spaces_no_special_chars

    @staticmethod
    def format_ampersand_in_type_url(string):
        string_without_special_chars = string
        if re.compile('&'):
            string_without_special_chars = re.sub('&', 'and', string)
        return string_without_special_chars

    @staticmethod
    def contains_ampersand_char(string):
        regexp = re.compile('&amp;')
        if regexp.search(string):
            return True

    @staticmethod
    def contains_hyphen_char(string):
        regexp = re.compile('–&nbsp;')
        if regexp.search(string):
            return True

    @staticmethod
    def contains_space_char(string):
        regexp = re.compile('&nbsp;')
        if regexp.search(string):
            return True

    @staticmethod
    def contains_filtered_tag(tag_to_filter, primary_tags):
        true_match = False
        for tag in primary_tags:
            match = re.search(tag_to_filter.lower(), tag)
            if match:
                print(match)
                true_match = True
        return true_match

    def replace_ampersand_char(self, string):
        if self.contains_ampersand_char(string):
            return re.sub('&amp;', '&', string)
        else:
            return string

    def replace_hyphen_char(self, string):
        if self.contains_hyphen_char(string):
            return re.sub('–&nbsp;', '– ', string)
        else:
            return string

    def remove_html_tags(self, raw_html):
        cleaner = re.compile('<.*?>')
        clean_text = re.sub(cleaner, '', raw_html)
        if self.contains_ampersand_char(clean_text):
            clean_text = self.replace_ampersand_char(clean_text)
            return clean_text
        else:
            return clean_text

    @staticmethod
    def set_locale(locale_string):
        print('locale_string', locale_string)
        import locale

        locale.setlocale(locale.LC_ALL, locale_string)
        loc = locale.getlocale()
        print(loc)

    def scroll_to_bottom(self):
        self.driver.wait_for_page_load()
        self.driver.execute_script(
            'window.scroll({'
            'top: (document.body.scrollHeight), '
            'left: 0,'
            "behavior: 'smooth'});"
        )
        time.sleep(1)

    def scroll_to_fifty_percent(self):
        self.driver.execute_script(
            'window.scroll({'
            'top: (document.body.scrollHeight/2), '
            'left: 0,'
            "behavior: 'smooth'});"
        )

    def scroll_to_content(self):
        self.driver.execute_script(
            'window.scroll({'
            "top: document.getElementById('footer-standard'),"
            'left: 0,'
            " behavior: 'smooth'});"
        )
        time.sleep(1)

    def scroll_to_feed_mobile(self):
        self.driver.execute_script(
            "document.querySelector('.article-list__feed').scrollIntoView();"
        )

    def scroll_to_feed(self, random_article, keyword_url, get_viewport):
        self.scroll_to_feed_desktop(
            random_article, keyword_url
        ) if get_viewport == 'desktop' else self.scroll_to_feed_mobile()

    def scroll_to_feed_desktop(self, random_article, keyword_url):
        self.scroll_to_bottom()
        print('RANDOM IN scroll_to_feed', random_article)
        locator = self.get_scroll_locator(keyword_url, random_article)
        print('locator', locator)
        from selenium.webdriver.common.by import By

        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        from selenium.webdriver import Keys

        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
