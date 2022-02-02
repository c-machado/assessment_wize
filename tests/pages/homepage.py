import random
import datetime
import time

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.base_page_api import BasePageAPI
from tests.pages.locators import PageLocators


class HomePage(BasePage, BasePageAPI):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_article = 0

    def get_articles_in_feed_list(self):
        self.driver.wait_for_page_load()
        articles_list = self.driver.find_elements(*PageLocators.feed_articles_list)
        return articles_list

    def get_article_dates_in_feed_list(self):
        article_dates_in_feed = self.driver.find_elements(*PageLocators.feed_article_dates_list)
        return article_dates_in_feed

    def get_date_article_in_feed(self):
        """To capture the date shown in an article in the feed"""
        """:return e.g. Jan 20 / Dec 2021"""
        article_date_list = self.get_article_dates_in_feed_list()
        print('random_article_in_date_feed', self.random_article)
        for article_date_index in range(0, len(article_date_list)):
            print('article_date_index', article_date_index, 'article_date_in_feed ',
                  article_date_list[article_date_index].get_attribute("innerHTML"))
            if article_date_index == self.random_article:
                print('article_date_index', article_date_index, 'actual_article_date_in_feed ', article_date_list[article_date_index].get_attribute("innerHTML"))
                return article_date_list[article_date_index].get_attribute("innerHTML")

    def get_date_first_article_in_feed(self, keyword_url):
        self.go_back_previous_page()
        self.close_bar(PageLocators.cookie_banner_ok_cta)
        date_in_first_article = self.get_article_dates_in_latest_api(keyword_url)[0]
        print('date_in_api', date_in_first_article)
        return date_in_first_article

    def get_date_from_article_in_feed_in_latest_api(self, keyword_url):
        """:return published date from the current random article in API format"""
        """we need to navigate different new category pages, since the first article in the api is not showed in the 
        feed as in the other pages"""
        print('random_article in get_date_from_article_in_feed_in_latest_api', self.random_article)
        article_dates_in_api = self.get_article_dates_in_latest_api(keyword_url)
        start_range = 1
        if keyword_url.__contains__(Constants.GERMANY_CATEGORY_PAGE) or \
                keyword_url.__contains__(Constants.INDIA_CATEGORY_PAGE) or \
                keyword_url.__contains__(Constants.AUSTRALIA_CATEGORY_PAGE):
            start_range = 2
            self.random_article = self.random_article + 1
        for index in range(start_range, len(article_dates_in_api)):
            print('index', index, 'feed_article_date_in_latest_api: ', article_dates_in_api[index], "random", self.random_article)
            if index == self.random_article:
                print('index', index, 'date expected in api format: ', article_dates_in_api[index])
                return article_dates_in_api[index]

    def get_date_format_in_feed_per_locale(self, keyword_url, locale):
        """:return date in API in corresponding format based on the locale and year"""
        """To capture the format that applies based on the current random article"""
        """It should be Month Day (if the year is the same as the current one)"""
        """It should be Month Year (if the year is the previous tp the current one)"""
        date_article_in_api = self.get_date_from_article_in_feed_in_latest_api(keyword_url)
        year_current_article = (datetime.datetime.strptime(date_article_in_api, Constants.DATE_FORMAT_IN_API)).year
        print('year_current_article', year_current_article)
        current_year = datetime.datetime.now().year
        print('current_year', current_year)
        if current_year == year_current_article:
            return self.get_format_per_year(locale, Constants.DATE_FORMAT_IN_FEED_PER_LOCALE, date_article_in_api)
        elif year_current_article < current_year:
            return self.get_format_per_year(locale, Constants.DATE_FORMAT_IN_FEED_PAST_YEAR_PER_LOCALE, date_article_in_api)

    def get_format_per_year(self, locale, constants_date_format, date_article_in_api):
        self.set_locale(locale)
        format_expected = self.get_date_format_per_locale(locale, constants_date_format)
        print('format0', format_expected)
        date_expected = datetime.datetime.strptime(date_article_in_api, Constants.DATE_FORMAT_IN_API).strftime(
            format_expected)
        print('return date_expected', date_expected)
        return date_expected

    def get_random_article_in_feed(self):
        feed_list_length = len(self.get_articles_in_feed_list())
        print('list length of articles in feed', feed_list_length)
        self.random_article = random.randint(1, feed_list_length - 1)
        return self.random_article

    def click_to_random_article(self):
        article_list = self.get_articles_in_feed_list()
        print('random_article in click article:', self.random_article)
        for article in range(0, len(article_list)):
            if article == self.random_article:
                print('article to clickx: ', article_list[article].get_attribute("innerHTML"))
                self.driver.wait_for_element_visible(article_list[article])
                self.driver.wait_for_element_clickable(article_list[article])
                time.sleep(1)
                article_list[article].click()

    def click_load_more_stories_in_feed(self):
        self.driver.click_to_element(PageLocators.feed_load_more)

    def order_list_by_date_desc(self, article_dates_list):
        print(article_dates_list.sort(lambda date: datetime.datetime.strptime(date, "%d-%b-%y")))
        return article_dates_list.sort(lambda date: datetime.datetime.strptime(date, "%d-%b-%y"))
