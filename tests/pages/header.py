import time

import requests

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_cta_all_product_updates(self, locale):
        if locale == '/':
            self.driver.click_to_element(PageLocators.menu_all_product_updates_cta)

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

    def click_on_submenu_item(self, submenu):
        submenu_locator = self.get_item_selector(submenu, PageLocators.submenu_locators)
        self.driver.click_to_element(submenu_locator)

    def click_on_subscribe_cta(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.menu_subscribe_cta)

    def click_on_subscribe_cta_toast(self):
        time.sleep(2)
        self.driver.click_to_element(PageLocators.toast_bar_subscribe_cta)

    def click_see_all_cta_sub_menu(self):
        see_all_items = self.driver.get_urls_list(PageLocators.submenu_company_news_see_all_ctas)
        self.check_internal_status(see_all_items)

    def confirm_kebab_menu_opts(self, locale, option):
        kebab_option_selector = self.get_item_selector(option, PageLocators.kebab__options_locators)
        option_text_in_page = self.driver.find_element(*kebab_option_selector).text
        print('option_text_in_page', option_text_in_page)
        option_text_expected = self.get_kebab_opt_expected_text(locale, option)
        print('option_text_expected', option_text_expected)
        assert option_text_in_page == option_text_expected

    def get_publish_date_in_rss(self):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.driver.get_page_source(), 'xml')
        # print('all', soup.prettify())
        publish_date = soup.find('lastBuildDate').text
        date_formatted = self.get_date_in_api_format(publish_date[5:16], Constants.DATE_FORMAT_IN_RSS)
        return date_formatted

    @staticmethod
    def get_kebab_opt_expected_text(locale, option):
        for element, text in Constants.KEBAB_MENU_OPTIONS.items():
            if element == option + "_" + locale:
                return text

    def get_url_submenu_items(self, item, locators):
        for item_id, locator_item in locators.items():
            if item_id == item:
                return self.driver.get_urls_list(locator_item)
