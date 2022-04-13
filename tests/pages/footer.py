import logging
import re
import time

import requests

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Footer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.languages = []
        self.logger = logging.getLogger(__name__)

    def click_social_media_item(self, social_media):
        self.driver.click_to_element(PageLocators.social_media_locators[social_media])

    def click_google_logo(self):
        self.driver.click_to_element(PageLocators.footer_google_logo)

    def click_to_each_language_in_selector(self):
        self.close_cookie_banner()
        languages = self.driver.get_select_options(PageLocators.language_selector)
        is_status_valid = True
        for opt in languages.options:
            url = Constants.BASE_URL + opt.get_attribute("value")
            response = requests.get(url)
            if response.status_code != 200:
                is_status_valid = False
            self.languages.append(opt.text)
        return is_status_valid

    def click_all_social_media_links(self):
        social_media_items = self.get_social_media_items()
        is_status_valid = True
        for social_item in social_media_items:
            response = requests.get(social_item.get_attribute("href"))
            if response.status_code == 404:
                is_status_valid = False
        return is_status_valid

    def close_cookie_banner(self):
        self.close_bar(PageLocators.cookie_banner_ok_cta)

    def confirm_links_opened_in_a_new_tab(self):
        social_media_items = self.get_social_media_items()
        is_target_valid = True
        for socialItem in social_media_items:
            target = socialItem.get_attribute("target")
            if target != '_blank':
                is_target_valid = False
        return is_target_valid

    def confirm_social_media_url_is_secure(self):
        social_media_items = self.get_social_media_items()
        is_url_secure = True
        for social_item in social_media_items:
            # valid_url = re.compile("http[s]?:", social_item.get_attribute("href"))
            # print('valid_url', valid_url)
            social_item_url = social_item.get_attribute("href")
            if not social_item_url.startswith("https://"):
                self.logger.error(social_item_url)
                is_url_secure = False
        return is_url_secure

    def get_social_media_items(self):
        return self.driver.find_elements(*PageLocators.social_media_list)

    def get_legal_links(self):
        legal_links = self.driver.get_elements_list(PageLocators.legal_links_list)
        legal_items_urls_dic = {}
        for legal_item in legal_links:
            legal_items_urls_dic[legal_item.text] = legal_item.get_attribute("href")
        return legal_items_urls_dic

    def get_expected_legal_links_per_locale(self, locale):
        """:return two dictionaries (legal links and about) joined"""
        about_link = self.get_about_blog_legal_links_expected_per_locale(locale)
        legal_links_expected = {}
        for locale_legal_items in Constants.LEGAL_LINKS.items():
            if locale_legal_items[0] == locale and about_link is not None:
                locale_legal_links = locale_legal_items[1]
                legal_links_expected = {**locale_legal_links, **about_link}
            elif locale_legal_items[0] == locale and about_link is None:
                legal_links_expected = locale_legal_items[1]
        return legal_links_expected

    @staticmethod
    def get_about_blog_legal_links_expected_per_locale(locale):
        about_blog_legal_links = {**Constants.LEGAL_LINKS_ABOUT_THE_BLOG_URL,
                                  **Constants.LEGAL_LINKS_ABOUT_THE_BLOG_COPY}
        locale_legal_about = {}
        for key, value in about_blog_legal_links.items():
            if key in Constants.LEGAL_LINKS_ABOUT_THE_BLOG_URL and key in Constants.LEGAL_LINKS_ABOUT_THE_BLOG_COPY:
                if key == locale:
                    locale_legal_about[value] = Constants.BASE_URL + Constants.LEGAL_LINKS_ABOUT_THE_BLOG_URL[key]
                    return locale_legal_about

    def go_to_footer(self):
        self.scroll_to_bottom()

    def target_media_url(self, social_media):
        social_items_list = self.driver.get_elements_list(PageLocators.social_media_list)
        for social_item in social_items_list:
            item = social_item.get_attribute("aria-label")
            if item == social_media:
                return social_item.get_attribute("href")
