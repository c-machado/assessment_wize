import requests

from tests.consts import api_const
from tests.consts.constants import Constants


class BasePageAPI(object):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_article_dates_in_latest_api(self, keyword_url):
        """the url defines the parameters to add in the request to the API"""
        """:return a list with the article dates in the API format e.g. 2021-11-15"""
        api_url = self.get_api_url(keyword_url)
        response = requests.get(Constants.BASE_URL + api_url)
        print('api:', Constants.BASE_URL + api_url)
        result = response.json()
        article_dates = []
        for article in result['results']:
            article_dates.append(article['published'][0:10])
            print("article['published'][0:10]", article['published'])
            print("article['headline']", article['headline'])
        return article_dates

    @staticmethod
    def get_api_url(keyword_url):
        """:return api url according to page received, this is required because each page has different filters"""
        for page, api_url in api_const.LATEST_FEED.items():
            if page == keyword_url:
                print('API_URL', api_url, "KEYWORD_URL", keyword_url)
                return api_url


