import logging
import re
import time

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
        self.collections_dict = {}
        self.logger = logging.getLogger(__name__)

    def click_search_icon_in_nav_bar(self):
        self.driver.click_to_element(PageLocators.search_icon_nav_desktop)
        self.driver.wait_for_element_visible(*PageLocators.search_bar_text_field)
        time.sleep(1)

    def click_search_icon_in_bar_expanded(self):
        self.driver.click_to_element(PageLocators.search_icon_nav_expanded)
        self.driver.wait_for_page_load()

    def click_filter_by_random_option(self):
        filter_by_options_list = self.get_list_filter_by_results()
        self.get_random_element_to_filter(filter_by_options_list)
        self.tag_to_filter = filter_by_options_list[self.random_filter].get_attribute("innerHTML")
        self.tag_to_filter = self.replace_ampersand_char(self.tag_to_filter)
        filter_by_options_list[self.random_filter].click()
        self.driver.wait_for_page_load()
        self.driver.wait_for_element_visible(PageLocators.search_tag_filter_selected)

    def click_on_collection_element(self, index):
        print('element', index)
        index = "% s" % index
        from selenium.webdriver.common.by import By
        self.driver.find_element(By.CSS_SELECTOR, '.uni-search-results__list > a:nth-child(' + index + ')').click()

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
            if self.contains_ampersand_char(article_headline):
                article_headline = re.sub('&amp;', '&', article_headline)
            elif self.contains_space_char(article_headline):
                article_headline = re.sub('&nbsp;', ' ', article_headline)
            results_headlines.append(article_headline)
            self.logger.info('%s article_headline', article_headline)
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
        return self.random_filter

    def get_results_filtered(self, keyword):
        articles_in_feed = self.get_articles_in_feed_search_results_page()
        articles_tags_in_feed_results = self.get_tag_eyebrow_in_feed_results_page(articles_in_feed, keyword)
        for tag in articles_tags_in_feed_results:
            if tag != self.tag_to_filter:
                self.logger.info('%s tag in feed', tag)
                return False
        return True

    def get_suggested_results_expected(self, keyword_url, text_to_search):
        suggested_results_api = self.get_suggested_results_in_search_api(keyword_url, text_to_search)
        self.logger.info('%s suggested_results_api', suggested_results_api)
        return suggested_results_api

    def get_search_results_in_page(self):
        results_in_page = self.driver.find_elements(*PageLocators.search_results_list)
        headlines_in_results_page = self.get_search_results_headlines(results_in_page)
        self.logger.info('%s headlines_in_results_page', headlines_in_results_page)
        return headlines_in_results_page

    # TODO: add validation when there are not suggested results
    def get_suggested_results_in_page(self):
        suggested_results_in_page = self.driver.find_elements(*PageLocators.search_suggestions_results_list)
        headlines_suggested_results = self.get_search_results_headlines(suggested_results_in_page)
        self.logger.info('%s headlines_suggested_results', headlines_suggested_results)
        return headlines_suggested_results

    def get_tag_eyebrow_in_feed_results_page(self, eyebrow_in_articles, keyword):
        tag_articles_eyebrow = []
        index = 0
        collection_index = 0
        for element in eyebrow_in_articles:
            tag_eyebrow = self.remove_html_tags(element.get_attribute("innerHTML"))
            self.logger.info('%s tag_eyebrow', tag_eyebrow)
            tag_eyebrow_principal = tag_eyebrow.split("/ ")[1] if not (keyword.__contains__('ar-mena')) \
                else tag_eyebrow.split("- ")[1] + '- ' + tag_eyebrow.split("- ")[2]
            self.logger.info('%s tag_eyebrow_principal', tag_eyebrow_principal)
            self.logger.info('%s tag_to_filter', self.tag_to_filter)
            index += 1
            if 'collection' in tag_eyebrow_principal:
                collection_index += 1
                self.collections_dict.setdefault(collection_index, []).append(index)
                self.collections_dict.setdefault(collection_index, []).append(element)
            elif not(tag_eyebrow_principal.strip().startswith('From')) and (tag_eyebrow_principal != self.tag_to_filter):
                tag_eyebrow_secondary = tag_eyebrow.split("/ ")[2] if not (keyword.__contains__('ar-mena')) \
                        else tag_eyebrow.split("- ")[1] + '- ' + tag_eyebrow.split("- ")[2]
                tag_articles_eyebrow.append(tag_eyebrow_secondary)
            elif self.tag_to_filter in tag_eyebrow_principal:
                if tag_eyebrow_principal.strip().startswith("From"):
                    tag_articles_eyebrow.append(tag_eyebrow_principal[5:len(self.tag_to_filter)+6].strip())
                else:
                    tag_articles_eyebrow.append(tag_eyebrow_principal)
        if collection_index >= 1:
            assert self.get_collection_primary_tag(keyword)
        return tag_articles_eyebrow

    def get_collection_primary_tag(self, keyword):
        primary_tags_list = []
        for item in self.collections_dict.values():
            index = item[0]
            self.logger.info('%s elf.collections_dict', self.collections_dict)
            self.scroll_to_feed(index-1, keyword)
            self.click_on_collection_element(index)
            data_analytics = self.driver.find_element(*PageLocators.collection_data_analytics)
            primary_tag = (data_analytics.get_attribute("outerHTML").split("primaryTag")[1]).split("&quot;")[2]
            print('primary_tag', primary_tag)
            self.logger.info('%s primary_tag', primary_tag)
            primary_tags_list.append(primary_tag)
            self.driver.go_back_to_url()
        return self.contains_filtered_tag(self.tag_to_filter, primary_tags_list)

    def is_search_bar_visible(self):
        return self.driver.find_element(*PageLocators.search_bar_text_field).is_displayed()

    def is_search_bar_not_visible(self):
        self.driver.wait_for_element_not_visible(*PageLocators.search_bar_text_field)

    def is_searchbar_button_visible(self):
        return self.driver.find_element(*PageLocators.search_icon_nav_desktop).is_displayed()

    def is_search_results_header_visible(self):
        self.logger.info('%s search_bar',
                         self.driver.find_element(*PageLocators.search_results_header).get_attribute("outerHTML"))
        return self.driver.find_element(*PageLocators.search_results_header).is_displayed()

    def type_search_criteria(self, search_criteria):
        time.sleep(1)
        text_field = self.driver.find_element(*PageLocators.search_bar_text_field)
        text_field.send_keys(search_criteria)
