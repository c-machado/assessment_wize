import time

from tests.pages.base_page import BasePage
from tests.pages.cookie_banner import CookieBanner
from tests.pages.locators import PageLocators


class Footer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_social_media_item(self, social_media):
        self.go_to_footer()
        time.sleep(1)
        self.driver.click_to_element(PageLocators.social_media_locators[social_media])

    def target_media_url(self, social_media):
        social_items_list = self.driver.get_elements_list(PageLocators.social_media_list)
        for social_item in social_items_list:
            item = social_item.get_attribute("aria-label")
            if item == social_media:
                return social_item.get_attribute("href")

    def get_legal_links(self):
        legal_links = self.driver.get_elements_list(PageLocators.legal_links_list)
        legal_items_urls_dic = {}
        for legal_item in legal_links:
            legal_items_urls_dic[legal_item.text] = legal_item.get_attribute("href")
            print('3', legal_items_urls_dic)
        return legal_items_urls_dic

    def go_to_footer(self):
        self.scroll_to_bottom()
        CookieBanner.close_cookie_banner(self)

    def verify_language_selector_content(self, locale):
        languages = self.driver.get_select_options(PageLocators.language_selector)
        for opt in languages.options:
            print('opt language selector: ', opt.text)
            if opt.text == locale:
                return True

