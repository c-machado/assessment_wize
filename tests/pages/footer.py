import requests

from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Footer(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def click_social_media_item(self, social_media):
        self.scroll_to_bottom()
        self.close_cookie_banner()
        # self.scroll_to_content()
        self.browser.click_to_element(PageLocators.social_media_locators[social_media])

    def target_media_url(self, social_media):
        social_items_list = self.browser.get_elements_list(PageLocators.social_media_list)
        for social_item in social_items_list:
            item = social_item.get_attribute("aria-label")
            if item == social_media:
                return social_item.get_attribute("href")

    def get_legal_links(self):
        legal_links = self.browser.get_elements_list(PageLocators.legal_links_list)
        legal_items_urls_dic = {}
        for legal_item in legal_links:
            legal_items_urls_dic[legal_item.text] = legal_item.get_attribute("href")
            print('3', legal_items_urls_dic)
        return legal_items_urls_dic

