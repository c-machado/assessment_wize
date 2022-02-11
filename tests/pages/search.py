import re
import time

import requests
from assertpy import assert_that

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.base_page_api import BasePageAPI
from tests.pages.locators import PageLocators


class Search(BasePage, BasePageAPI):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_filter = 0
        self.tag_to_filter = ''

    def click_search_icon_in_nav_bar(self):
        self.driver.click_to_element(PageLocators.search_icon_nav_desktop)
        self.driver.wait_for_element_visible(*PageLocators.search_bar_text_field)
        # time.sleep(2)

    def click_search_icon_in_bar_expanded(self):
        self.driver.click_to_element(PageLocators.search_icon_nav_expanded)
        self.driver.wait_for_page_load()

    def click_filter_by_random_option(self):
        filter_by_options_list = self.get_list_filter_by_results()
        print('filter_by_options_list', len(filter_by_options_list))
        self.get_random_element_to_filter(self.get_list_filter_by_results())
        self.tag_to_filter = filter_by_options_list[self.random_filter].get_attribute("innerHTML")
        print('tag to filter', self.tag_to_filter)
        filter_by_options_list[self.random_filter].click()
        self.driver.wait_for_page_load()
        self.driver.wait_for_element_visible(PageLocators.search_tag_filter_selected)

    def close_search_bar(self):
        self.driver.click_to_element(PageLocators.search_close_icon_desktop)

    def get_articles_in_feed_search_results_page(self):
        return self.driver.find_elements(*PageLocators.search_eyebrow_articles_in_feed)

    @staticmethod
    def get_msg_no_search_results_per_language(text_to_search, language):
        for language_id, message in Constants.SEARCH_NO_RESULTS_MSG.items():
            if language_id == language:
                message_no_search_results = re.sub('text_to_search', text_to_search, message)
                print('expected', message_no_search_results)
                return message_no_search_results

    def get_msg_no_search_results_in_page(self):
        print('actual msg', self.driver.find_element(*PageLocators.search_no_results_header).get_attribute("innerHTML"))
        return self.driver.find_element(*PageLocators.search_no_results_header).get_attribute("innerHTML")

    def get_search_results_headlines(self, search_results):
        results_headlines = []
        for article in search_results:
            article_headline = article.get_attribute("innerHTML")
            print('article value', article.get_dom_attribute("innerHTML"))
            if self.contains_ampersand_char(article_headline):
                article_headline = re.sub('&amp;', '&', article_headline)
            results_headlines.append(article_headline)
            print('headline in page', article_headline)
        return results_headlines

    def get_list_filter_by_results(self):
        self.driver.wait_for_page_load()
        filter_by_options = self.driver.find_elements(*PageLocators.search_filter_by)
        for element in filter_by_options:
            print('element', element.get_attribute("innerHTML"))
        return filter_by_options

    def get_random_element_to_filter(self, element_list):
        import random
        self.random_filter = random.randint(1, len(element_list) - 1)
        print('random', self.random_filter)
        return self.random_filter

    def get_results_filtered(self):
        articles_in_feed = self.get_articles_in_feed_search_results_page()
        articles_tags_in_feed_results = self.get_tag_eyebrow_in_feed_results_page(articles_in_feed)
        for tag in articles_tags_in_feed_results:
            if tag != self.tag_to_filter:
                print('tag in feed', tag)
                return False
        return True

    def get_suggested_results_expected(self, keyword_url, text_to_search):
        return self.get_suggested_results_in_search_api(keyword_url, text_to_search)

    def get_search_results_in_page(self):
        results_in_page = self.driver.find_elements(*PageLocators.search_results_list)
        return self.get_search_results_headlines(results_in_page)

    def get_suggested_results_in_page(self):
        suggested_results_in_page = self.driver.find_elements(*PageLocators.search_suggestions_results_list)
        return self.get_search_results_headlines(suggested_results_in_page)

    @staticmethod
    def get_tag_eyebrow_in_feed_results_page(eyebrow_in_articles):
        tag_articles_eyebrow = []
        for element in eyebrow_in_articles:
            tag_eyebrow = element.get_attribute("innerHTML").split("/ ")[1]
            print('tag', tag_eyebrow)
            tag_articles_eyebrow.append(tag_eyebrow)
        return tag_articles_eyebrow

    def is_search_bar_visible(self):
        return self.driver.find_element(*PageLocators.search_bar_text_field).is_displayed()

    def is_search_bar_not_visible(self):
        self.driver.wait_for_element_not_visible(*PageLocators.search_bar_text_field)

    def is_searchbar_button_visible(self):
        return self.driver.find_element(*PageLocators.search_icon_nav_desktop).is_displayed()

    def is_search_results_header_visible(self):
        return self.driver.find_element(*PageLocators.search_results_header).is_displayed()

    def type_search_criteria(self, search_criteria):
        text_field = self.driver.find_element(*PageLocators.search_bar_text_field)
        text_field.send_keys(search_criteria)

    @staticmethod
    def load_recent_article():
        response = requests.get(Constants.BASE_URL+'/api/v2/latest')
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        assert_that(response.status_code).is_equal_to(200)
        result = response.json()
        print('len response', len(result['results']))
        articles = [result['results'] for article in result]
        # print('articles', articles)
        # assert_that(android_articles).contains('category')
        for article in result['results']:
            print('article', article)
            print('category', article['category'])
            print('tag', article['tag'])
            print('published', article['published'])
            assert_that(article['category']).contains('article')
        assert False
