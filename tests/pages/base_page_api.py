import json
import logging
import re
import urllib.parse
from datetime import date, timedelta

import requests
from selenium.common.exceptions import WebDriverException

from tests.consts import api_const
from tests.consts.constants import Constants
from bs4 import BeautifulSoup


class BasePageAPI(object):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def get_api_url_per_type_of_search(self, keyword_url):
        locale_api_url = self.get_locale_url(keyword_url)
        if self.driver.current_url().__contains__('search'):
            self.logger.info('%s api_url_search', api_const.SEARCH_API[locale_api_url])
            return api_const.SEARCH_API[locale_api_url]
        else:
            self.logger.info('%s api_url_suggestions', api_const.SEARCH_SUGGESTIONS_API[locale_api_url])
            return api_const.SEARCH_SUGGESTIONS_API[locale_api_url]

    def get_total_count_articles(self, keyword_url):
        """:return count of articles"""
        self.logger.info(keyword_url)
        api_url = self.get_api_url(keyword_url, api_const.LATEST_FEED)
        self.logger.info(api_url)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        return result['meta']

    def get_article_dates_in_latest_api(self, keyword_url):
        """:return a list with the article dates in the API format e.g. 2021-11-15"""
        self.logger.info(keyword_url)
        api_url = self.get_api_url(keyword_url, api_const.LATEST_FEED)
        self.logger.info(api_url)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        article_dates = []
        for article in result['results']:
            self.logger.info('%s published date', article['published'])
            published_date = article['published'][0:10]
            if published_date <= (date.today()+timedelta(days=1)).strftime("%Y-%m-%d"):
                article_dates.append(published_date)
        return article_dates

    def is_the_article_published(self, article):
        # self.logger.info('%s current date', (date.today() + timedelta(days=1)).strftime("%Y-%m-%d"))
        # self.logger.info('%s published date', article['published'])
        published_date = article['published'][0:10]
        return True if published_date <= (date.today() + timedelta(days=1)).strftime("%Y-%m-%d") else False

    def get_article_tags_in_latest_api(self, keyword_url):
        """:return a list with the article tag in the API e.g. diversity-and-inclusion"""
        article_tags = []
        api_url = self.get_api_url(keyword_url, api_const.LATEST_FEED)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        self.logger.info('%s current date', (date.today() + timedelta(days=1)).strftime("%Y-%m-%d"))
        for article in result['results']:
            self.logger.info('%s article[tag]', article['tag'])
            self.logger.info('%s published date', article['published'])
            if self.is_the_article_published(article):
                article_tags.append(article['tag'])
                self.logger.info('%s article[tag]', article['tag'])
        return article_tags

    def get_article_titles_in_latest_api(self, keyword_url):
        article_headlines = []
        api_url = self.get_api_url(keyword_url, api_const.LATEST_FEED)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        for article in result['results']:
            if self.is_the_article_published(article):
                article_headlines.append(article['headline'])
                self.logger.info('%s article[headline]', article['headline'])
        return article_headlines

    def get_api_url(self, keyword_url, api_urls):
        """:return api url according to locale received from the feature file example"""
        for locale, api_url in api_urls.items():
            if locale == keyword_url:
                self.logger.info(api_url)
                return api_url

    def get_api_url_with_updated_parameters(self, api_url, text_to_search):
        """:return api url per locale with the text_to_search updated in the parameters in the api_url """
        return self.replace_query_parameter(text_to_search, "text_to_search", api_url)

    def get_api_url_with_type_and_tag_parameters(self, api_url, type_filter, tag_filter):
        """:return api url per locale with the type and tag filters updated in the parameters in the api_url """
        api_url_with_type = self.replace_query_parameter(type_filter, "type_filter", api_url)
        api_url_with_type_and_tag = self.replace_query_parameter(tag_filter, "tag_filter", api_url_with_type)
        self.logger.info(api_url_with_type_and_tag)
        return api_url_with_type_and_tag

    def get_tags_in_api_url(self, api_url):
        tags = re.split(r'tags=|&template', api_url)[1]
        tags_list = []
        if re.search(',', tags):
            tags_list = tags.split(',')
            self.logger.info('%s tags_list', tags_list)
            return tags_list
        else:
            self.logger.info('%s unique tag', tags)
            return tags

    def get_results_in_api(self, api_url):
        """:return latest api results according to page received"""
        """the url defines the parameters to add in the request to the API"""
        try:
            if Constants.BASE_URL.endswith('blog.google'):
                response = requests.get(api_url)
                result = response.json()
            else:
                self.driver.go_to_URL(api_url)
                soup = BeautifulSoup(self.driver.get_page_source(), 'lxml')
                api_result = soup.find('pre').text
                result = json.loads(api_result)
                self.driver.go_back_to_url()
                self.driver.wait_for_page_load()
            return result
        except WebDriverException:
            print("Exception on {}".format(api_url))

    def get_suggested_results_in_search_api(self, keyword_url, text_to_search):
        article_results_suggestions = []
        api_url = self.get_api_url_per_type_of_search(keyword_url)
        api_url_with_txt_to_search = self.get_api_url_with_updated_parameters(api_url, text_to_search)
        self.logger.info('%s BASE_URL + api_url_with_txt_to_search', Constants.BASE_URL + api_url_with_txt_to_search)
        result = self.get_results_in_api(Constants.BASE_URL + api_url_with_txt_to_search)
        for article in result['results']:
            headline = article['headline'].replace(u'\xa0', u' ')
            article_results_suggestions.append(headline)
            self.logger.info('%s article[headline] in api', headline)
        return article_results_suggestions

    def get_titles_in_press_asset_api(self, api_url):
        titles_in_press_assets_results = []
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        for asset in result['results']:
            titles_in_press_assets_results.append(asset['title'])
        return titles_in_press_assets_results

    def get_assets_download_urls_per_filter_in_press_api(self, api_url):
        assets_download_urls_in_press_assets_results = []
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        for asset in result['results']:
            assets_download_urls_in_press_assets_results.append(asset['download_url'])
            self.logger.info('%s asset[download_url]', asset['download_url'])
        return assets_download_urls_in_press_assets_results

    def replace_query_parameter(self, type_filter, str_to_replace, url):
        import re
        query_parameter = type_filter
        if self.contains_space(type_filter):
            query_parameter = re.sub(r'\s+', '%20', type_filter)
        query_parameter = urllib.parse.quote(type_filter)
        query_parameter_updated = re.sub(str_to_replace, query_parameter, url)
        return query_parameter_updated

    @staticmethod
    def contains_space(string):
        import re
        regexp = re.compile(r'\s+')
        if regexp.search(string):
            return True

    @staticmethod
    def get_locale_url(keyword_url):
        keyword_url = keyword_url.split('/')
        if keyword_url[1] != 'intl':
            locale_url = '/'
        else:
            locale_url = '/'.join(keyword_url[0:3]) + '/'
        return locale_url
