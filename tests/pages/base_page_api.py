import re
import unicodedata
import urllib.parse

import requests

from tests.consts import api_const
from tests.consts.constants import Constants


class BasePageAPI(object):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_api_url_per_type_of_search(self):
        if self.driver.current_url().__contains__('search'):
            return api_const.SEARCH_API
        else:
            return api_const.SEARCH_SUGGESTIONS_API

    def get_article_dates_in_latest_api(self, keyword_url):
        """:return a list with the article dates in the API format e.g. 2021-11-15"""
        api_url = self.get_latest_api_url(keyword_url)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        article_dates = []
        for article in result['results']:
            article_dates.append(article['published'][0:10])
            print("article['published'][0:10]", article['published'])
        return article_dates

    def get_article_tags_in_latest_api(self, keyword_url):
        """:return a list with the article tag in the API e.g. diversity-and-inclusion"""
        article_tags = []
        api_url = self.get_latest_api_url(keyword_url)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        for article in result['results']:
            article_tags.append(article['tag'])
            print("article['tag]", article['tag'])
        return article_tags

    def get_article_titles_in_latest_api(self, keyword_url):
        article_headlines = []
        api_url = self.get_latest_api_url(keyword_url)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        for article in result['results']:
            article_headlines.append(article['headline'])
            print("article['headline']", article['headline'])
        return article_headlines

    @staticmethod
    def get_latest_api_url(keyword_url):
        """:return api url according to page received, this is required because each page has different filters"""
        for page, api_url in api_const.LATEST_FEED.items():
            if page == keyword_url:
                # print('API_URL', api_url, "KEYWORD_URL", keyword_url)
                return api_url

    @staticmethod
    def get_tags_in_api_url(api_url):
        tags = re.split(r'tags=|&template', api_url)[1]
        print('tags', tags)
        tags_list = []
        if re.search(',', tags):
            tags_list = tags.split(',')
            print('tags_list', tags_list)
            return tags_list
        else:
            print('tags1', tags)
            return tags

    @staticmethod
    def get_results_in_api(api_url):
        """:return latest api results according to page received"""
        """the url defines the parameters to add in the request to the API"""
        response = requests.get(api_url)
        # print('api:', api_url)
        result = response.json()
        return result

    def get_search_api_url(self, keyword_url, text_to_search):
        """:return api url according to page received, this is required because each locale has different site_id"""
        print('current url', self.driver.current_url())
        urls = self.get_api_url_per_type_of_search()
        locale_url = self.get_base_keyword_url(keyword_url)
        print('locale_url', locale_url)
        for page, url in urls.items():
            if page == locale_url:
                api_url = self.replace_query_parameter(text_to_search, url)
                print('API_URL_SEARCH', api_url)
                return api_url

    def get_suggested_results_in_search_api(self, keyword_url, text_to_search):
        article_results_suggestions = []
        api_url = self.get_search_api_url(keyword_url, text_to_search)
        result = self.get_results_in_api(Constants.BASE_URL + api_url)
        for article in result['results']:
            article_results_suggestions.append(article['headline'])
            print("article['headline']", article['headline'])
        return article_results_suggestions

    def replace_query_parameter(self, text_to_search, url):
        import re
        query_parameter = text_to_search
        if self.contains_space(text_to_search):
            query_parameter = re.sub(r'\s+', '%20', text_to_search)
        query_parameter = urllib.parse.quote(text_to_search)
        print('query_parameter', query_parameter)
        query_parameter_updated = re.sub("text_to_search", query_parameter, url)
        return query_parameter_updated

    @staticmethod
    def contains_space(string):
        import re
        regexp = re.compile(r'\s+')
        if regexp.search(string):
            return True

    @staticmethod
    def get_base_keyword_url(keyword_url):
        substring = keyword_url[0:6]
        print('substring', substring)
        if substring == '/intl/':
            url = keyword_url[0:12]
            print('keyword_url[0:12]', keyword_url[0:12])
        else:
            url = keyword_url[0]
            print('keyword_url[0]', keyword_url[0])
        return url
