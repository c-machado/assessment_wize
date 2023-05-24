import logging
import re
import time

import requests

from tests.consts import api_const
from tests.pages.base_page import BasePage
from tests.pages.base_page_api import BasePageAPI
from tests.pages.locators import PageLocators


class PressAssets(BasePage, BasePageAPI):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_option_in_filter_by(self, select_options, type_of_filter):
        # filter_options_list = []
        for opt in select_options.options:
            filter_option = opt.get_attribute('innerHTML').strip()
            if self.contains_ampersand_char(filter_option):
                filter_option = re.sub('&amp;', '&', filter_option)
            if type_of_filter == filter_option:
                self.logger.info(type_of_filter)
                opt.click()
                # filter_options_list.append(filter_option)

    # TODO: Find a way to send the parameter tag_filter as optional, so we can use the same function to get the api_url
    def get_api_url_with_type_and_tag(self, type_filter, tag_filter, keyword):
        print('type_filter', type_filter)
        print('tag_filter', tag_filter)
        locale_url = self.get_locale_url(keyword)
        api_url = api_const.PRESS_ASSETS_PER_TYPE_AND_TAG_API[locale_url]
        type_filter = self.format_ampersand_in_type_url(type_filter)
        tag_filter = self.format_ampersand_in_url(tag_filter)
        api_url_with_type_and_tag = (
            self.get_api_url_with_type_and_tag_parameters(
                api_url, type_filter, tag_filter
            )
        )
        return api_url_with_type_and_tag

    def get_api_url_with_type(self, type_filter, keyword):
        locale_url = self.get_locale_url(keyword)
        api_url = api_const.PRESS_ASSETS_PER_TYPE_API[locale_url]
        type_filter = self.format_ampersand_in_type_url(type_filter)
        api_url_with_type = self.get_api_url_with_updated_parameters(
            api_url, type_filter
        )
        return api_url_with_type

    def get_results_filter_by_type(self, filter_by_type):
        select_opts_per_type = self.driver.get_select_options(
            PageLocators.press_filter_by_type
        )
        self.click_option_in_filter_by(select_opts_per_type, filter_by_type)
        # TODO: Explore a different solution to avoid using time sleep.
        #  This is required because the stage is taking too long to load the content filtered.
        #  It's the same in the examples below
        time.sleep(1)

    def get_results_filter_by_product(self, filter_by_product):
        select_opts_per_product = self.driver.get_select_options(
            PageLocators.press_filter_by_product
        )
        self.click_option_in_filter_by(
            select_opts_per_product, filter_by_product
        )
        time.sleep(1)

    def get_results_filter_by_topic(self, filter_by_topic):
        select_opts_per_topic = self.driver.get_select_options(
            PageLocators.press_filter_by_topic
        )
        self.click_option_in_filter_by(select_opts_per_topic, filter_by_topic)
        time.sleep(1)

    def get_titles_in_press_assets_page(self):
        titles = []
        number_of_results = self.driver.find_element(
            *PageLocators.press_number_of_results
        ).get_attribute('innerHTML')
        if not number_of_results.startswith('0'):
            titles_list = self.driver.find_elements(
                *PageLocators.press_titles_in_page
            )
            for title in titles_list:
                titles.append(title.get_attribute('innerHTML'))
        return titles

    @staticmethod
    def confirm_download_url_per_assets(download_urls_list):
        is_status_valid = True
        for url in download_urls_list:
            response = requests.get(url)
            status = response.status_code
            if status != 200:
                is_status_valid = False
        return is_status_valid
