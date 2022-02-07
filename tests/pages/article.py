import time
import random

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class ArticlePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_date_in_article(self):
        return self.driver.find_element(*PageLocators.article_published_at)

    def get_secondary_tags_in_article(self):
        secondary_tags_list = self.driver.find_elements(*PageLocators.article_secondary_tags)
        tags_in_article = []
        for element in secondary_tags_list:
            tag_string = element.get_attribute("innerHTML")
            tag = self.replace_space(tag_string)
            tags_in_article.append(tag.lower())
        return tags_in_article








