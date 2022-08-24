import logging
import time

import requests

from bs4 import BeautifulSoup

from tests.pages.base_page_api import BasePageAPI
from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Header(BasePage, BasePageAPI):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_site_space_index = 0
        self.site_space_url = ''
        self.site_space_title_in_products = ''
        self.logger = logging.getLogger(__name__)

    def click_cta_all_product_updates(self, locale, viewport):
        if locale == '/' and viewport == 'desktop':
            self.driver.click_to_element(PageLocators.menu_all_product_updates_cta_desktop)
        elif locale == '/' and viewport == 'mobile':
            self.driver.click_to_element(PageLocators.menu_all_product_updates_cta_mobile)

    def click_on_hamburger_menu(self):
        self.driver.click_to_element(PageLocators.hamburger_menu)

    def click_on_hamburger_rss(self):
        self.driver.click_to_element(PageLocators.hamburger_menu_rss)

    def click_on_nav_logo(self):
        self.driver.click_to_element(PageLocators.menu_keyword_logo)

    def click_on_kebab_menu(self):
        self.driver.click_to_element(PageLocators.kebab_toggle)

    def click_on_kebab_option(self, kebab_option):
        self.driver.click_to_element(PageLocators.kebab__options_locators[kebab_option])

    def click_on_submenu_item(self, submenu, get_viewport):
        if get_viewport == 'mobile':
            submenu_locator = self.get_item_selector(submenu, PageLocators.submenu_locators_mobile)
            self.driver.click_to_element(submenu_locator)
        elif get_viewport == 'desktop':
            submenu_locator = self.get_item_selector(submenu, PageLocators.submenu_locators_desktop)
            self.driver.click_to_element(submenu_locator)

    def click_on_subscribe_cta(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.menu_subscribe_cta)

    def click_on_subscribe_cta_on_sticky(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.menu_subscribe_cta)

    def click_on_subscribe_cta_mobile(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.menu_subscribe_mobile_hamburger_cta)

    def click_on_subscribe_cta_mobile_sticky(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.menu_subscribe_mobile_cta_sticky)

    def click_on_subscribe_cta_toast(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.toast_bar_subscribe_cta)

    def click_random_site_space(self, site_spaces_list):
        element = site_spaces_list[self.random_site_space_index]
        self.site_space_url = (element.get_attribute("outerHTML").split('href="')[1].split('" rel')[0])
        self.site_space_title_in_products = self.get_text_from_span(element)
        element.click()

    def click_see_all_cta_company_sub_menu(self, viewport):
        if viewport == 'desktop':
            see_all_items = self.driver.get_urls_list(PageLocators.submenu_company_news_see_all_ctas)
            self.check_internal_status(see_all_items)
        elif viewport == 'mobile':
            see_all_items = self.driver.get_urls_list(PageLocators.submenu_company_news_see_all_ctas_mobile)
            self.check_internal_status(see_all_items)

    def close_cookie_banner(self):
        self.close_bar(PageLocators.cookie_banner_ok_cta)

    def confirm_kebab_menu_opts(self, language, option):
        kebab_option_selector = self.get_item_selector(option, PageLocators.kebab__options_locators)
        option_text_in_page = self.driver.find_element(*kebab_option_selector).text
        self.logger.info('%s option_text_in_page', option_text_in_page)
        option_text_expected = self.get_kebab_opt_expected_text(language, option)
        self.logger.info('%s option_text_expected', option_text_expected)
        assert option_text_in_page == option_text_expected

    def get_sitespaces_list(self):
        self.close_bar(PageLocators.cookie_banner_ok_cta)
        site_spaces_list = self.driver.find_elements(*PageLocators.site_spaces_in_ads_and_analytics)
        self.logger.info('%s site_space_list ', site_spaces_list)
        return site_spaces_list

    def get_random_sitespace(self, site_spaces_list):
        self.random_site_space_index = self.get_random_index_in_list(site_spaces_list)

    def get_sitespace_title_expected_in_products(self):
        self.logger.info('%s random', self.random_site_space_index)
        return self.get_element_in_list(Constants.SITESPACE_TITLE_IN_PRODUCTS, self.random_site_space_index)

    def get_sitespace_title_expected_in_nav(self):
        return self.get_element_in_list(Constants.SITESPACE_TITLE_IN_NAV_MENU, self.random_site_space_index)

    def get_site_space_title_in_navigation(self):
        title_in_sitespace = self.driver.find_element(*PageLocators.site_space_title_in_nav_menu).get_attribute("innerHTML").strip()
        if self.contains_ampersand_char(title_in_sitespace):
            title_in_sitespace = self.replace_ampersand_char(title_in_sitespace)
            self.logger.info(title_in_sitespace)
        return title_in_sitespace

    def get_publish_date_in_rss(self):
        soup = BeautifulSoup(self.driver.get_page_source(), 'xml')
        publish_date = soup.find('lastBuildDate').text
        date_formatted = self.get_date_in_api_format(publish_date[5:16], Constants.DATE_FORMAT_IN_RSS)
        self.logger.info(date_formatted)
        return date_formatted

    @staticmethod
    def get_kebab_opt_expected_text(language, option):
        for element, text in Constants.KEBAB_MENU_OPTIONS.items():
            if element == option + "_" + language:
                return text

    def get_url_submenu_items(self, item, locators):
        for item_id, locator_item in locators.items():
            if item_id == item:
                return self.driver.get_urls_list(locator_item)

    def click_submenu_items_mobile(self, submenu):
        locator = self.get_item_selector(submenu, PageLocators.submenu_items_mobile)
        submenus_list = self.driver.find_elements(*locator)
        for element in submenus_list:
            element.click()
            time.sleep(1)
