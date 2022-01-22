import random
import datetime

import config
from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_article = 0

    def get_articles_in_feed_list(self):
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

    @staticmethod
    def get_article_dates_in_latest_api(keyword_url):
        """the url defines the parameters to add in the request to the API"""
        """:return a list with the article dates in the API format e.g. 2021-11-15"""
        import requests
        if keyword_url.__contains__('perspectives'):
            response = requests.get(Constants.BASE_URL + config.LATEST_FEED_PERSPECTIVE)
        elif keyword_url.__contains__('/intl/de-de/'):
            response = requests.get(Constants.BASE_URL + config.LATEST_FEED_DE)
        elif keyword_url.__contains__('/intl/en-au/'):
            response = requests.get(Constants.BASE_URL + config.LATEST_FEED_AU)
        elif keyword_url.__contains__('/intl/en-in/'):
            response = requests.get(Constants.BASE_URL + config.LATEST_FEED_IN)
        else:
            response = requests.get(Constants.BASE_URL + config.LATEST_FEED)
        result = response.json()
        article_dates = []
        for article in result['results']:
            article_dates.append(article['published'][0:10])
            print("article['published'][0:10]", article['published'])
        return article_dates

    def get_date_from_article_in_feed_in_latest_api(self, keyword_url):
        """:return published date from the current random article in API format"""
        print('random_article in get_date_from_article_in_feed_in_latest_api', self.random_article)
        article_dates_in_api = self.get_article_dates_in_latest_api(keyword_url)
        for index in range(0, len(article_dates_in_api)):
            print('index', index, 'feed_article_date_in_latest_api: ', article_dates_in_api[index])
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
            print('Je suis tres content', locale)
            self.set_locale(locale)
            format0 = self.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PER_LOCALE)
            # date_expected = datetime.datetime.strptime(date_article_in_api, format0)
            date_expected_t = datetime.datetime.strptime(date_article_in_api, Constants.DATE_FORMAT_IN_API).strftime(format0)
            print('format0', format0)
            print('return date_expectedt', date_expected_t)
            return date_expected_t
        elif year_current_article < current_year:
            print('je suis tres intelligent', locale)
            self.set_locale(locale)
            format1 = self.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PAST_YEAR_PER_LOCALE)
            date_expected_1 = datetime.datetime.strptime(date_article_in_api, Constants.DATE_FORMAT_IN_API).strftime(format1)
            print('format0', format1)
            print('return date_expectedt', date_expected_1)
            return date_expected_1

    # def get_date_format_in_feed(self, url, locale, date_article):
    #     """To capture the format that applies based on the received date"""
    #     """It should be Month Day (if the year is the same as the current one)"""
    #     """It should be Month Year (if the year is the previous tp the current one)"""
    #
    #     """e.g.: 2022-01-21 14:04:31.821058"""
    #     current_year = datetime.datetime.now().year
    #     print('date_article_received', date_article)
    #     print('url', Constants.BASE_URL + url)
    #     year_current_article = ''
    #     Dict = {}
    #     article_dates_in_api = self.get_article_dates_in_latest_api(url)
    #
    #     for date_current_article in article_dates_in_api:
    #         # published_date_in_api = self.get_date_in_api_format(date_current_article, Constants.DATE_FORMAT_IN_API)
    #         '''replace with the method in base_page'''
    #         year_current_article = (datetime.datetime.strptime(date_current_article, Constants.DATE_FORMAT_IN_API)).year
    #         # print('published_date_in_api: ', published_date_in_api)
    #         print('year_current_article ', year_current_article, 'date_current_article', date_current_article)
    #         if current_year == year_current_article:
    #             print('Je suis tres content')
    #             format = self.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PER_LOCALE)
    #             Dict = dict([(date_current_article, format)])
    #             print(Dict)
    #             print('return content', self.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PER_LOCALE))
    #         elif year_current_article < current_year:
    #             print('je suis tres intelligent')
    #             format1 = self.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PAST_YEAR_PER_LOCALE)
    #             print('return intelligent',
    #                   self.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PAST_YEAR_PER_LOCALE))
    #             Dict = dict([(date_current_article, format1)])
    #             print(Dict)

    def get_random_article_in_feed(self):
        self.random_article = random.randint(0, len(self.get_articles_in_feed_list()) - 1)
        return self.random_article

    def click_to_random_article(self):
        article_list = self.get_articles_in_feed_list()
        # random_article = self.get_random_article_in_feed()
        print('random_article in click article:', self.random_article)
        for article in range(0, len(article_list)):
            if article == self.random_article:
                print('article to click: ', article_list[article].get_attribute("innerHTML"))
                self.driver.wait_for_element_visible(article_list[article])
                article_list[article].click()
