from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class CookieBanner(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_read_more_article(self, viewport):
        if viewport == 'mobile':
            self.driver.click_to_element(PageLocators.article_read_more_mobile)
        elif viewport == 'desktop':
            self.driver.click_to_element(PageLocators.article_read_more_cta)

    def close_cookie_banner(self):
        self.close_bar(PageLocators.cookie_banner_ok_cta)

    def get_cookie_text_in_page(self):
        self.driver.find_element(*PageLocators.cookie_banner_bar)

    @staticmethod
    def get_cookie_text_per_language(language):
        for cookie_copy, language_id in Constants.COOKIE_BANNER_TXT.items():
            if language_id == language:
                return cookie_copy

    def click_see_details_cta(self):
        self.driver.click_to_element(PageLocators.cookie_see_details_cta)

    def cookie_not_displayed(self):
        self.driver.wait_for_element_not_visible(PageLocators.cookie_banner_bar)
