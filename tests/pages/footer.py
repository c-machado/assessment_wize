import time

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Footer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_social_media_item(self, social_media):
        self.driver.click_to_element(PageLocators.social_media_locators[social_media])

    def click_google_logo(self):
        self.driver.click_to_element(PageLocators.cookie_banner_ok_cta)
        self.driver.click_to_element(PageLocators.footer_google_logo)

    def click_to_open_language_selector(self):
        self.driver.click_to_element(PageLocators.cookie_banner_ok_cta)
        self.driver.click_to_element(PageLocators.language_selector)

    def get_legal_links(self):
        legal_links = self.driver.get_elements_list(PageLocators.legal_links_list)
        legal_items_urls_dic = {}
        for legal_item in legal_links:
            legal_items_urls_dic[legal_item.text] = legal_item.get_attribute("href")
        # print('legal links in page', legal_items_urls_dic)
        return legal_items_urls_dic

    def get_expected_legal_links_per_locale(self, locale):
        about_link = self.get_about_blog_legal_links_expected_per_locale(locale)
        for locale_legal_items in Constants.LEGAL_LINKS.items():
            if locale_legal_items[0] == locale:
                locale_legal_links = locale_legal_items[1]
                legal_links_expected = {**locale_legal_links, **about_link}
                return legal_links_expected

    @staticmethod
    def get_about_blog_legal_links_expected_per_locale(locale):
        about_blog_legal_links = {**Constants.LEGAL_LINKS_ABOUT_THE_BLOG_URL, **Constants.LEGAL_LINKS_ABOUT_THE_BLOG_COPY}
        locale_legal_about = {}
        for key, value in about_blog_legal_links.items():
            if key in Constants.LEGAL_LINKS_ABOUT_THE_BLOG_URL and key in Constants.LEGAL_LINKS_ABOUT_THE_BLOG_COPY:
                if key == locale:
                    locale_legal_about[value] = Constants.BASE_URL+Constants.LEGAL_LINKS_ABOUT_THE_BLOG_URL[key]
                    return locale_legal_about

    def go_to_footer(self):
        self.scroll_to_bottom()

    def target_media_url(self, social_media):
        social_items_list = self.driver.get_elements_list(PageLocators.social_media_list)
        for social_item in social_items_list:
            item = social_item.get_attribute("aria-label")
            if item == social_media:
                return social_item.get_attribute("href")

    def verify_language_selector_content(self, locale):
        languages = self.driver.get_select_options(PageLocators.language_selector)
        for opt in languages.options:
            print('opt language selector: ', opt.text)
            if opt.text == locale:
                return True

